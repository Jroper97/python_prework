#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
#The first line of the code has been defined as below.

def hello_user(user_name):
    print("hello_" + user_name.title())
user_name = input('Enter Username: ')

hello_user(user_name)

#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for value in range(1,101,2):
        print(value)

first_odds()

#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.

def max_num_in_list(a_list):
    maximum = a_list[0]
    for value in range(len(a_list)):
        if a_list[value] > maximum:
            maximum = a_list[value]
    return maximum
    
a_list = [2, 7, 67, 72, 83]
print(max_num_in_list(a_list))


#Question 4
#Write a function to return if the given year is a leap year.
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
    #Checking if the year is divisble by 4
    if a_year % 4 == 0:
        return True
    #Checking if the year is divisble by 100
    elif a_year % 100 == 0:
        return False
    #Checking if the year is divible by 400
    elif a_year % 400 ==0:
        return True
    else:
        return False
    
a_year = int(input('Enter a year to see if it is a leap year: '))
print(is_leap_year(a_year))    


#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list) + 1))
#Driver Code
a_list = [2,3,4,5,6,7]
print(is_consecutive(a_list))

a_list = [1,2,4,5]
print(is_consecutive(a_list))