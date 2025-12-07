from sys import stdin
import copy

reading_intervals=True
intervals=[]

def is_inside_intervals(x):
    for interval in intervals:
        if x >= interval[0] and x <= interval[1]:
            return True
    return False

def has_overlap(interval1, interval2):
    if interval1[0] >= interval2[0] and interval1[0] <= interval2[1]:
        return True
    elif interval1[1] >= interval2[0] and interval1[1] <= interval2[1]: 
        return True
    elif interval2[0] >= interval1[0] and interval2[0] <= interval1[1]:
        return True
    elif interval2[1] >= interval1[0] and interval2[1] <= interval1[1]: 
        return True
    else:
        return False

def get_union(interval1, interval2):
    return [min(interval1[0],interval2[0]),max(interval1[1],interval2[1])]

def count_elements():
    count=0
    for pair in intervals:
        count+=pair[1]-pair[0]+1
    return count


s=0
for line in stdin:
    line=line.replace('\n','')
    if reading_intervals:
        if line != "":
            first_str, second_str = line.split("-")
            first=int(first_str)
            second=int(second_str)
            intervals.append([first,second])
        else:
            reading_intervals=False
            overlap_flag=True
            while overlap_flag:
                print(intervals)
                overlap_flag=False
                for i in range(len(intervals)):
                    for j in range(i+1, len(intervals)):
                        if has_overlap(intervals[i],intervals[j]):
                            overlap_flag=True
                            new_intervals=[]
                            new_intervals.append(get_union(intervals[i],intervals[j]))
                            for k, x in enumerate(intervals):
                                if k!=i and k!=j:
                                    new_intervals.append(x)
                            intervals = copy.deepcopy(new_intervals)
                            break
                    if overlap_flag:
                        break


    else:
        if line == "":
            break
        x=int(line)
        if(is_inside_intervals(x)):
            print(f"{x} fresh")
            s+=1
        else:
            print(f"{x} spoiled")
        pass

print(f"{s} of the available ingredient IDs are fresh.")
print(f"Total amount of fresh ingredients: {count_elements()}")
