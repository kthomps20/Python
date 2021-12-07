import numpy as np

# Create a numpy array

my_list = [1, 2, 3, 4, 5, 6]
my_array = np.array(my_list)

print(my_list)
print(my_array)

# Create an array from CSV import
test_2 = np.genfromtxt(r'C:\DEV\Python\Python3_Basics\Numpy\Numpy_book.csv', delimiter=',')
print(test_2)

#Element wise operation allows you to perform addition to each element in array
l = [1,2,3,4,5]
l_plus_3 = []
for i in range(len(l)):
    l_plus_3.append(l[i] + 3)

print("List: addition of 3" + str(l_plus_3))

new_l = np.array(l) + 3
print("Using a numpy array:" + str (new_l))


#Operations with numpy, can add/substract multiple arrays
test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])
test_3_fixed = test_3 + 2

total_grade = test_1 + test_2 + test_3_fixed

final_grade = total_grade/3
print(final_grade)


# 2-D Array, often set of samples
#coin toss

coin_toss = np.array [0,1,1,1,1]
coin_toss_attempt2 = np.array([0,1,1,1,1], [0,0,1,0,0])


#Accessing 