def insertion_sort(num_list):
    for i in range(1,len(num_list)):
        temp=num_list[i]
        j=i-1
        while(num_list[j]>temp and j>=0):
            num_list[j+1]=num_list[j]
            j-=1
        num_list[j+1]=temp
    return num_list
        
num_list=[34, 67, 8, 19, 2, 23, 1, 91]
print(insertion_sort(num_list))
        
            
            
        