tuple_list =[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

print("List of Tuple before sorting : " + str(tuple_list))

tuplen = len(tuple_list); 
for i in range(0, tuplen):
    for j in range(0, tuplen - i - 1):
        if(tuple_list[j][-1] > tuple_list[j + 1][-1]):
            swap = tuple_list[j]
            tuple_list[j] = tuple_list[j + 1]
            tuple_list[j + 1] = swap

print("List of Tuple after sorting : " + str(tuple_list))