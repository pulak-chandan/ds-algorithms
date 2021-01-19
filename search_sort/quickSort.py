def quick_sort(num_list,low,high):
    print("List to part:",num_list[low:high+1])
    if len(num_list[low:high+1])<=1:
        return num_list
    
    else:
        p=partition(num_list,low,high)
        quick_sort(num_list,low,p-1)
        quick_sort(num_list,p+1,high)
        return num_list
        
def swap(num_list, first_index, second_index):
    #Remove pass and copy the code written earlier for this function
    temp=num_list[first_index]
    num_list[first_index]=num_list[second_index]
    num_list[second_index]=temp     

def partition(num_list,low,high):
    pivot=high
    i=low
    j=low
    for j in range(low,high):
        if num_list[j]<num_list[pivot]:
            swap(num_list,i,j)
            i+=1
    swap(num_list,pivot,i)
    return i
        
    
list=[102,54,26,93,17,77,31,44,55,20,100,-3]  
print(quick_sort(list,0,len(list)-1))