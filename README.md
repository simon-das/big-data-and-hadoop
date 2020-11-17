# Assignment-1
### Problem Description:
You will be given variable number of TXT files having different types of ASCII sentences. A python program must be developed to accept all these file names as arguments 
and the output shall provide all the word counts in single output.
### Output can be shown as:
{'am': 1, 'python': 1, 'affraid': 1, 'want': 1, 'learn': 1, 'of': 1, 'to': 1, 'I': 2, 'python.': 1, 'But': 1}
### Instruction to be followed:
1. Testing procedure: <yourpythoncode.py> <file1> <file2> <file3>…<fileN>
2. The python binaries shall be 3.x
3. Files can be in your current directory or in different directory
4. You need to show the running time of your program in seconds
5. You can’t use any external library to satisfy the requirement except basic python libraries.

# Assignment-2
### Problem Description:
You have been given with a UNIX passwd file having all the user’s details. Now you need to develop a shell script which will be taking out only duplicate usernames and 
their unique shell names as output from the given file. In addition, you need to take the passwd file as input in the shell script.
### Output can be shown as:
###### _Duplicate users are as follows:_  
adm  
halt  
games  
[…continue printing usernames in same fashion above for more duplicate users]  
###### _Unique shell used among all the duplicate users above:_  
/bin/sh  
/bin/bash  
/bin/csh  
[…continue printing shell names in same fashion above for more cases]
### Instruction to be followed:
1. Testing procedure: <yourpythoncode.py> <file1> <file2> <file3>…<fileN>
2. The python binaries shall be 3.x
3. Files can be in your current directory or in different directory
4. You need to show the running time of your program in seconds
5. You can’t use any external library to satisfy the requirement except basic python libraries.

# Assignment-3
### Problem Description:
We all know that Covid-19 pandemic is going on world-wide and almost every corner of the world is impacted globally. You are given with a Covid-19 dataset collected from the 
internet to do certain analysis.  
**All the raw responses are kept in file named Covid_Analysis_DataSet.csv  
Detail schema is self-explanatory.**
###### _The following analytics shall be done:_
Month, Year and countryterritoryCode wise, please derive Infection Rate and Death Rate.  
###### _Note:_
Infection Rate = (cases / TestPerformed) * 100%
Death Rate = (deaths / cases) * 100%

### Output can be shown as:
Month;Year;CountryCode;InfectionRate;DeathRate  
September;2020; AFG;3;10  
October;2020; AFG;5;12  
### Instruction to be followed:
1.	Consider Raw Capture file shall be loaded in HDFS /ASSIGNMENT directory hourly from external program. So, you will get the mentioned file in the designed location 
periodically.
2.	Process all the outputs in Apache Spark in Standalone Cluster Mode
3.	Store all the results in HDFS /OUTPUT in mentioned CSV format (; separated file)
4.	Schedule the spark job to run in every hour at 15 minutes
5.	You need to submit following files as ZIP format and naming convention as suggested by earlier assignment in this course:  
  a.	Python Program  
  b.	Shell Script  
  c.	Crontab Configuration Text File  

