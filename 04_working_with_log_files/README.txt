Imagine one of your colleagues is struggling with a program that keeps throwing an error. Unfortunately, the program's
source code is too complicated to easily find the error there. The good news is that the program outputs a log file
you can read! Let's write a script to search the log file for the exact error, then output that error into a separate
file. so you can work out what's wrong.
----------------------------------------
View log file
In the /data directory, there's a file named fishy.log, which contains the system log. Log entries are written in this format:

Month Day hour:minute:second mycomputername "process_name"["random 5 digit number"] "ERROR/INFO/WARN" "Error description"

For every process, the runtime log that's generated contains a timestamp and appropriate message alongside.
-----------------------------------------
The sys module provides information about the Python interpreter's constants, functions, and methods.
The os module provides a portable way of using operating system dependent functionality with Python.

Regular Expression (RegEx) is a sequence of characters that defines a search pattern. We can use regular expressions using re module.
------------------------------------------
we'll use the method os.path.expanduser ('~'), which returns the home directory of your system instance. Then,
we'll concatenate this path (to the home directory) to the file errors_found.log in /data directory.
------------------------------------------
sys.exit(0) is used to exit from Python, the optional argument passed can be an integer giving the exit status (defaulting to zero), or
another type of object. If it is an integer, zero is considered "successful termination" and any nonzero value is considered an
"abnormal termination" by shells.
-------------------------------------------

