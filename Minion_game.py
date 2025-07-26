# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string .

kevin = 0
stuart = 0
word = 'BANANA'
n = len(word)
for i in range(n): 
    if word[i].lower() in ['a','e','i','o','u']:
        kevin+= n-i
        print("kevin",i)
        print("kevin's score",kevin)
    else:
        stuart+= n-i
        print("stuart",i)
        print("stuart score", stuart)
        
if stuart > kevin:
    print(f"Stuart {stuart}")
elif stuart < kevin:
    print(f"Kevin{kevin}")
else:
    print("draw")
        
            