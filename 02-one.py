import math
def get_n_digits(x):
    return math.floor(math.log10(x))+1

def get_lower_bound(x):
    n_digits=get_n_digits(x)
    if n_digits % 2 == 0:
        first_half = x//(10**(n_digits//2))
        second_half = x%(10**(n_digits//2))
        if first_half >= second_half:
            return first_half
        else:
            return first_half+1
    else:
        return 10**(n_digits//2)

def get_upper_bound(x):
    n_digits=get_n_digits(x)
    if n_digits % 2 == 0:
        first_half = x//(10**(n_digits//2))
        second_half = x%(10**(n_digits//2))
        if first_half <= second_half:
            return first_half
        else:
            return first_half-1
    else:
        return 10**(n_digits//2)-1

def duplicate_digits(x):
    return x*(10**get_n_digits(x))+x



s=input()
total_sum=0
for interval in s.split(","):
    print("interval:",interval)
    first_str, second_str = interval.split("-")

    infimum=int(first_str)
    supremum=int(second_str)

    start=get_lower_bound(infimum)
    stop=get_upper_bound(supremum)


    for i in range(start,stop+1):
        invalid_id = duplicate_digits(i)
        total_sum+=invalid_id
        print(invalid_id)

print("Total Sum =",total_sum)
