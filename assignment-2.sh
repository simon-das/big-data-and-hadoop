#!/bin/bash

#checking if there is exactly one argument or not
if [ $# -eq 1 ]; then
   #flag variable
   f=1
   #field number storing variable
   v=`cat $1 | awk -F: {'print NF'}`
   
   #loop to check if there are lines with fields not equal to 7
   for i in $v
   do
   if [ $i != 7 -a $i != 0 ]; then
      f=0
      break
   fi
   done

   #if the argument is a passwd file then do the main operation
   if [ $f == 1 ]; then
      echo "Duplicate users are as follows:"
      cat $1 | awk -F: {'print $1'} | sort | uniq -d
      echo "Unique shell used among all the duplicate users above:"
      cat $1 | awk -F: {'print $7, $1'} | sort -k 2 | uniq -f 1 -D | awk '{print $1}' | sort | uniq

   #if the argument isn't a passwd file then print the following error
   else
      echo "Error: All of the lines(without the blank line/lines) don't have 7 fields as a passwd file should have."
   fi

#if there isn't exactly one argument then print the following error
else
   echo "Error: Only one passwd file is expected as argument. But $# arguments found!"
fi
