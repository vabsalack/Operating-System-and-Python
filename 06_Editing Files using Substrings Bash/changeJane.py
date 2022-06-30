#!/usr/bin/env python3
import sys
import subprocess


myfile = open("oldFiles.txt","r")
data = myfile.read()
new_string = data.replace('jane','jdoe')
print(new_string)
subprocess.run(["mv", myfile, new_string])