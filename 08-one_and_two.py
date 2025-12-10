from sys import stdin
import math

uf=[]
ufs=[]

def find(x):
    if x == uf[x]:
        return x
    else:
        uf[x] = find(uf[x])
        return uf[x]

def union(x,y):
    if ufs[find(y)] < ufs[find(x)]:
        x,y=y,x

    s=ufs[find(x)]+ufs[find(y)]
    ufs[find(x)]=s
    ufs[find(y)]=0
    uf[find(y)]=find(x)


def distance(x,y):
    return sum([(x[i] - y[i])**2 for i in range(len(x))])**(1/2)




points = []
for line in stdin:
    line=line.replace('\n','')
    if line == "":
        break
    coords_str = line.split(',')
    coords = [int(x) for x in coords_str]
    points.append(coords)
    print(coords)




distances=[]
for i, p0 in enumerate(points):
    for j, p1 in enumerate(points[i+1:], start=i+1):
        d=distance(p0,p1)
        distances.append((d,i,j))

print(distances)
distances.sort()
print(distances)

uf = [i for i in range(len(points))]
ufs = [1 for i in range(len(points))]

MAX_CONNECTIONS=1000
if len(points) < 500:
    MAX_CONNECTIONS=10


connections=0
new_connections=0
for l in distances:
    if connections == MAX_CONNECTIONS:
        # Answer to Part One
        s=sorted(ufs,reverse=True)
        print(s)
        print(s[:3])
        part_one_answer = math.prod(s[:3])
        print(part_one_answer)

    connections+=1
    d=l[0]
    i=l[1]
    p0=points[i]
    j=l[2]
    p1=points[j]
    print(f"Connection number {connections}, unique {new_connections} - ", end='')
    print(f"({i},{j}) = ({p0},{p1}): {d:.2f}, ", end='')
    if find(i) != find(j):
        #if ufs[find(i)]==1 or ufs[find(j)]==1:
        #    connections+=1
        #    pass
        print(f"Joining {find(i)} and {find(j)}")
        union(i,j)
        new_connections+=1
        if new_connections==1000-1:
            print("One Circuit To Rule Them All achieved")
            part_two_answer = p0[0]*p1[0]

            print(f"Answer to Part One: {part_one_answer}")
            print(f"Answer to Part Two: {part_two_answer}")
            break
        #print(sorted(ufs,reverse=True))
    else:
        print(f"Already joined ({find(i)})")





