# SOAL 1 - Menghitung rata-rata
# Tuliskan program untuk Soal 1 di bawah ini
print("SOAL 1 :")
def find_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg

print("The average is", find_average([18,25,3,41,5]))
print("========================")
print("\n")



# SOAL 2 - Menulis kelipatan bilangan
# Tuliskan program untuk Soal 2 di bawah ini
print("SOAL 2:")
num=eval(input("enter a number : "))
factors=[]
for i in range(1,num+1):
    if num%i==0:
       factors.append(i)

print ("Factors of {} = {}".format(num,factors))
print("========================")
print("\n")

print("    INTERMEZO")
def pattern(n):
    k = 2 * n - 2
    x = 0
    for i in range(0, n):
        x += 1
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print(x, end=" ")
        print("\r")
    k = n - 2
    x = n + 2
    for i in range(n, -1, -1):
        x -= 1
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print(x, end=" ")
        print("\r")
 
pattern(5)
