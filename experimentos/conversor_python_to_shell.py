#!/bin/python
import os
while 1!=0:
 current_directory = os.popen("pwd")
 type(current_directory)
 print(current_directory.read())
 input_string = input()
 output = os.popen(input_string)
 type(output)
 print(output.read())
