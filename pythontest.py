'''numbers = input()
newarr = list(numbers)
finalarr = list(map(int, newarr))

finalarr.sort()
finalarr.sort(reverse = True)

for i in range(len(finalarr)):
    print(finalarr[i], end='')'''
import sys

'''num = int(input())
numbers = []

for i in range(num):
    number = int(input())
    numbers.append(number)

numbers.sort()

for j in range(len(numbers)):
    print(numbers[j])'''

'''num = int(input())
fact = 1

if num == 0:
    print("1")
else:
    for i in range(num):
        fact *= i + 1
    print(fact)'''

'''import sys

for i in range(3):
    numbers = []
    num = int(input())

    for j in range(num):
        number = int(sys.stdin.readline().strip())
        numbers.append(number)

    if sum(numbers) > 0:
        print("+")
    elif sum(numbers) == 0:
        print("0")
    else:
        print("-")'''

'''n = int(input())

print(n * (n + 1) // 2)
print((n * (n + 1) // 2) ** 2)
print((n * (n + 1) // 2) ** 2)'''

'''num = int(input())
sum_tips = 0
tips = []

for i in range(num):
    tip = int(input())
    tips.append(tip)

tips.sort()
tips.sort(reverse=True)

for j in range(num):
    if tips[j] - j > 0:
        sum_tips += tips[j] - j

print(sum_tips)'''

'''str = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_list = [-1] * 26

for i in str:
    re = alphabet.find(i)
    alphabet_list[re] = str.index(i)

for i in alphabet_list:
    print(i, end=" ")'''

'''while True:

    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break;

    if (a > b and b > c) or (a > c and c > b):
        if b**2 + c**2 == a**2:
            print("right")
        else:
            print("wrong")
    elif (b > a and b > c) or (b > c and c > a):
        if a**2 + c**2 == b**2:
            print("right")
        else:
            print("wrong")
    else:
        if a**2 + b**2 == c**2:
            print("right")
        else:
            print("wrong")'''

'''n1 = int(input())
n2 = int(input())
n3 = int(input())
num = [0] * 10

re = n1 * n2 * n3
temp_str = str(re)

for i in temp_str:
    num[int(i)] += 1

for i in range(10):
    print(num[i])'''
'''import math

m, n = map(int, input().split())
primes = [True for l in range(1, n+1)]
i = 0
j = 0


for i in range(1, len(primes) + 1):
    if i == 1:
        primes[0] = False
        continue
    j = 2
    while j < i:
        if i % j == 0:
            primes[i - 1] = False
            k = 2
            while i * k <= n:
                primes[(i - 1) * k] = False
                k += 1
        j += 1

for k in range(len(primes)):
    print(primes[k], end=" ")'''

'''import math

MIN, MAX = map(int, input().split())
prime = [True for i in range(MAX + 1)]

prime[1] = False

for i in range(2, int(math.sqrt(MAX)) + 1):
    if prime[i] == True:
        j = 2
        while i * j <= MAX:
            prime[i] = False
            j += 2

for i in range(MIN - 1, MAX):
    if prime[i]:
        print(i, end=" ")'''


'''m, n = map(int, input().split())

a = [False, False] + [True]*(n-1)
primes = []

for i in range(2, n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

for i in primes:
    if m <= i <= n:
        print(i, end=" ")'''

'''import sys
queue = []
num = int(input())

for i in range(num):
    command = sys.stdin.readline().split()
    if 'pop' in command:
        if len(queue) == 0:
            print("-1")
        else:
            print(queue.pop(0))

    elif 'size' in command:
        print(len(queue))

    elif 'empty' in command:
        if len(queue) == 0:
            print("1")
        else:
            print("0")

    elif 'front' in command:
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[0])

    elif 'back' in command:
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[-1])
    else:
        queue.append(command[-1])'''

