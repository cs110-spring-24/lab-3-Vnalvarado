print("Options:1,2,3,4,5,6,7,8,9,10")
run = input("Enter the problem you want to run:")
run=int(run)
if run ==1: 
    print("Running Problem 1")
    for count in range (1,1001):
        print(count)
elif run ==2:
    print("Running problem 2")
    for count in range(1,1001,2):
        print(count)
elif run ==3: 
    print("Running problem 3")
    for count in range(0,1001):
        if count % 3 == 0:
            print(count)
elif run ==4: 
    print("Running problem 4")
    for count in range (1,1001):
        if count % 3==0 or count % 5 ==0: 
            print(count)
elif run ==5:
    print("Running problem 5")
    for count in range (1,1001):
        num=int(input("Enter a number greater than 200:"))
        if count % 11==0 or count % 13==0:
            print(count)
elif run==6:
    print("Running problem 6")
    for count in range (1,1001):
        string="Hello"
        for l in range (len(string)):
            print(string[l])
elif run==7:
    print("Running problem 7")
    for count in range (1,1001):
        string="Conditional"
        for l in range (0,len(string),2):
            print(string[l])
elif run==8:
    print("Running problem 8")
    import random
    dice=random.randint(1,6)
    ones=0 
    twos=0
    threes=0
    fours=0
    fives=0
    sixes=0
    for rolls in range(100):
        if dice ==1:
            ones +=1
        elif dice ==2: 
            twos +=1
        elif dice ==3:
            threes +=1
        elif dice ==4:
            fours +=1
        elif dice ==5: 
            fours +=1
        elif dice ==6: 
            fours +=1
            print(dice)
        print(f"You rolled {ones} 1s, {twos} 2s, {threes} 3s,{fours} 4s, {fives} 5s, {sixes} 6s")
elif run==9:
    print("Running problem 9")
    num=int(input("Enter a number:"))
    if num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
        if flag:
            print(num, "is not a prime number")
        else:
            print(num, "is a prime number")
elif run==10:
    print("Running problem 10")
    def print_primes():
        print("Prime numbers less than 1000:")
    for num in range(2, 1000):
        if (num):
            print(num, end=" ")

print_primes()