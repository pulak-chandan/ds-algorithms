#DSA-Tryout
import random
def find_it(num,element_list):
    #Remove pass and write the logic to search num in element_list using binary search algorithm
    #Return the total number of guesses made
    element_list.sort()
    guess=0
    low=0
    high=len(element_list)-1
    while(low<=high):
        guess+=1
        mid=low+((high-low)//2)
        if element_list[mid]==num:
            print(low,high,mid)
            return mid
        elif element_list[mid]>num:
            high=mid-1
        else:
            low=mid+1
    print("Element not found !!")
    return guess    

#Initializes a list with values 1 to n in ascending order and returns it
def initialize_list_of_elements(n):
    list_of_elements=[]
    for i in range(1, n+1):
        list_of_elements.append(i)
    return list_of_elements

def play(n):
    # Step 1: Invoke initialize_list_of_elements() by passing n
    # Step 2: Generate a random number from the list of elements. The number should be between 1 and n (both inclusive)
    # Step 3: Invoke find_it() by passing the number generated at Step 2 and list generated at Step 1 and display the return value
    # Remove pass and write the code to implement the above three steps.
    element_list=initialize_list_of_elements(n)
    num=90
    print(find_it(num,element_list))

#Pass different values to play() and observe the output
play(100)
