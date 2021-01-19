
def swap(num_list, first_index, second_index):
    #Remove pass and copy the code written earlier for this function
    temp=num_list[first_index]
    num_list[first_index]=num_list[second_index]
    num_list[second_index]=temp


def find_next_min(num_list,start_index):
    #Remove pass and copy the code written earlier for this function
    min_ind=start_index
    for i in range(start_index,len(num_list)):
        if num_list[i]<num_list[min_ind]:
            min_ind=i
    return min_ind

def selection_sort(num_list):
    #Remove pass and implement the selection sort algorithm to sort the elements of num_list in ascending order
    for i in range(0,len(num_list)-1):
        min_index=find_next_min(num_list,i)
        swap(num_list,i,min_index)


#Pass different values to the function and test your program
num_list=[8,2,19,34,23, 67, 91]
print("Before sorting;",num_list)
selection_sort(num_list)
print("After sorting:",num_list)