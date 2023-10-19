

def parse(feet_inches):
    part=feet_inches.split(" ")
    feet=float(part[0])
    inches=float(part[1])
    stud={"feet":feet,"inches":inches}
    return stud
    