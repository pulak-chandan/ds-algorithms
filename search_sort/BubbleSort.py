
def swap(num_list, first_index, second_index):
    #Remove pass and copy the code written earlier for this function
    temp=num_list[first_index]
    num_list[first_index]=num_list[second_index]
    num_list[second_index]=temp
 
# without break the no of pass is (no of elements-1)   
def bubble_sort(num_list):
    pass_count=0
    for pass_count in range(0,len(num_list)-1):
        swapped=False
        for j in range(0,len(num_list)-1-pass_count):
            if num_list[j]>num_list[j+1]:
                swapped=True
                swap(num_list,j,j+1)
        if swapped== False:
            break
    print("No of passes:",pass_count+1)




num_list=[5,4,3,2,1,7,6]
print("In the beginning:",num_list)
print("______________________________________________")
bubble_sort(num_list)
print("______________________________________________")
print("At the end:",num_list)
