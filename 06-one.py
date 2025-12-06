from sys import stdin
import re
number_lines=4
numbers_string=[]
operators=[]


def preprocess_line(line):
    line=line.replace('\n','')
    #print(f"line before: {line}")
    line=re.sub(" +"," ", line) # deduplicate spaces
    line=re.sub("^ ","", line) # remove prefix space
    line=re.sub(" $","", line) # remove postfix space
    #print(f"line after: {line}")
    return line

def perform_calculation(string_matrix, operators):
    output_array=[]
    for j in range(len(operators)):
        if operators[j]=='+':
            output=0
            for i in range(len(string_matrix)):
                output+=int(string_matrix[i][j])
            output_array.append(output)
        elif operators[j]=='*':
            output=1
            for i in range(len(string_matrix)):
                output*=int(string_matrix[i][j])
            output_array.append(output)
    return output_array



for i, line in enumerate(stdin):
    line = preprocess_line(line)
    if line == "":
        break
    if i < number_lines:
        numbers_string.append(line.split(" "))
    else:
        operators=line.split(" ")
        output = perform_calculation(numbers_string, operators)

        s=0
        for value in output:
            s+=value

        print(numbers_string)
        print(operators)
        print(output)
        print(f"sum={s}")
        print

        exit(1)
