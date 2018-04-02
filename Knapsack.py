 '''
 creating a class Food, which does some simple tasks
 1) Initialization
 2) getter methods
 3) creating nice string representation to be returned
 '''
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
        return self.names + '<' + str(self.values) + ', ' + str(self.calories) + '>'

'''
this function will return a list
It basically takes 3 lists as input, and returns the menu list which contains each item with the value and calories associated with it
'''
def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu

'''
This function returns the resulting list and the total value based on the computation done with regards to keyFunction
'''
def greedy(items, maxCost, keyFunction):
    itemsCopy = sorted(items, key=keyFunction, reverse = True) #using sorted instead of sort as it will create a new copy of list, setting reverse true as we want the order to be from best to worst                     
    results = []
    totalValue, totalCost = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if(totalCost+itemsCopy[i].getCost()) <= maxCost: #maxCost is the constraint we have in place
            results.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return results, totalValue

'''
This function just does the printing, takes the input, calls the greedy function, and prints out the result
'''
def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(foods, constraint, keyFunction)
    print('Total value of items taken =', val)
    for item in taken:
        print('  ', item)

'''
Function calls testGreedy
'''
def testGreedys(items, maxUnit):
    print("based on value")
    testGreedy(foods, maxUnit, Food.getValue) #notice the 3rd parameter this is the keyFunction based on which the computation happens
    print("based on cost")
    testGreedy(foods, maxUnit, lambda x: 1/Food.getCost(x))
    print("based on density")
    testGreedy(foods, maxUnit, Food.density)

names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)
testGreedys(foods, 1000)
