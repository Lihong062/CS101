"""
lihong.wang062@duke.edu
lw324
Lihong Wang
"""


def falling(time, velo):
    """
    return float indicating
    number of meters an object has
    fallen after being dropped/thrown
    with initial velocity given by
    float parameter velo
    (given in meters/second)
    and after falling for float parameter
    time seconds
    """
    print(velo*time + 0.5*9.81*time**2)
    return(velo*time + 0.5*9.81*time**2)