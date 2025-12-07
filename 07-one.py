from sys import stdin
import copy
prev_line = None
split_counter = 0
for line in stdin:
    line=line.replace('\n','').replace('S','|')
    if line == "":
        break
    line=list(line)
    #print(line)
    if prev_line != None:
        for i in range(len(line)):
            if prev_line[i] == '|':
                if line[i] != '^':
                    line[i] = '|'
                else:
                    split=False
                    if i-1>=0:
                        if line[i-1] != '^':
                            split=True
                            line[i-1] = '|'

                    if i+1<len(line):
                        if line[i+1] != '^':
                            split=True
                            line[i+1] = '|'
                    if split:
                        split_counter+=1

    print("".join(line))
    prev_line = copy.deepcopy(line)

print(f"Split {split_counter} times.")
