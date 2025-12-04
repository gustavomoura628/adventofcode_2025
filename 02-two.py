import math
def get_n_digits(x):
    return math.floor(math.log10(x))+1

def get_nth_chunk(x,width,n):
    n_digits=get_n_digits(x)
    if(n_digits<width*n):
        print(f"ERROR: invalid chunk {n}th chunk of {x} with width {width}")
        exit(1)
    return x//(10**(n_digits-(n*width)))%(10**width)


def check_repeating(x,width):
    n_digits=get_n_digits(x)
    if n_digits%width != 0:
        return False
    chunks=n_digits//width
    first_chunk=get_nth_chunk(x,width,1)
    for i in range(2,chunks+1):
        if first_chunk!=get_nth_chunk(x,width,i):
            return False

    return True

s=input()
total_sum=0
for interval in s.split(","):
    print("interval:",interval)
    first_str, second_str = interval.split("-")

    infimum=int(first_str)
    supremum=int(second_str)

    for x in range(infimum,supremum+1):
        for width in range(1,get_n_digits(x)//2+1):
            if check_repeating(x,width):
                invalid_id = x
                total_sum+=invalid_id
                print(invalid_id)
                break

print("Total Sum =",total_sum)
