a = int(input("Enter your number.: "))
if  a==2 or a==3:
    print("PRIME NUMBER")

for num in range(2,a):
        if a % num ==0 :
            print(f"Entered {a}  is not prime number.")
            break
        elif a%(num-1):
            print("Entered number is prime.")
            break
        else:
            continue

