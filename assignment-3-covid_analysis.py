from pyspark import SparkConf, SparkContext, SQLContext 
from hdfs import Config
from pyspark.sql import functions as func
from pyspark.sql.types import IntegerType
import sys, os, math
 
# Constants 
APP_NAME = "Covid Analysis" 
HDFS_RAWFILE_DIR = "/ASSIGNMENT/"
HDFS_OUTPUT_DIR = "/OUTPUT/" 
HDFS_BASE_URL = "hdfs://bdrenfdludcf01:9000" 
 
 
if __name__ == "__main__": 
 
    # Folder creation for placing all the spark data 
    cmd_a = "mkdir -p " + "/tmp/SPARK_PROCESS/" 
    os.system(cmd_a) 
 
    # Configure Spark 
    conf = SparkConf().setAppName(APP_NAME).set("spark.local.dir", "/tmp/SPARK_PROCESS/") 

    sc = SparkContext(conf=conf)
    sqlContext = SQLContext(sc) 
    client = Config().get_client('bdrenhdfs') 
    files = client.list(HDFS_RAWFILE_DIR) 
    totalfilecount = len(files) 
 
    if totalfilecount == 0: 
        print("There is no files to be processed, application exiting...") 
        sys.exit(0) 
 
    filecount = 0 
 
    for filename in files: 
        print(filename) 
        if filename.find("Covid_Analysis_DataSet.csv") >= 0: 
            filecount = filecount + 1 
            df_covid = sqlContext.read.format("csv").option("delimiter", ":").option("header", 'true').load(HDFS_BASE_URL + HDFS_RAWFILE_DIR + filename)
 
    if filecount == 0: 
        print("The desired file is not present here, application exiting...") 
        system.exit(0)

    
    #converting month and year to integer
    df_covid_month_year_int = df_covid.withColumn("month", df_covid["month"].cast(IntegerType())).withColumn("year", df_covid["year"].cast(IntegerType()))

    #creating temporary view
    df_covid_month_year_int.createOrReplaceTempView("covid") 

    #main query
    sqlDF = sqlContext.sql("SELECT month Month, year Year, countryterritoryCode CountryCode, (sum(cases)/sum(TestPerformed))*100 InfectionRate, (sum(deaths)/sum(cases))*100 DeathRate FROM covid group by month, year, countryterritoryCode").orderBy('CountryCode', 'year', 'month')

    #changing month format
    sqlDF_month_updated = sqlDF.withColumn("Month", func.when(sqlDF["Month"]==1, "January").when(sqlDF["Month"]==2, "February").when(sqlDF["Month"]==3, "March").when(sqlDF["Month"]==4, "April").when(sqlDF["Month"]==5, "May").when(sqlDF["Month"]==6, "June").when(sqlDF["Month"]==7, "July").when(sqlDF["Month"]==8, "August").when(sqlDF["Month"]==9, "September").when(sqlDF["Month"]==10, "October").when(sqlDF["Month"]==11, "November").when(sqlDF["Month"]==12, "December").otherwise(sqlDF["Month"]))

    #rounding the InfectionRate and DeathRate
    sqlDF_rounded = sqlDF_month_updated.withColumn("InfectionRate", func.round(sqlDF_month_updated["InfectionRate"], 2)).withColumn("DeathRate", func.round(sqlDF_month_updated["DeathRate"], 2))

    #showing the output
    sqlDF_rounded.show()

    #writing the output in a output.csv file
    sqlDF_rounded.coalesce(1).write.mode("overwrite").option("delimiter", ";").option("header", 'true').csv(HDFS_BASE_URL + HDFS_OUTPUT_DIR + "output.csv") 

    #call shutdown to release all resources properly
    sc.stop() 
