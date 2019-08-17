numbersfile = open('numbers.txt', 'w')

numbers = [1, 2, 3]

for number in numbers:
    numbersfile.write(str(number) + '\n')
    #since the write method only accept string you need to convert the int ino strings

numbersfile.close()
