random_numbers = [29, 68, 69, 30, 20, 91, 62, 28, 36, 67, 40, 71, 71, 82, 71, 84, 96, 34, 40, 92, 57, 56, 86, 63, 88, 79, 48, 22, 12, 74,
86, 54, 94, 19, 73, 25, 23, 72, 74, 56,53, 52, 55, 10, 37, 48, 82, 84, 57, 45, 85, 48, 58, 56, 95, 21, 47, 98, 71, 38, 24, 51, 28, 71,
52, 33, 78, 78, 77, 24,17, 31, 85, 87, 86, 63, 23, 73, 40, 64, 35, 29, 10, 43, 99, 38, 63, 61, 76, 91, 64, 48, 23, 26, 19, 21, 17, 49,
15, 62]


a = []
b = []
for number in random_numbers:
    if number %5 == 0:
        a.append(number)
    if number%3 == 0:
        b.append(number)
print(a)
print(b)

print (sum(b) + sum(a))

prime = []
prime_sum = 0
for k in random_numbers:
    count = 0
    for w in range(2,k):
        if k % w != 0:
            count += 1
            if count == k-2 :
                prime.append(k)
                prime_sum += k
print ()
print (prime)
print (prime_sum)
