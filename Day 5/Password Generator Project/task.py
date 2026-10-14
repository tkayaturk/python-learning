import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password_1 = ""
for tekrar in range(nr_letters):
    password_1 += random.choice(letters)

password_2 = ""
for tekrar in range(nr_symbols):
    password_2 += random.choice(symbols)

password_3 = ""
for tekrar in range(nr_numbers):
    password_3 += random.choice(numbers)


total_password =[]
total_password.extend(password_1)
total_password.extend(password_2)
total_password.extend(password_3)

random.shuffle(total_password)

final_password = "".join(total_password)
print(f"Your password is {final_password}")

