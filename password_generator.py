import random
# Создаем список с английскими символами
english_characters = [chr(i) for i in range(65, 91)] + \
    [chr(i) for i in range(97, 123)]
# Создаем список со специальными символами
special_characters = [chr(i) for i in range(33, 48)] + [chr(i) for i in range(
    58, 65)] + [chr(i) for i in range(91, 97)] + [chr(i) for i in range(123, 127)]
# Создаем список с цифрами
digits = [str(i) for i in range(10)]

length = int(input("How many letters would you like in your password "))
simvols = int(input("How many simvols would you like in your password "))
nums = int(input("How many nums would you like in your password "))

letter = ''
let = length - simvols - nums

while (simvols != 0):
    letter += random.choice(special_characters)
    simvols -= 1

while (let != 0):
    letter += random.choice(english_characters)
    let -= 1

while (nums != 0):
    letter += random.choice(digits)
    nums -= 1

letter_list = list(letter)
random.shuffle(letter_list)
shuffled_letter = ''.join(letter_list)

print(shuffled_letter)
