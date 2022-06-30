Imagine one of your IT coworkers just retired and left a folder of scripts for you to use. One of the scripts,
called emails.py, matches users to an email address and lets us easily look them up! For the most part, the script works
great — you enter an employee's name and their email is printed to the screen. But, for some employees, the output
doesn't look quite right. Your job is to add a test to reproduce the bug, make the necessary corrections, and verify
that all the tests pass to make sure the script works! Best of luck!

--------------------------------

The script accepts arguments through the command line. These arguments are stored in a list named sys.argv.
The first element of this list, i.e. argv[0], is always the name of the file being executed.
So the parameters, i.e., first name and last name, are then stored in argv[1] and argv[2] respectively.
----------------------------------
A test case is an individual unit of testing that checks for a specific response to a particular set of inputs.

The package unittest supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into
collections, and independence of the tests from the reporting framework.
This module also provides classes that make it simple to support these qualities for a set of tests.

Another important aspect of the unittest module is the test runner. A test runner is a component that orchestrates
the execution of tests and provides the outcome to the user.
-----------------------------------
The following import statement allows a Python file to access the script from another Python file. In this case,
we will import the function find_email, which is defined in the script emails.py.

from emails import find_email

Here, variable test case contains the parameters to be passed to the script emails.py. As we mentioned, the script file
is the first element of input parameters through command line using argv. Since we already imported the function
find_email from emails.py earlier, we will pass None in place of the script file and call it later in the script.
Adding to None, we will pass a first name and last name as parameters.
-----------------------------------
Classes are a way to bundle data and functionality together. Creating a new class creates a new type of object,
which further allows new instances of that type to be made.

The method assertEqual passes the test case to the function find_email, which we imported earlier from emails.py,
and checks whether it generates the expected output.

