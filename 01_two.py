from sys import stdin

class Dial():
    def __init__(self):
        self.number_of_times_pointing_at_zero=0
        self.pointing_at=50
        print(f"- The dial starts by pointing at {self.pointing_at}.")

    def turn_left(self):
        self.pointing_at-=1
        if self.pointing_at==0:
            self.number_of_times_pointing_at_zero+=1
        if self.pointing_at==-1:
            self.pointing_at=99

    def turn_right(self):
        self.pointing_at+=1
        if self.pointing_at==100:
            self.pointing_at=0
        if self.pointing_at==0:
            self.number_of_times_pointing_at_zero+=1

    def turn_dial(self, input_string):
        direction = input_string[0]
        clicks = int(input_string[1:])
        prev_zeros=self.number_of_times_pointing_at_zero
        while clicks>0:
            if direction == 'R':
                self.turn_right()
            elif direction == 'L':
                self.turn_left()
            clicks-=1
        pass_by_zero=self.number_of_times_pointing_at_zero - prev_zeros
        print(f"- The dial is rotated {input_string} to point at {self.pointing_at}; during this rotation, it points at 0 {pass_by_zero} times.")

dial=Dial()

for line in stdin:
    input_string=line.replace('\n','')
    if input_string == "":
        break
    dial.turn_dial(input_string)

print("number_of_times_pointing_at_zero=",dial.number_of_times_pointing_at_zero)
