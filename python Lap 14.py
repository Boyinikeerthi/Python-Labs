# 1.write a python program to get only unique items from two sets.
#set1={10,20,30,40,50}
#set2={30,40,50,60,70}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
s=set1.union(set2)
print("Unique items:", s)



# 2.write a python program to return a set of elements present in set3 or 4, but not both.
#set3={10,20,30,40,50}
#set4={30,40,50,60,70}

set3={10,20,30,40,50}
set4={30,40,50,60,70}
print(set3.symmetric_difference(set4))



# 3.write a python program to check if two sets have any elements in common.if yes, display the common elements.
#set5={10,20,30,40,50}
#set6={60,70,80,90,10}

set5={10,20,30,40,50}
set6={60,70,80,90,10}
common=set5.intersection(set6)
if common:
    print("Common elements found:", common)
else:
    print("No common elements.")


# 4.write a python program to remove items from set7 that are not common to both set7 and set8
#set7={10,20,30,40,50}
#set8={30,40,50,60,70}


set7={10,20,30,40,50}
set8={30,40,50,60,70}
set7=set7.intersection(set8)
print(set7)
