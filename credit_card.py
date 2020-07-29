def valid_input(number):
    '''(str) -> bool

    Returns True, if the string is 13-16 char long and has only num. values.
    '''

    if 12 < len(number) < 17:
        for char in number:
            if char not in '0123456789':
                return False
                break
        return True

    else:
        return False
    
# User input
number = input("Enter credit/debit card number: ")

while not valid_input(number):
    print("Numerical values only, lenght 13 - 16 digits accepted.")
    number = input("Enter credit/debit card number: ")

number_list = []
for char in number:
    number_list.append(int(char))

# Luhn's algorithm
double = []
for i in range(-2, -(len(number_list) + 1), -2):
    double.append(number_list[i] * 2)

sum_even = 0
for j in range(len(double)):
    sum_even = sum_even + double[j] // 10 + double[j] % 10

sum_odd = 0
for k in range(-1, -(len(number_list) + 1), -2):
    sum_odd = sum_odd + number_list[k]

# Output
if (sum_even + sum_odd) % 10 != 0:
    print("Invalid card number!")

elif number_list[0] == 4:
    print("VISA")

elif number_list[0] == 3 and (number_list[1] == 4 or number_list[1] == 7):
    print("American Express")

elif number_list[0] == 5 and (number_list[1] in range(1, 6)):
    print("MASTERCARD")

else:
    print("Card type unknown")
    


