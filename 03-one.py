from sys import stdin

s=0
for line in stdin:
    line=line.replace('\n','')
    if line == "":
        break

    ones_digit=0
    tens_digit=0
    for i in range(len(line)):
        digit=int(line[i])
        if i+1 < len(line) and digit > tens_digit:
            tens_digit=digit
            ones_digit=0
        elif digit > ones_digit:
            ones_digit=digit

    jolts=tens_digit*10+ones_digit
    s+=jolts
    print(jolts)

print("Total jolts = ", s)