'''import sys
queue = []
num = int(input())

for i in range(num):
    command = sys.stdin.readline().split()
    if 'pop' in command:
        if len(queue) == 0:
            print("-1")
        else:
            print(queue.pop(-1))

    elif 'size' in command:
        print(len(queue))

    elif 'empty' in command:
        if len(queue) == 0:
            print("1")
        else:
            print("0")

    elif 'top' in command:
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[-1])
    else:
        queue.append(command[-1])'''

'''case = 1
while True:
    for i in range(int(input())):
        num = int(input())
    print(f"Case {case}: Sorting... done!")
    case += 1'''

'''import sys
deque = []
num = int(input())

for i in range(num):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == 'pop_front':
        if len(deque) == 0:
            print("-1")
        else:
            print(deque.pop(0))

    elif command[0] == 'pop_back':
        if len(deque) == 0:
            print("-1")
        else:
            print(deque.pop(-1))

    elif command[0] == 'push_front':
        deque.insert(0, int(command[-1]))
    elif command[0] == 'push_back':
        deque.insert(len(deque), int(command[-1]))

    elif command[0] == 'size':
        print(len(deque))

    elif command[0] == 'empty':
        if len(deque) == 0:
            print("1")
        else:
            print("0")

    elif command[0] == 'front':
        if len(deque) == 0:
            print("-1")
        else:
            print(deque[0])

    elif command[0] == 'back':
        if len(deque) == 0:
            print("-1")
        else:
            print(deque[-1])'''

'''school = input()

if school == 'NLCS':
    print("North London Collegiate School")
elif school == 'BHA':
    print("Branksome Hall Asia")
elif school == 'KIS':
    print("Korea International School")
else:
    print("St. Johnsbury Academy")'''

'''num = int(input())
stack = []

for i in range(num):
    numbers = int(input())
    if numbers == 0:
        stack.pop(-1)
    else:
        stack.append(numbers)

print(sum(stack))'''

'''while True:
    i = 0
    count = 0
    num = input()
    if num == '0':
        break
    else:
        for i in range(len(num) // 2):
            if num[i] == num[len(num) - i - 1]:
                continue
            else:
                print("no")
                count += 1
                break
        if count == 0:
            print("yes")

        else:
            for j in range(len(num) // 2):
                if num[j] == num[len(num) - j - 1]:
                    continue
                else:
                    print("no")
                    break
            if i == len(num) // 2 - 1:
                print("yes")'''

'''num = int(input())
score_list = [float(i) for i in input().split()]

score_list.sort()
M = score_list[-1]

for i in range(num):
    score_list[i] = score_list[i] / M * 100

print(sum(score_list) / num)'''

'''xy_list = []
num = int(input())

for i in range(num):
    x, y = map(int, input().split())
    xy_list.append((x, y))

xy_list.sort()

for i in range(num):
    print(xy_list[i][0], xy_list[i][1])'''

'''import sys
i = 0
while True:
    arr = sys.stdin.readline().rstrip().split()
    if arr[0] == '0':
        break
    i += 1
    print(f"Case {i}: Sorting... done!")'''

'''num = int(input())
opt = []
    
for i in range(num // 5 + 1):
    for j in range(num // 3 + 1):
        if i * 5 + j * 3 == num:
            opt.append(i + j)

if len(opt) == 0:
    print("-1")
else:
    print(min(opt))'''

'''import sys
dic = {}
num = int(sys.stdin.readline())

for j in range(num):
    for i in sys.stdin.readline().rstrip():
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1

new_dic = sorted(dic.items(), key=lambda x: x[0])

for i in range(len(new_dic)):
    for j in range(new_dic[i][1]):
        print(new_dic[i][0])'''


'''num = input()

if '7' not in num and int(num) % 7 != 0:
    print("0")
elif '7' not in num and int(num) % 7 == 0:
    print("1")
elif '7' in num and int(num) % 7 != 0:
    print("2")
elif '7' in num and int(num) % 7 == 0:
    print("3")'''

'''import sys
num = int(input())
sum = 0
j = 0

str = sys.stdin.readline().rstrip()

for i in str:
    sum += (ord(i) - 96) * 31**j
    j += 1

print(sum % 1234567891)'''
'''import sys

count = 0
n, k = map(int, sys.stdin.readline().rstrip().split())
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

print(fact(n) // (fact(k) * fact(n - k)))'''

