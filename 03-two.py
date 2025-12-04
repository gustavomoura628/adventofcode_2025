from sys import stdin

s=0
for line in stdin:
    line=line.replace('\n','')
    if line == "":
        break

    print(f"Checking {line}: ")

    max_digits = [0,0,0,0,0,0,0,0,0,0,0,0]
    print(f"Max digits = {max_digits}")
    for i in range(len(line)):
        digit=int(line[i])
        print(f"Digit {digit}")
        for j in range(12):
            if i+(12-j-1) < len(line) and digit > max_digits[j]:
                print(f"Swapped {max_digits[j]} for {digit}")
                max_digits[j]=digit
                for k in range(j+1,12):
                    max_digits[k]=0
                break
        print(f"Max digits = {max_digits}")

    jolts=0
    for i in range(12):
        jolts*=10
        jolts+=max_digits[i]

    s+=jolts
    print(jolts)

print("Total jolts = ", s)
