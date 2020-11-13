import sys
import time

if __name__ == '__main__':

    startTime = time.time()
    counts = {}
    
    for fileName in sys.argv:
        if fileName == sys.argv[0]:
            pass
        else:
            try:
                fileOpen = open(fileName, "r+")
                while True:
                    line = fileOpen.readline()
                    if not line:
                        break
                    words = line.split()
                    for word in words:
                        if word in counts:
                            counts[word] = counts[word]+1
                        else:
                            counts[word] = 1
            except IOError:
                print("\n", fileName, " is not found.")

    print("\n", counts)
    finishTime = time.time()
    print("Time taken : ", finishTime - startTime, end = "s\n")

    exit(0)
    
