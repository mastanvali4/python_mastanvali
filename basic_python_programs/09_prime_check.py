n=int(input("Enter number: "))
flag=True
for i in range(2,int(n**0.5)+1):
    if n%i==0: flag=False; break
print("Prime" if flag else "Not Prime")