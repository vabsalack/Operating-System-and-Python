you'll change the username of your coworker Jane Doe from "jane" to "jdoe" in compliance with company's naming policy.
The username change has already been done. However, some files that were named with Jane's previous username "jane"
haven't been updated yet. To help with this, you'll write a bash script and a Python script that will take care of the
necessary rename operations.

---------------------------------
cat: cat [file]

The cat command allows us to create single or multiple files, view the contents of a file, concatenate files, and
redirect output in terminal or other files.
----------------------------------
grep: grep [pattern] [file-directory]

The grep command, which stands for "global regular expression print", processes text line-by-line and prints any
lines that match a specified pattern.

Here, [file-directory] is the path to the directory/folder where you want to perform a search operation.
The grep command is also used to search text and match a string or pattern within a file.
----------------------------------
cut: cut [options] [file], cut -d [delimiter] -f [field number], cut -d ' ' -f 1-3, cut -d ' ' -f 1,3

The cut command extracts a given number of characters or columns from a file. A delimiter is a character
or set of characters that separate text strings.
For delimiter separated fields, the - d option is used. The -f option specifies the field, a set of fields, or a
range of fields to be extracted.
------------------------------------
test: test -e ~/data/jane_profile_07272018.doc

the test command to test for the presence of a file. The command test is a command-line utility on Unix-like
operating systems that evaluate conditional expressions.

We'll use this command to check if a particular file is present in the file system. We do this by using the -e flag.
This flag takes a filename as a parameter and returns True if the file exists.
--------------------------------------
import sys
import subprocess

The sys (System-specific parameters and functions) module provides access to some variables used or maintained by the
interpreter and to functions that interact with the interpreter. The subprocess module allows you to spawn new processes,
connect to their input/output/error pipes, and get their return codes.







