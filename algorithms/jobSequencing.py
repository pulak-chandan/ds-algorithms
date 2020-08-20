n = 7
profits = [35, 30, 25, 20, 15, 12, 5]
deadlines = [3, 4, 4, 2, 3, 1, 2]
num_slots = max(deadlines)
job_arr = [None] * num_slots
profit = 0
count = 0
for i in range(len(profits)):
    if count == num_slots:
        break
    for j in range(deadlines[i] - 1, -1, -1):
        if job_arr[j] is None:
            job_arr[j] = 'J' + str(i + 1)
            profit += profits[i]
            count += 1
            break
print("Total profit:", profit)
print("Jobs selected:", job_arr)
