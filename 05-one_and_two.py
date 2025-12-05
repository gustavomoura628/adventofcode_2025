from sys import stdin

class Node():
    def __init__(self, infimum, supremum):
        self.infimum = infimum
        self.supremum = supremum
        self.left_child = None
        self.right_child = None
        self.is_included = False

    def include(self, left, right):
        print(f"({self.infimum},{self.supremum}): Including [{left}, {right}]")
        if self.is_included:
            return
        elif left == self.infimum and right == self.supremum:
            self.left_child = None
            self.right_child = None
            self.is_included = True
        else:
            midpoint = (self.infimum+self.supremum)//2
            if right <= midpoint:
                self.force_left_include(left,right)
            elif left >= midpoint+1:
                self.force_right_include(left,right)
            else:
                self.force_left_include(left,midpoint)
                self.force_right_include(midpoint+1,right)

            # Defragmentation
            if self.left_child != None and self.left_child.is_included and self.right_child != None and self.right_child.is_included:
                self.left_child = None
                self.right_child = None
                self.is_included = True
    
    def is_inside_intervals(self, x):
        if x < self.infimum or x > self.supremum:
            return False
        elif self.is_included:
            return True

        midpoint = (self.infimum + self.supremum)//2
        if x <= midpoint:
            if self.left_child == None:
                return False
            else:
                return self.left_child.is_inside_intervals(x)
        else:
            if self.right_child == None:
                return False
            else:
                return self.right_child.is_inside_intervals(x)

    def count_elements(self):
        if self.is_included:
            return self.supremum-self.infimum+1
        
        s = 0
        if self.left_child != None:
            s+=self.left_child.count_elements()

        if self.right_child != None:
            s+=self.right_child.count_elements()

        return s



    def force_left_include(self, left, right):
        """
        Creates a left child if None, then includes
        """
        midpoint = (self.infimum + self.supremum)//2
        if self.left_child == None:
            self.left_child = Node(self.infimum, midpoint)
        self.left_child.include(left,right)

    def force_right_include(self, left, right):
        """
        Creates a right child if None, then includes
        """
        midpoint = (self.infimum + self.supremum)//2
        if self.right_child == None:
            self.right_child = Node(midpoint+1,self.supremum)
        self.right_child.include(left,right)

    def print(self, indentation=""):
        print(f"{indentation}-[{self.infimum},{self.supremum}]")
        if self.left_child != None:
            self.left_child.print(indentation+"|")
        else:
            print(f"{indentation}|-None")

        if self.right_child != None:
            self.right_child.print(indentation+"|")
        else:
            print(f"{indentation}|-None")







reading_intervals=True
intervals=[]
global_lower_bound = None
global_upper_bound = None
root = None

s=0

for line in stdin:
    line=line.replace('\n','')
    if reading_intervals:
        if line == "":
            reading_intervals=False
            print(f"[{global_lower_bound}, {global_upper_bound}]")
            root = Node(global_lower_bound,global_upper_bound)
            for i, interval in enumerate(intervals):
                root.include(interval[0],interval[1])
                print(f"Included interval {interval} ({i}/{len(intervals)})")
            root.print()
            continue


        first_str, second_str = line.split("-")
        first=int(first_str)
        second=int(second_str)
        if global_lower_bound == None or first < global_lower_bound:
            global_lower_bound = first
        if global_upper_bound == None or second > global_upper_bound:
            global_upper_bound = second

        intervals.append([first,second])
    else:
        if line == "":
            break
        x=int(line)
        if(root.is_inside_intervals(x)):
            print(f"{x} fresh")
            s+=1
        else:
            print(f"{x} spoiled")
        pass

print(f"{s} of the available ingredient IDs are fresh.")
print(f"Total amount of fresh ingredients: {root.count_elements()}")
