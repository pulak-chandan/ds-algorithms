def merge_sort(num_list):
    # Remove pass and write the logic here to return the sorted list
    print('Splitting',num_list)
    #terminating condition
    if len(num_list)<=1:
        return num_list
    else:
        mid=len(num_list)//2 
        left_list=num_list[:mid]
        right_list=num_list[mid:]
        #recursion
        left_sort_list=merge_sort(left_list)
        right_sort_list=merge_sort(right_list)
        sort_list=merge(left_sort_list,right_sort_list)
        return sort_list

def merge(left_list,right_list):
    # Remove pass and write the logic to merge the elements in the left_list and right_list and return the sorted list
    sorted_list=[]
    i=0
    j=0
    while i <len(left_list) and j <len(right_list):
            if left_list[i]<right_list[j]:
                sorted_list.append(left_list[i])
                i+=1
            else:
                sorted_list.append(right_list[j])
                j+=1
    if i < (len(left_list)):
        while i !=(len(left_list)):
            sorted_list.append(left_list[i])
            i+=1 
    if j < (len(right_list)):
        while j !=(len(right_list)):
            sorted_list.append(right_list[j])
            j+=1
    print("Merging:",sorted_list)
    return sorted_list
            

num_list=[34, 67, 8, 19, 2, 23, 1, 91]
print("Before sorting:",num_list)
sorted_list = merge_sort(num_list)
print("After sorting:",sorted_list)
                 