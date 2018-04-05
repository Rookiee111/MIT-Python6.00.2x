"""
this is a test of dynamic programming, and how it can better improve the performance of the algorithm
In this example we have considered a knapsack problem, the idea is we have menu of items and we have to fill the knapsack with the items
with the constraint that we do not go beyond a certain number of calories
"""
"""
There are 3 functions, one to build a menu, one without dynamic programming ( MaxVal) and one with dynamic programming (FastMaxVal)
"""

import random
import sys
sys.setrecursionlimit(2000) #setting the recursion limmit to 2000, by default it is 1000, if the depth goes beyond 1000 the error is thrown
#creating a class, this serves the basic purpose , initializing, defined getter methods and finally method to return a presenteable output of an object
class Food(object):
    def __init__(self, n, v, c):
        self.names = n
        self.values = v
        self.calories = c

    def getValue(self):
        return self.values

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue()/self.getCost()

    def __str__(self):
        return self.names + "<" + str(self.values) + "," + str(self.calories) + ">"


#def buildMenu(names, values, calories):
#    menu = []
#    for x in range(len(values)):
#        menu.append(Food(names[i], values[i], calories[i]))
#    return menu

# building a list items, we use random generator to generate random numbers
def buildLargerMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food(str(i), random.randint(1, maxVal), random.randint(1, maxCost)))
    return items

# this is the MaxVal function without any optimization
def MaxVal(toConsider, avail):
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        result = MaxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        withVal, withValTaken = MaxVal(toConsider[1:], avail - nextItem.getCost())
        withVal += nextItem.getValue()
        #if i do not consider the next Value
        withoutValue, wihtoutTaken = MaxVal(toConsider[1:], avail)
        if withVal > withoutValue:
            result = (withVal, withValTaken + (nextItem, ))
        else:
            result = (withoutValue, wihtoutTaken)
    return result

#FastMaxVal -> optimized version, created a dictionary to store or record values. So we are actually recoarding scenarios
# for example we index (len(toConsider), avail) as key -> so we are storing the number of items yet to be considered and how many calories are left,
#based on the scenario if the code comes across a state where it has already computed a scenario for specific (len(toConsider), avail) then instead of recomputing
# it just retrieves from dictionary
#example: if a result is computed for len(toConsider) -> 5 and avail = 300, then next item it won't compute this will get it from dictionary

def fastMaxVal(toConsider, avail, memo={}):
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        nextVal, withVal = fastMaxVal(toConsider[1:], avail - nextItem.getCost(), memo)
        nextVal += nextItem.getValue()
        withoutVal, withouttaken = fastMaxVal(toConsider[1:], avail, memo)
        if nextVal > withoutVal:
            result = (nextVal, withVal + (nextItem, ))
        else:
            result = (withoutVal, withouttaken)
    memo[(len(toConsider), avail)] = result
    return result

def testMaxVal(foods, maxCost, algorithm, printItems = True):
    print("menu contains", len(foods), 'items')
    print("search tree allocating", maxCost, "units")
    val, taken = algorithm(foods, maxCost)
    print("total Value:", val)
    if printItems:
        for item in taken:
            print("  ", item)


#testing by generating different number of items
for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45, 50):
    foods = buildLargerMenu(numItems, 90, 250)
    testMaxVal(foods, 750, fastMaxVal, False)
