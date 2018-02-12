Python 3.6.4 (v3.6.4:d48ecebad5, Dec 18 2017, 21:07:28) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> players = [29, 58, 66, 71, 87]
>>> players[2]
66
>>> players[2] = 68
>>> players
[29, 58, 68, 71, 87]
>>> players + [90, 91, 98]
[29, 58, 68, 71, 87, 90, 91, 98]
>>> players
[29, 58, 68, 71, 87]
>>> players.append(120)
>>> players
[29, 58, 68, 71, 87, 120]
>>> players[:2]
[29, 58]
>>> players[:2] = [0, 0]
>>> players
[0, 0, 68, 71, 87, 120]
>>> players[:2] = []
>>> players
[68, 71, 87, 120]
>>> players[:] = []
>>> players
[]
>>> 
