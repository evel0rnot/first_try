zork = 0
counting = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    counting = counting + 1
    print( counting, zork, thing )
print('Average', zork/counting)