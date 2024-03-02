smallest_so_far = 1 
print('Before', smallest_so_far)
for the_num in [9, 41, 12, 3, 83, 14]:
    if the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)
print('After', smallest_so_far)