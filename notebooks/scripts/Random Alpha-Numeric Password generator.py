import random
import string

def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    print("Random alphanumeric String is:", result_str)
    return

val = input("Enter your value: ") 


get_random_alphanumeric_string(int(val))


while True:
    choice = input("Regenerate(Y/N)")
    if(choice == 'Y'):
        value = input("Enter your value: ")
        get_random_alphanumeric_string(int(value))
    elif(choice == 'N'):
        break
    else:
        print('Wrong Input')
        continue
       
