nest_list = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
sorted_data = sorted(nest_list, key=lambda x: x[1])
print(sorted_data)
char_str = []
for x,y in enumerate(sorted_data):
    second_lowest = sorted_data[1][1]
    print(second_lowest)
    if sorted_data[x][1] == second_lowest:
        char_str.append(sorted_data[x][0])
        print(char_str)
    else:
        print('No match')
print(sorted(char_str))

        
    