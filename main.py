import math

inputs_number=int(input("How many numbers do you want to enter for the diagnosis?"))
numbers=[]
for i in range(inputs_number) :
    number=int(input("[INPUT] Enter your numbers one by one :"))
    if number==0 or number==1:
        print("[ERROR] 0 and 1 are neither prime nor not prime.")
    else :
        numbers.append(number)


for x in numbers:
    y=int(math.sqrt(x))
    while y>1:
        if x%y==0:
            print(f"[INFO] The number {x} is not prime.")
            break
        y-=1

    if y==1:
        print(f"[INFO] The number {x} is prime.")
