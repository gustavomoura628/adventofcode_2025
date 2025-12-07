from sys import stdin
import copy
prev_line = None
timeline_counter=0
def convert_to_numbers(char):
    if char == '.':
        return 0
    elif char == 'S':
        return 1
    else:
        return -1

def is_splitter(x):
    return x == -1

for line in stdin:
    line=line.replace('\n','')
    if line == "":
        break
    line=list(line)
    line = [convert_to_numbers(c) for c in line]
    print("prev: ",line)
    if prev_line != None:
        for i in range(len(line)):
            if is_splitter(prev_line[i]):
                continue
            if is_splitter(line[i]):
                if i-1>=0:
                    if not is_splitter(line[i-1]):
                        line[i-1] += prev_line[i]

                if i+1<len(line):
                    if not is_splitter(line[i+1]):
                        line[i+1] += prev_line[i]



            else:
                line[i] += prev_line[i]
    print("aftr: ",line)
    prev_line = copy.deepcopy(line)

s=0
for val in prev_line:
    s+=val

print(f"In total, the particle ends up on {s} different timelines.")
