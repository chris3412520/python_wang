
"""1.输出100到200内所有的素数。"""

for num in range(100,201):
    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    if is_prime and num!=1:
        print(num)
    else:
        continue




















"""from math import sqrt
for num in range(100,201):
    end = int(sqrt(num))
    is_prime = True
    for x in range(2, end + 1):
        if num % x == 0:
            is_prime = False
            break
    if is_prime and num != 1:
        print('%d是素数' % num)
    else:
        continue
"""






"""
def prime_100_to_200():
    for num in range(100, 201):
        if is_prime(num):
            print(num, end=" ")
    print()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# prime_100_to_200()"""