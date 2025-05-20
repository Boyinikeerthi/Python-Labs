# 1.Write a python program to find the number of appears in the tuple.
#input tuplex:(2,4,5,6,2,3,4,4,7)
#output:3


tuple1=(2,4,5,6,2,3,4,4,7)
print(tuple1.count(4))


# 2.Write a python program to convert a list to a tuple.
#input:listx=(5,10,7,4,15,3)
#output:(5,10,7,4,15,3)


listx = [5,10,7,4,15,3]
tuplex = tuple(listx)
print("Tuple:", tuplex)


# 3.Write a python program to calculate the sum of the numbers in a given tuple.
#input tuples_list:[(1,2),(3,4),(5,6)]
#output:21


tuples_list = [(1, 2), (3, 4), (5, 6)]
total = 0
for tup in tuples_list:
    for num in tup:
        total += num
print("Sum of all numbers in the tuples:", total)


# 4.Write a python program and iterate the given tuples
#input:  employee1 = ("John Doe", 101, "Human Resources", 60000)
       # employee1 = ("Alice Smith", 102, "Marketing", 55000)
       # employee1 = ("Bob Johnson", 103, "Engineering", 75000)


employees = [("John Doe", 101, "Human Resources", 60000),
    ("Alice Smith", 102, "Marketing", 55000),
    ("Bob Johnson", 103, "Engineering", 75000)]  
for emp in employees:
    name, emp_id, department, salary = emp
    print(f"Name: {name}, ID: {emp_id}, Department: {department}, Salary: {salary}")


 