'''num = int(input())
str = sys.stdin.readline().rstrip()
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

for i in str:
    if i in vowels:
        count += 1

print(count)'''

'''n = input()
num = list(n)
sum_ = 0
count = 0

if len(num) == 1:
    sum_ = int(n)
    count = -1
else:
    while True:
        for i in range(len(num)):
            sum_ += int(num[i])
        if sum_ < 10:
            break
        else:
            num = list(str(sum_))
            sum_ = 0
            count += 1

if sum_ % 3 != 0:
    print(count + 1)
    print("NO")
else:
    print(count + 1)
    print("YES")'''

'''N = int(input())
count = 0
if N == 2:
    print("NO")
else:
    for i in range(1, N+1):
        if i % 2 == 0 and (N - i) % 2 == 0:
            count = 1
            break
        else:
            count = 0
    if count == 0:
        print("NO")
    else:
        print("YES")'''

'''a, b = map(int, input().split())

if (a == 0 and b == 5) or (a == 5 and b == 2) or (a == 2 and b == 0):
    print("<")
elif (a == 5 and b == 0) or (a == 2 and b == 5) or (a == 0 and b == 2):
    print(">")
elif a == b:
    print("=")
elif (a == 1 or a == 3 or a == 4) and (b == 0 or b == 2 or b == 5):
    print("<")
elif (b == 1 or b == 3 or b == 4) and (a == 0 or a == 2 or a == 5):
    print(">")
else:
    print("=")'''

'''num = int(input())
numbers = input()
odd = 0
even = 0

for i in range(num):
    if int(numbers[i]) % 2 == 0:
        even += 1
    else:
        odd += 1

if odd > even:
    print("1")
elif odd < even:
    print("0")
else:
    print("-1")'''

'''num = int(input())

for i in range(num):
    a, b = map(int, input().split())
    if b > 2:
        if b % 2 == 0 and (a + b * 4) > b // 2 * 15:
            print((b // 2) + ((a + b * 4) - b // 2 * 15) // 15 + 1)
        elif b % 2 == 0:
            print(b // 2)
        elif b % 2 != 0 and (a + b * 4) > (b // 2 + 1) * 15:
            print(b // 2 + 1 + ((a + b * 4) - (b // 2 + 1) * 15) // 15 + 1)
        elif b % 2 != 0:
            print(b // 2 + 1)

    elif a == 0 and b == 0:
        print("0")
    elif (a + b * 4) // 15 == 0:
        print("1")
    elif (a + b * 4) % 15 == 0:
        print((a + b * 4) // 15)
    elif (a + b * 4) % 15 != 0:
        print((a + b * 4) // 15 + 1)'''

'''num = int(input())

if num == 1:
    print("12 1600")
elif num == 2:
    print("11 894")
elif num == 3:
    print("11 1327")
elif num == 4:
    print("10 1311")
elif num == 5:
    print("9 1004")
elif num == 6:
    print("9 1178")
elif num == 7:
    print("9 1357")
elif num == 8:
    print("8 837")
elif num == 9:
    print("7 1055")
elif num == 10:
    print("6 556")
else:
    print("6 773")'''

'''st = "WelcomeToSMUPC"
num = int(input())

if num <= 14:
    print(st[num - 1])
else:
    print(st[num%14 - 1])'''

'''num = int(input())

V = num // 5
I = num % 5

for i in range(V):
    print("V", end='')
for i in range(I):
    print("I", end='')'''

'''import sys
str = list(sys.stdin.readline().rstrip())
i = 1
if len(str) % 3 != 0:
    while True:
        if (len(str) + i) % 3 == 0:
            break
        i += 1

    for j in range(i):
        str.insert(0, '0')

str.reverse()
n = 0
temp_sum = 0
oct = []

for i in str:
    temp_sum += pow(2, n) * int(i)
    n += 1
    if n == 3:
        oct.insert(0, temp_sum)
        temp_sum = 0
        n = 0

for i in oct:
    print(i, end='')'''

