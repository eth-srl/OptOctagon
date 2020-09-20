import sys
sys.path.insert(0, '../ELINA/python_interface')
import numpy as np

from fconv import fkrelu

inp = """1.0914518706365015 1 1 1
0.7037897001336353 1 1 0
0.537676045105144 1 1 -1
1.0292636993889446 1 0 1
0.6504383786533002 1 0 0
0.5156917944949679 1 0 -1
1.1791578236324034 1 -1 1
0.8947163575838206 1 -1 0
0.857437706969855 1 -1 -1
0.628425399455722 0 1 1
0.2760508616095165 0 1 0
0.21719466285478614 0 1 -1
0.5215858260931827 0 0 1
0.28217767842241803 0 0 -1
0.7639581990009716 0 -1 1
0.5834062500849349 0 -1 0
0.6963726402603853 0 -1 -1
0.38991936273238853 -1 1 1
0.18778986567560146 -1 1 0
0.23282318405342653 -1 1 -1
0.355528838732926 -1 0 1
0.2508672752205009 -1 0 0
0.3902844482853806 -1 0 -1
0.6848684778185293 -1 -1 1
0.6115739851762569 -1 -1 0
0.7598280080083571 -1 -1 -1"""

inp = inp.split('\n')
inp = [line.split() for line in inp]
inp = [list(map(float, line)) for line in inp]
inp = np.array(inp)

print(inp)

print(fkrelu(inp))




