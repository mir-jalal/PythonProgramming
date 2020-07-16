prime = 1000000*[False]

for i in range(2, 1000):
    for j in range(2, 1000):
        prime[i*j] = True;

sum = 0

k = int(input(k))

for i in range(2, 1000000):
    if not prime[i]:
        sum = sum + i
        if sum % k == 0:
            break

print(sum)
