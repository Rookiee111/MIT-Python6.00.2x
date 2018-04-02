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

def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))

    return menu
def greedy(items, maxCost, keyFunction):
    itemsCopy = sorted(items, key=keyFunction, reverse = True)
    results = []
    totalValue, totalCost = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if(totalCost+itemsCopy[i].getCost()) <= maxCost:
            results.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return results, totalValue

def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(foods, constraint, keyFunction)
    print('Total value of items taken =', val)
    for item in taken:
        print('  ', item)

def testGreedys(items, maxUnit):
    print("based on value")
    testGreedy(foods, maxUnit, Food.getValue)
    print("based on cost")
    testGreedy(foods, maxUnit, lambda x: 1/Food.getCost(x))
    print("based on density")
    testGreedy(foods, maxUnit, Food.density)

names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)
testGreedys(foods, 1000)
