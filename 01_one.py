from sys import stdin

class Dial():
    def __init__(self):
        self.number_of_times_pointing_at_zero=0
        self.pointing_at=50
        print(f"- The dial starts by pointing at {self.pointing_at}.")

    def turn_dial(self, input_string):
        direction = 1 if input_string[0]=='R' else -1
        clicks = int(input_string[1:])
        final_value=int(self.pointing_at + direction*clicks)
        print(f"Direction={direction}, Clicks={clicks}, Final Value={final_value}")
        pass_by_zero=abs(final_value)//100
        if final_value<=0 and not (self.pointing_at==0 and pass_by_zero==0):
            pass_by_zero+=1

        self.number_of_times_pointing_at_zero+=pass_by_zero
        self.pointing_at=final_value%100
        print(f"- The dial is rotated {input_string} to point at {self.pointing_at}; during this rotation, it points at 0 {pass_by_zero} times.")

dial=Dial()

for line in stdin:
    input_string=line.replace('\n','')
    if input_string == "":
        break
    dial.turn_dial(input_string)

print("number_of_times_pointing_at_zero=",dial.number_of_times_pointing_at_zero)
