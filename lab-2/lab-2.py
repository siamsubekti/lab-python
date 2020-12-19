# DDP LAB-2

# SOAL 1 - Mencetak bilangan
# Tuliskan program untuk Soal 1 di bawah ini
print('SOAL 1')
for i in range(100, 0, -2) :
    print(i, end=', ')
print('\n')



# SOAL 2 - Menghitung rata-rata
# Tuliskan program untuk Soal 2 di bawah ini
print('SOAL 2')
amount = int(input("Enter the amount of numbers that you have: "))

numbers = []
for i in range(amount):
    new = input('Enter number {}: '.format(i+1))
    numbers.append(new)

print('list number of input ',numbers)

sum = 0.0
for i in numbers:
    sum = float(sum) + float(i)
    
    avg = float(sum) / len(numbers)
print(f'sum {sum:.6f}')
print('length numbers', len(numbers))
print(f'average is: {sum / len(numbers):.15f}')
print('\n')



# SOAL 3 - Mencetak persegi
# Tuliskan program untuk Soal 3 di bawah ini

print('SOAL 3')
n=eval(input("enter number : "))
for i in range(n):
    print('# ' * n)


