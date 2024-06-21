import random
import string

def gererate_password(min_length,number=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
     characters += digits
    if special_chatacters:
      characters += special


    pwd =""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
     new_char = random.choice(characters)
     pwd += new_char


    if new_char in digits:
        has_number = True
    elif new_char in special:
        has_special = True


    meets_criteria = True
    if numbers:
        meets_criteria =has_number
    if spical_charaters:
        meets_criteria =meets_criteria and has_special  
 
 
    return pwd



min_length = input("Enter the minimum lenghth: ")
has_number = input("Do you want to have number (y/n)? ").lower()== "y"
has_speical =input("Do you want to have number (y/n)? ").lower()== "y"
pwd = generate_password(min_length,has_number, has_speical)
print("The generated password is:",pwd)








gererate_password(10)    

