# Thesaurus application to find the meaning of the word.
# It takes input from the user and return the meaning of the word
# and find the closest meaning of the word if the word does not exist in the database.
# Using offline database: from data.json

import json
from difflib import get_close_matches

# create collection data from json file
data = json.load(open('data.json'))

# translate the word
def translate(word):
    keywords = data.keys()
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]    
    elif word.upper() in data:
        return data[word.upper()] 
    else:
        # check the closest word with the user input
        closest_word = get_close_matches(word, keywords)
        if len(closest_word) != 0:
            ans = input(f'Did you mean {closest_word[0]} instead? Press Y if yes or press N if no: ')
            if ans.upper() == 'Y':
                return data[closest_word[0]]
            elif ans.upper() == 'N':    
                return 'The word does not exist, please double check again.'
            else:
                return 'Sorry, you enter the wrong input.'    
        else:    
                return 'The word does not exist, please double check again.'            
        
# Ask user input
user_input = input("Enter the word: ")

# Display the meaning(s)
meanings = translate(user_input)
if isinstance(meanings, list) and len(meanings) > 1:
    for i in range(0,len(meanings)):
        print(f'{i+1}.{meanings[i]}')
elif isinstance(meanings, list) and len(meanings) == 1:
    print(meanings[0]) 
else:
    print(meanings)
          