'''word = input()
word = word.upper()
words = {}
count = 0

for i in word:
    if i not in words:
        words[i] = 1
    else:
        words[i] += 1

new_list = [i for i in words.values()]

for i in new_list:
    if max(new_list) == i:
        count += 1

if count == 1:
    for i in words.keys():
        if words[i] == max(new_list):
            print(i)
else:
    print("?")'''

'''N, A, B = map(int, input().split())
A_i = [int(i) for i in input().split()]
B_i = [int(i) for i in input().split()]
temp = []
i = 0
k = 0
count = 0

if N != 1:
    for i, j in zip(A_i, B_i):
        for k in range(0, 10000):
            if i + A*k == j + B*k:
                temp.append(k)
                break
        if k == 9999:
            print("NO")
            count = 1
            break

    if count != 1:
        print("YES")
        for i in temp:
            print(i, end=' ')

else:
    if A_i == B_i:
        print("YES")
        print("0")
    else:
        for i, j in zip(A_i, B_i):
            for k in range(0, 10000):
                if i + A * k == j + B * k:
                    temp.append(k)
                    break
            if k == 9999:
                print("NO")
                count = 1
        if count != 1:
            print("YES")'''

'''arr = [int(i) for i in input().split()]
count = 0
for i in arr:
    if i == 9:
        count += 1

if count >= 1:
    print("F")
else:
    print("S")'''


'''def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


num = int(input())
for i in range(num):
    r, n = map(int, input().split())
    print(factorial(n) // (factorial(n - r) * factorial(r)))'''

'''11365번'''
'''while True:
    password = input()
    if password == "END":
        break
    for i in range(-1, -len(password) - 1, -1):
        print(password[i], end="")
    print()'''

'''def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


num = int(input())
fact = str(factorial(num))
i = 0

if fact[-1] == '0':
    for i in range(2, num+1):
        if fact[-i] != '0':
            break
    print(i - 1)
else:
    print("0")'''

'''a, b, c = map(int, input().split())
num = [a, b, c]

min_num = min(num)
max_num = max(num)

num.remove(min_num)
num.remove(max_num)

print(min_num,num[0],max_num)'''

'''1735'''

'''def Euclidean(a, b):
    while b != 0:
        [a, b] = [b, a % b]
    return a


n1, n2 = map(int, input().split())
n3, n4 = map(int, input().split())

re1 = n4*n1 + n2*n3
re2 = n2*n4

print((n4*n1 + n2*n3) // Euclidean(re1, re2), n2*n4 // Euclidean(re1, re2))'''
'''2754번'''
'''import sys
str = sys.stdin.readline().rstrip()

if str[0] == 'A':
    if str[-1] == '+':
        print("4.3")
    elif str[-1] == '0':
        print("4.0")
    elif str[-1] == '-':
        print("3.7")
elif str[0] == 'B':
    if str[-1] == '+':
        print("3.3")
    elif str[-1] == '0':
        print("3.0")
    elif str[-1] == '-':
        print("2.7")
elif str[0] == 'C':
    if str[-1] == '+':
        print("2.3")
    elif str[-1] == '0':
        print("2.0")
    elif str[-1] == '-':
        print("1.7")
elif str[0] == 'D':
    if str[-1] == '+':
        print("1.3")
    elif str[-1] == '0':
        print("1.0")
    elif str[-1] == '-':
        print("0.7")
else:
    print("0.0")'''

'''def GCD(a, b):
    while b != 0:
        [a, b] = [b, a % b]
    return a


num = int(input())
for i in range(num):
    a, b = map(int, input().split())
    print(GCD(a, b) * (a // GCD(a, b)) * (b // GCD(a, b)))'''

'''7595번'''
'''def triangles(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("*", end='')
        print()


while True:
    n = int(input())
    if n == 0:
        break
    triangles(n)'''

