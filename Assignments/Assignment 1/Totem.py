# Lihong Wang, lw324, lihong.wang062@duke.edu

import random

def part_hair_spiky():
    """
    1 Returns a string that is
    spiky hair
    """
    s = r"012345678901234567"
    s = r" | | | |  | | | | " + "\n"
    s+= r" /\/\/\/\/\/\/\/\ "
    return s

def part_hair_curly():
    """
    2 Returns a string that is
    curly hair
    """
    s = r"012345678901234567"
    s = r" {}{{}}{{}}{{}}{} " + "\n"
    s+= r" {{{{}}{}{}{{}}}} "
    return s

def part_eyes_left():
    """
    3 Returns a string that is
    eyes looking left
    """
    s = r"012345678901234567"
    s = r" /     \  /     \ " + "\n"
    s+= r" o      || o    | " + "\n"
    s+= r" \_____/  \_____/ "
    return s

def part_eyes_right():
    """
    4 Returns a string that is
    eyes looking straight
    """
    s = r"012345678901234567"
    s = r" /     \  /     \ " + "\n"
    s+= r" |     o||      o " + "\n"
    s+= r" \_____/  \_____/ "
    return s

def part_eyes_straight():
    """
    5 Returns a string that is
    eyes looking straight
    """
    s = r"012345678901234567"
    s = r" /     \  /     \ " + "\n"
    s+= r" |  o   ||   o  | " + "\n"
    s+= r" \_____/  \_____/ "
    return s

def part_mouth_closed():
    """
    6 Returns a string that is
    mouth closed
    """
    s = r"012345678901234567"
    s = r" |              | " + "\n"
    s+= r" |    _______   | "
    return s

def part_mouth_open():
    """
    7 Returns a string that is
    mouth open
    """
    s = r"012345678901234567"
    s = r" |    (    )    | " + "\n"
    s+= r" |    (____)    | "
    return s

def part_mouth_happy():
    """
    8 Returns a string that is
    mouth smiling
    """
    s = r"012345678901234567"
    s = r" |              | " + "\n"
    s+= r" |   \_____/    | "
    return s

def part_mouth_sad():
    """
    9 Returns a string that is
    mouth sad
    """
    s = r"012345678901234567"
    s = r" |    _____     | " + "\n"
    s+= r" |   /     \    | "
    return s

def part_nose_left():
    """
    10 Returns a string that is
    nose to the left
    """
    s = r"012345678901234567"
    s = r" |      /       | " + "\n"
    s+= r" |     /__      | "
    return s

def part_nose_right():
    """
    11 Returns a string that is
    nose to the right
    """
    s = r"012345678901234567"
    s = r" |       \      | " + "\n"
    s+= r" |      __\     | "
    return s

def part_chin_plain():
    """
    12 Returns a string that is
    a plain chin
    """
    s = r"012345678901234567"
    s = r" |______________| "
    return s

def happy_head():
    """
    1 Print a head that looks happy
    """
    print(part_hair_spiky())
    print(part_eyes_straight())
    print(part_nose_left())
    print(part_mouth_happy())
    print(part_chin_plain())

def sad_head():
    """
    2 Print a head that looks sad
    """
    print(part_hair_curly())
    print(part_eyes_left())
    print(part_nose_right())
    print(part_mouth_sad())
    print(part_chin_plain())

def worried_head():
    """
    3 Print a head that looks worried
    """
    print(part_hair_curly())
    print(part_eyes_right())
    print(part_nose_left())
    print(part_mouth_closed())
    print(part_chin_plain())

def head_with_eyes(eyefunc):
    """
    1 Print a head with eyes specified by eyefunc
    """
    print(part_hair_spiky())
    print(eyefunc())
    print(part_nose_right())
    print(part_mouth_happy())
    print(part_chin_plain())

def head_with_nose(nosefunc):
    """
    2 Print a head with nose specified by nosefunc
    """
    print(part_hair_spiky())
    print(part_eyes_straight())
    print(nosefunc())
    print(part_mouth_happy())
    print(part_chin_plain())

def head_with_mouth(mouthfunc):
    """
    3 Print a head with nose specified by nosefunc
    """
    print(part_hair_curly())
    print(part_eyes_straight())
    print(part_nose_left())
    print(mouthfunc())
    print(part_chin_plain())

def selfie_band():
    """
    Returns a string that is
    a selfie band
    """
    s = r"012345678901234567"
    s = r" +--------------+ " + "\n"
    s+= r" |lw324    lw324| " + "\n"
    s+= r" +--------------+ "
    return s

def selfie(eyefunc, mouthfunc):
    """
    Returns a string that is
    a head with a selfie band
    """
    print(part_hair_spiky())
    print(selfie_band())
    print(eyefunc())
    print(part_nose_right())
    print(mouthfunc())
    print(part_chin_plain())

def head_random():
    """
    Print a head with randomly chosen
    eyes
    """
    x = random.randint(1, 3)
    if x == 1:
        eyefunc = part_eyes_straight
    elif x == 2:
        eyefunc = part_eyes_right
    else:
        eyefunc = part_eyes_left
    head_with_eyes(eyefunc)


def totem_fixed():
    """
    Print the same totem pole with three
    heads, one happy, one sad, on worried
    """
    happy_head()
    sad_head()
    worried_head()

def totem_selfie():
    """
    Print a totem pole with selfie band
    By calling the selfie() helper function
    """
    selfie(part_eyes_straight, part_mouth_happy)
    selfie(part_eyes_left, part_mouth_sad)
    selfie(part_eyes_right, part_mouth_closed)

def totem_random():
    """
    Print three random heads
    using head_random()
    """
    head_random()
    head_random()
    head_random()

if __name__ == '__main__':
    print("\nfixed totem\n")
    totem_fixed()

    print("\nself totem\n")
    totem_selfie()

    print("\nrandom totem\n")
    totem_random()
