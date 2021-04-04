"""
lihong.wang062@duke.edu
lw324
Lihong Wang
"""

def minutesNeeded(m):
    """
    Return integer number of minutes to launder m (integer) loads
    washing - 25 min; drying - 25 min; folding - 10 min
    Each load takes 60 min, new load can enter exactly 25 min after previous load
    So we need to return 60 + 25(m-1) minutes
    """
    # print (60 + (m - 1) * 25)
    return (60+(m-1)*25)
