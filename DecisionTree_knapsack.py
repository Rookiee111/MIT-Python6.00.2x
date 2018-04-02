"""
This algorithm returns an optimal solution to the problem as it follows brute force methodology, however the problem is with the efficiency. 
This has the complexity of 2^(n+1), which is not efficient when compared with Greedy that has effeciency nlogn, however Greedy does not 
promise global optimized solution
"""
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
        return self.names + "<" + str(self.values) + ", " + str(self.calories) + ">"

def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu

'''
this function will do tree based computation
it takes 2 arguments
toConsider -> this is to either pick that element or not to pick
avail -> this is the constraint put in replace
this is a left first depth first search, which means it will check the entire left branch before tracking back to the next possibility
'''
def maxVal(toConsider, avail):
    if toConsider == [] or avail == 0: #if either the toConsider list is empty or if available cost is 0 then return an empty tuples
        result = (0, ())
    elif toConsider[0].getCost() > avail: #checking if the item that is to be considered has its cost greater than the avail constraint, if yes, then pick the next one
        result = maxVal(toConsider[1:], avail) #making the recursive call to start with the next items
    else:
        nextItem = toConsider[0] # We decide to pick the next available item
        #Since we decided to pick the item, we are next going to check for next item in the list and also reduce the available cost
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getCost())
        withVal += nextItem.getValue()
        #The other option is if we decide not to pick the next available item
        withoutVal, withOutTake = maxVal(toConsider[1:], avail)
        if withVal > withoutVal: #checking which is the better choice to take
            result = (withVal, withToTake + (nextItem, ))
        else:
            result = (withoutVal, withOutTake)
    return result

def testmaxVal(foods, maxUnit, printItems=True):
    val, taken = maxVal(foods, maxUnit)
    print("total value: ", val)
    if printItems:
        for item in taken:
            print('  ', item)


names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)
testmaxVal(foods, 750)
