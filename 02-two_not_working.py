import math
def get_n_digits(x):
    return math.floor(math.log10(x))+1

def get_nth_chunk(x,width,n):
    n_digits=get_n_digits(x)
    if(n_digits<width*n):
        print("ERROR: invalid chunk")
        exit(1)
    return x//(10**(n_digits-(n*width)))%(10**width)

def get_lower_bound(x,width):
    n_digits=get_n_digits(x)
    if n_digits % width == 0:
        first_chunk = get_nth_chunk(x,width, 1)
        for i in range(2, n_digits//width+1):
            if first_chunk > get_nth_chunk(x,width,i):
                return first_chunk
            elif first_chunk < get_nth_chunk(x,width,i):
                return first_chunk+1
        return first_chunk
    else:
        return 10**width

def get_upper_bound(x,width):
    n_digits=get_n_digits(x)
    if n_digits % width == 0:

        first_chunk = get_nth_chunk(x,width, 1)
        for i in range(2, n_digits//width+1):
            if first_chunk < get_nth_chunk(x,width,i):
                return first_chunk
            elif first_chunk > get_nth_chunk(x,width,i):
                return first_chunk-1
        return first_chunk
    else:
        return 10**width-1

def plicate_digits(x,n):
    s=0
    for i in range(n):
        s*=(10**get_n_digits(x))
        s+=x
    return s

s=input()
total_sum=0
for interval in s.split(","):
    print("interval:",interval)
    first_str, second_str = interval.split("-")

    infimum=int(first_str)
    supremum=int(second_str)

    for width in range(1, get_n_digits(supremum)//2+1):
        start=get_lower_bound(infimum,width)
        stop=get_upper_bound(supremum,width)
        print(f"Width {width}, start {start}, stop {stop}")


        for i in range(start,stop+1):
            invalid_id = plicate_digits(i,2)
            total_sum+=invalid_id
            print(invalid_id)

print("Total Sum =",total_sum)
