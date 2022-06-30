Imagine your company uses a server that runs a service called ticky, an internal ticketing system.
The service logs events to syslog, both when it runs successfully and when it encounters errors.

The service's developers need your help getting some information from those logs so that they can better understand
how their software is used and how to improve it. So, for this lab, you'll write some automation scripts that will
process the system log and generate reports based on the information extracted from the log files.


--------------------------------------------------------------
sort the dictionary using the item's key. For this use the operator module.

Pass the function itemgetter() as an argument to the sorted() function.

fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}

import operator
sorted(fruit.items(), key=operator.itemgetter(0))
[('apples', 5), ('bananas', 7), ('oranges', 3), ('pears', 2)]

sorted(fruit.items(), key=operator.itemgetter(1))
[('pears', 2), ('oranges', 3), ('apples', 5), ('bananas', 7)]
--------------------------------------------------------------


