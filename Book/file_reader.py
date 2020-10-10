filename = "pi_million_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_srting = ""
for line in lines:
    pi_srting += line.strip()

birthday = input("Введите дату своего дня рождения, в формате ддммгг: ")
if birthday in pi_srting:
    print("yes")
else:
    print("no")