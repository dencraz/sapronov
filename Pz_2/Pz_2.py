#Дано трехзначное число. Вывести число, полученное при прочтении исходного числа справа налево.
a = int(input('Введите трёхзначное число'))
if a <= 100  and a <= 999:
    print ('Введено не трёхзначное число')
else:
    print (" Введено трёхзначное число")
f = a%10*100 + a%100//10*10 + a//100
print (f)

