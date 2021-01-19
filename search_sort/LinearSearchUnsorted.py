def find_it(num,element_list):
    #Remove pass and write the logic to search num in element_list using linear search algorithm
    #Return the total number of guesses made
    guess=0
    for i in range(0,len(element_list)):
        guess+=1
        if element_list[i]==num:
            return guess
        



#Pass different values to play() and observe the output
element_list=[3,1,65,34,9,17,2,24,5,88,56]
print(find_it(88,element_list))