'''l1 = [0, 1, 4, 5]
l2 = [0, 1, 2, 3]
l3 = [0, 2, 4, 6]
l4 = [1, 3, 5, 7]
l5 = [2, 3, 6, 7]
l6 = [4, 5, 6, 7]

num = int(input())
for i in range(num):
    l = [int(i) for i in input().split()]
    l.sort()
    if l == l1 or l == l2 or l == l3 or l == l4 or l == l5 or l == l6:
        print("YES")
    else:
        print("NO")'''

'''5524번(스트릭 유지용)(제출함)'''
'''num = int(input())

for i in range(num):
    word = input()
    print(word.lower())'''

'''5554번(스트릭 유지용)(제출함)'''
'''numlist = []

for i in range(4):
    num = int(input())
    numlist.append(num)

print(sum(numlist) // 60)
print(sum(numlist) - sum(numlist) // 60 * 60)'''

'''15727번(스트릭 유지용)(제출함)'''

'''num = int(input())
if num % 5 == 0:
    print(num // 5)
else:
    print(num // 5 + 1)'''

'''num = int(input())
for i in range(num):
    number = [int(i) for i in input().split()]
    newint = sorted(number, reverse=True)
    print(newint[2])'''

'''def pivot(n):

    if n == 1: return 1
    if n == 2: return 1

    fn1 = 1
    fn2 = 1
    fn = 0

    for i in range(n - 2):
        fn = fn1 + fn2
        fn1 = fn2
        fn2 = fn

    return fn

num = int(input())
print(pivot(num))'''

'''2747번(제출함)'''
'''def pivot(n):

    if n == 0: return 0
    if n == 1: return 1
    if n == 2: return 1

    fn1 = 1
    fn2 = 1
    fn = 0

    for i in range(n - 2):
        fn = fn1 + fn2
        fn1 = fn2
        fn2 = fn

    return fn


num = int(input())

print(pivot(num))'''

'''def prime(n):
    for i in range(2, n+1):
        if n % i == 0:
            return False
    return True'''

'''n = int(input())
a = [False, False] + [True]*(7370000 - 1)
primes = []

for i in range(2, 7370001):
    if a[i]:
        if len(primes) == n:
            break
        primes.append(i)
        for j in range(2*i, 7370001, i):
            a[j] = False

print(primes[n - 1])'''
'''2033번(제출함)'''
'''num = list(input())
num.reverse()

for i in range(len(num)):
    num[i] = int(num[i])

for i in range(len(num)):
    if i == len(num) - 1:
        break
    else:
        if int(num[i]) >= 5:
            num[i + 1] += 1
            num[i] = 0
        else:
            num[i] = 0

for i in range(len(num) - 1, -1, -1):
    print(num[i], end='')'''

'''8871번(제출함)'''
'''num = int(input())

print((num + 1) * 2, (num + 1) * 3)'''

'''1264번(제출함)'''
'''count = 0
while True:
    str = input()
    str = str.lower()

    if str == '#':
        break
    for i in range(len(str)):
        if str[i] == 'a' or str[i] == 'e' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u':
            count += 1
    print(count)
    count = 0'''

'''26575번(제출함)'''
'''num = int(input())

for i in range(num):
    d, f, p = map(float, input().split())
    total = d * f * p
    print("$%.2f" % total)'''

'''10987번(제출함)'''
'''str = input()
count = 0

for i in range(len(str)):
    if str[i] == 'a' or str[i] == 'e' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u':
        count += 1

print(count)'''

'''24736번(제출함)'''
'''T, F, S, P, C = map(int, input().split())
T1, F1, S1, P1, C1 = map(int, input().split())
print(6*T + 3*F + 2*S + 1*P + 2*C, 6*T1 + 3*F1 + 2*S1 + 1*P1 + 2*C1)'''

'''17874번(제출함)'''
'''n, h, v = map(int, input().split())

if h < n / 2:
    h = n - h
if v < n / 2:
    v = n - v

print(h * v * 4)'''

'''11557번(제출함)'''
'''import sys

num = int(sys.stdin.readline())

for i in range(num):
    dic = {}
    n = int(sys.stdin.readline())
    for j in range(n):
        uni = sys.stdin.readline().rstrip().split()
        dic[uni[0]] = int(uni[-1])
    new_dic = sorted(dic.items(), key=lambda x: x[1])
    print(new_dic[n - 1][0])'''

