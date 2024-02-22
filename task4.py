arr_n = [1, 10, 2, 9]
f = round(sum(arr_n)/len(arr_n))
a = (abs(f - arr_n[0])) + (abs(f - arr_n[1])) + (abs(f - arr_n[2])) + (abs(f - arr_n[3]))
print(a)