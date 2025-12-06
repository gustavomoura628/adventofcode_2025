from sys import stdin
import re
number_lines=4
numbers_string=[]
operators=[]


all_lines=[]

for line in stdin:
    line = line.replace('\n','')
    if line == "":
        break
    all_lines.append(line.replace('\n',''))

values=[]
val=None
outputs=[]
for j in range(len(all_lines[0])):
    for i in range(len(all_lines)):
        char=all_lines[i][len(all_lines[0])-j-1]
        print(f"char = [{char}]")
        if char == " ":
            if val != None:
                values.append(val)
            val=None
        elif char == "+":
            if val != None:
                values.append(val)
            s=0
            for val in values:
                print(val)
                s+=val
            print("+")
            print(s)
            outputs.append(s)
            values=[]
            val=None
        elif char == "*":
            if val != None:
                values.append(val)
            s=1
            for val in values:
                print(val)
                s*=val
            print("*")
            print(s)
            outputs.append(s)
            values=[]
            val=None
        else:
            if val == None:
                val = 0
            val*=10
            val+=int(char)

    print()

s=0
for val in outputs:
    s+=val

print(f"Total sum = {s}")

#print(all_lines)
