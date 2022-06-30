sort the dictionary using the item's key. For this use the operator module.

Pass the function itemgetter() as an argument to the sorted() function.

fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}

import operator
sorted(fruit.items(), key=operator.itemgetter(0))
[('apples', 5), ('bananas', 7), ('oranges', 3), ('pears', 2)]

sorted(fruit.items(), key=operator.itemgetter(1))
[('pears', 2), ('oranges', 3), ('apples', 5), ('bananas', 7)]



