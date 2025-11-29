import random
num=random.randint(1,10)
guess=int(input("Guess (1-10): "))
print("Correct!" if guess==num else "Wrong! Number was "+str(num))