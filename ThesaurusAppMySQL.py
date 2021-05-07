# Thesaurus application to find the meaning of the word.
# It takes input from the user and return the meaning of the word
# and find the closest meaning of the word if the word does not exist in the database.
# Using offline database: MySQL database (cloud database from Ardit700_student db)

import mysql.connector
from difflib import get_close_matches

# Create connection to MySQL database with credentials
conn = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"    
)

# translate the word
def translate(keyword):
    # Create query to db
    cursor = conn.cursor()

    # Create similiar words as the keyword
    query = cursor.execute(f"SELECT * FROM Dictionary WHERE Expression LIKE '{keyword[0]}%'")
    search_words = cursor.fetchall()

    if search_words:
        similar_words = []
        for word in search_words:
            similar_words.append(word[0])

        if keyword in similar_words:
            query = cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{keyword}'")
            meanings = cursor.fetchall()
            return meanings
        elif keyword.title() in similar_words:
            query = cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{keyword.title()}'")
            meanings = cursor.fetchall()
            return meanings
        elif keyword.upper() in similar_words:
            query = cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{keyword.upper()}'")
            meanings = cursor.fetchall()
            return meanings        
        else:
            # check the closest word with the keyword
            closest_word = get_close_matches(keyword, similar_words)
            if len(closest_word) != 0:
                ans = input(f'Did you mean {closest_word[0]} instead? Press Y if yes or press N if no: ')
                if ans.upper() == 'Y':
                    query = cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{closest_word[0]}'")
                    meanings = cursor.fetchall()
                    return meanings  
                elif ans.upper() == 'N':    
                    return 'The word does not exist, please double check again.'
                else:
                    return 'Sorry, you enter the wrong input.'    
            else:    
                    return 'The word does not exist, please double check again.'       


# Ask user input
user_input = input("Enter the word:")

# Display the meaning(s)
translation = translate(user_input)
if isinstance(translation, list) and len(translation) > 1:
    for i in range(0,len(translation)):
        print(f'{i+1}.{translation[i][1]}')
elif isinstance(translation, list) and len(translation) == 1:
    print(translation[0][1]) 
else:
    print(translation)



