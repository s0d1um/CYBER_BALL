#!/bin/python
import os
#list_directories = os.popen("find |grep .py|grep juga")
list_directories = os.popen("perl -pi -e 's/MV9600/MV9600/g' *.py")
type(list_directories)
print(list_directories.read())
input_string = "find"
output = os.popen(input_string)
type(output)
print(output.read())
Prelude> concatMap (\x -> if x == '.' then "foo" else [x])



while 1!=0:
 comand = "cd "+list_directories
 input_string = comand
 output = os.popen(input_string)
 type(output)
 print(output.read())
 #perl -pi -e 's/MV9600/MV9600/g' *.py
 print()
