"""
Testing the complexity of two algorithms, the algo does the same set_access_token
of searching the minimum value, but the order of magnitude for
1) is O(n^2)
2) O(n)
so 1 is Quadratic
2nd is linear
finally we plot this for better understanding
"""

import time # timing the run
from random import randrange #using random function to generate numbers
import pylab as plt #pylab module to generate the graph
'''
function algocomplexitycheck1 is of complexity O(n^2)
'''
def algocomplexitycheck1(lst):
    count = 0
    for i in range(len(lst)):
        count += 1
        for j in range(i+1, len(lst)):
            count += 1
            if lst[i] > lst[j]:
                #count += 1
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    min = lst[0]
    return min, count

'''
function algocomplexitycheck2 is of complexity O(n)
'''

def algocomplexitycheck2(lst):
    minsofar = lst[0]
    for i in range(len(lst)):
        if lst[i] < minsofar:
            minsofar = lst[i]
    return minsofar

#lst = [5,4,3,2,1]
#lst3 = [0,4,1,2,5]
#lst2 = [1,2,3,4,5]
#print(algocomplexitycheck1(lst3)


#creating lists to store values for graph generation
timedlist1 = []
timedlist2 = []
lst_test = []
for size in range(1000, 10001, 1000): #using range function to create new lists size with gap 1000
    lst4 = [randrange(100000) for x in range(size)] #generating random no's based on list size
    start1 = time.time()
    print("for algo one:",algocomplexitycheck1(lst4))
    end1 = time.time()
    timedlist1.append(end1 - start1) #time difference for algo 1
    start2 = time.time()
    print("for algo two:",algocomplexitycheck2(lst4))
    end2 = time.time()
    timedlist2.append(end2 - start2) #time difference for algo 2
    lst_test.append(size)  #appending the size of the list to a list, this will be the base for plotting graph
    #print("For list size of %d the time taken is %f" % (size, end-start))

#plotting the graph
plt.plot(lst_test, timedlist1, "b-", label="ExecutionAlgo1", linewidth=2.0) 
plt.plot(lst_test, timedlist2, "r--", label="ExecutionAlgo2", linewidth=3.0)
plt.show()





