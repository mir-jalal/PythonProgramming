prime = 1000000*[True]

for i in range(2, 1000):
    for j in range(2, 1000):
        prime[i*j] = False;

sum = 0

k = int(input(k))

for i in range(2, 1000000):
    if prime[i]:
        sum = sum + i
        if sum % k == 0:
            break

print(sum)