'''9366번(제출함)'''
'''num = int(input())

def max(a, b, c):
    max = a

    if max < b:
        max = b
    if max < c:
        max = c

    return max


n = 1

for i in range(num):
    a, b, c = map(int, input().split())
    print(max(a, b, c))
    if a == b and b == c and c == a:
        print(f"Case #{n}: equilateral")
    elif max(a, b, c) < (a + b + c) - max(a, b, c):
        if a == b or b == c or c == a:
            print(f"Case #{n}: isosceles")
        else:
            print(f"Case #{n}: scalene")
    else:
        print(f"Case #{n}: invalid!")

    n += 1'''

#10101번
'''a = int(input())
b = int(input())
c = int(input())

if a == 60 and b == 60 and c == 60:
    print("Equilateral")
elif a + b + c == 180:
    if a == b or b == c or c == a:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")'''

#10808번
'''dic = {}

for i in range(97, 123):
    dic[chr(i)] = 0

word = input()

for i in word:
    if i in dic.keys():
        dic[i] += 1

for i in dic.values():
    print(i, end=' ')'''

#15702번(제출함)
'''n, m = map(int, input().split())
p_score = [int(i) for i in input().split()]
dic = {}

for i in range(m):
    m_score = [i for i in input().split()]
    sum = 0
    for j in range(1, len(m_score)):
        if m_score[j] == 'O':
            sum += p_score[j - 1]

    dic[int(m_score[0])] = sum

new = sorted(dic.items(), key=lambda x: (x[1], -x[0]))

print(new[m - 1][0], new[m - 1][1])'''

#28927번(제출함)
'''def sum(a, b, c):
    return 3 * a + 20 * b + 120 * c

t1, e1, f1 = map(int, input().split())
t2, e2, f2 = map(int, input().split())

if sum(t1, e1, f1) < sum(t2, e2, f2):
    print("Mel")
elif sum(t1, e1, f1) == sum(t2, e2, f2):
    print("Draw")
else:
    print("Max")'''

#2748번(제출함), 10826번(제출함), 10870번(제출함)
'''def pivo(n):

    if n == 0: return 0
    if n == 1: return 1

    fn1 = 0
    fn2 = 1
    fn = 0

    for i in range(n - 1):
        fn = fn1 + fn2
        fn1 = fn2
        fn2 = fn

    return fn


num = int(input())

print(pivo(num))'''


'''num = int(input())
score = []

for i in range(num):
    c, n, s = map(int, input().split())
    score.append((c, n, s))

n = sorted(score, key=lambda score: score[2])
print(n)'''

#1834번(제출함)
'''sum = 0
N = int(input())

for i in range(1, N):
    sum += (N + 1) * i

print(sum)'''

#2711번(제출함)
'''import sys
num = int(sys.stdin.readline())

for i in range(num):
    n = sys.stdin.readline().rstrip().split()
    str = n[-1]
    print(str[:int(n[0]) - 1] + str[int(n[0]):])'''

#1312번
'''a, b, n = map(int, input().split())

temp = list(str(a / b))
result = 0
i = 10'''



'''for i in range(len(temp)):
    if temp[i] == '.':
        result = int(temp[i + n])
print(result)'''

#1181번(제출함)
'''num = int(input())
dic = {}

for i in range(num):
    word = input()
    dic[word] = len(word)

result = sorted(dic.items(), key=lambda x: (x[1], x[0]))

for i in result:
    print(i[0])'''

#17219번(제출함)
'''import sys

a, b = map(int, sys.stdin.readline().split())
dic_site_p = {}

for i in range(a):
    site_p = sys.stdin.readline().rstrip().split()
    dic_site_p[site_p[0]] = site_p[1]

print(dic_site_p)

for i in range(b):
    site = sys.stdin.readline().rstrip()
    print(dic_site_p[site])'''

