print("The prime numbers from 1 to 50 are:")
for num in range(2,51):
    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print(num)