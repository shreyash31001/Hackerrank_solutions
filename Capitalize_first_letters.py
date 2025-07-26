a = 'chris alan'
new_str = []
for i, char in enumerate(a):
    if i == 0 or (a[i-1] == ' ' and char.isalpha()):
        new_str.append(char.upper())
    else:
        new_str.append(char)
new_str = ''.join(new_str)
print(new_str)  # Output: 'Chris Alan'

## Solution 2 
a = 'chris alan'
new_str = ' '.join(word.capitalize() for word in a.split())
print(new_str)  # Output: 'Chris Alan'

## Solution 3
a = 'chris alan'
print(a.title())  # Output: 'Chris Alan'