#11653번(제출함)
'''n = int(input())

a = [False, False] + [True]*(n-1)
primes = []

for i in range(2, n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

for i in range(2, n+1):
    while True:
        if n % i == 0:
            n //= i
            print(i)
        else:
            break'''

#11723번(제출함)
'''import sys
R = set()

for _ in range(int(input())):
    cmd = sys.stdin.readline().rstrip().split()

    if cmd[0] == "add" and cmd[-1] not in R:
        R.add(cmd[-1])

    elif cmd[0] == "remove" and cmd[-1] in R:
        R.remove(cmd[-1])

    elif cmd[0] == "check":
        if cmd[-1] in R:
            print("1")
        else:
            print("0")

    elif cmd[0] == "toggle":
        if cmd[-1] in R:
            R.remove(cmd[-1])
        else:
            R.add(cmd[-1])

    elif cmd[0] == "all":
        R = set(str(i) for i in range(1, 21))

    elif cmd[0] == "empty":
        R = set()'''

#31403번
'''A = int(input())
B = int(input())
C = int(input())

print(A + B - C)
print(int(str(A) + str(B)) - C)'''

#1764번(제출함)
'''import sys

N, M = map(int, sys.stdin.readline().split())
people = {}
result = []

for i in range(N):
    p = sys.stdin.readline().rstrip()
    people[p] = p

for _ in range(M):
    p_name = sys.stdin.readline().rstrip()
    try:
        result.append(people[p_name])
    except KeyError:
        continue

n_result = sorted(result)
print(len(n_result))
for i in n_result:
    print(i)'''

#11047번(제출함)
'''import sys
N, M = map(int, sys.stdin.readline().split())
coin = []
sum = 0

for _ in range(N):
    coin.append(int(sys.stdin.readline()))

for i in range(len(coin) - 1, -1, -1):
    if coin[i] <= M:
        sum += M // coin[i]
        M %= coin[i]

print(sum)'''

#11399번(제출함)
'''num = int(input())
time = [int(i) for i in input().split()]
time.sort()
sum = 0

for i in range(num):
    temp = 0
    for j in range(0, i + 1):
        temp += time[j]
    sum += temp

print(sum)'''

#11659번(제출함)
'''import sys
N, M = map(int, sys.stdin.readline().split())
num = [int(i) for i in sys.stdin.readline().split()]
new_num = [0]
sum = 0

for i in range(len(num)):
    sum += num[i]
    new_num.append(sum)

for k in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(new_num[j] - new_num[i - 1])'''

#10814번(제출함)
'''import sys
input = sys.stdin.readline
p = []

for _ in range(int(input())):
    people = input().rstrip().split()
    p.append((people[0], people[-1]))

p.sort(key=lambda x: int(x[0]))

for i, j in p:
    print(i, j)'''

#17283번(제출함)
'''import math as m

L = int(input())
R = int(input())

i = 1
sum = 0

while L > 5:
    L = m.floor(L * (R / 100))
    sum += L * pow(2, i)
    i += 1
    if m.floor(L * (R / 100)) <= 5:
        break

print(sum)'''

#6996번(제출함)
'''for _ in range(int(input())):
    word1, word2 = input().split()

    w1 = sorted(word1)
    w2 = sorted(word2)

    if w1 == w2:
        print(f"{word1} & {word2} are anagrams.")
    else:
        print(f"{word1} & {word2} are NOT anagrams.")'''

#2164번(제출함)
'''import sys
from collections import deque
input = sys.stdin.readline
num = int(input())
queue = deque([i for i in range(1, num + 1)])

while len(queue) != 1:
    queue.popleft()
    queue.append(queue[0])
    queue.popleft()

print(*queue)'''

#2858번(제출함)
R, B = map(int, input().split())
sum = 0

for i in range(1, B + 1):
    if B % i == 0:
        sum = (B // i) * 2 + i * 2 + 4
        if sum == R:
            if i + 2 > B // i + 2:
                print(i + 2, B // i + 2)
                break
            else:
                print(B // i + 2, i + 2)
                break

