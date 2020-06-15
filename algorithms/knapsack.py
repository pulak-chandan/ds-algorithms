# n : number of items available
n = 7
# m : maximum weight the bag can handle
m = 15
fruits_list = ['Apple','Orange','Banana','Grapes','Guava','Pineapple','Mango']
profit = [10,5,15,7,6,18,3]
weight = [2,3,5,7,1,4,1]
profit_per_kilo_to_qty_avl = [[fruits_list[i],round(profit[i]/weight[i],2),weight[i]] for i in range(n)]
print(profit_per_kilo_to_qty_avl)
profit_per_kilo_to_qty_avl_sorted = sorted(profit_per_kilo_to_qty_avl, key = lambda x: x[1], reverse = True)
print(profit_per_kilo_to_qty_avl_sorted)
profit = 0
for i in profit_per_kilo_to_qty_avl_sorted:
    if m >= i[2]:
        profit += i[1] * i[2]
    else:
        profit += i[1] * (i[2]-m)
        break
    m -=i[2]
    print(profit)
print(profit)



