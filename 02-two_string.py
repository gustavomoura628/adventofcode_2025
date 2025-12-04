import math

def check_repeating(x,width):
    return x==x[:width]*(len(x)//width)

s=0
for interval in input().split(","):
    first_str, second_str = interval.split("-")

    infimum=int(first_str)
    supremum=int(second_str)

    for x in range(infimum,supremum+1):
        for width in range(1,len(str(x))//2+1):
            if check_repeating(str(x),width):
                s+=x
                print(x)
                break

print("Total Sum =",s)
