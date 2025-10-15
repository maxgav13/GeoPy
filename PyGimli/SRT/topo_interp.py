import numpy as np
from scipy.interpolate import make_interp_spline

topo_file = 'GeoPy/PyGimli/ERT/DD_topo.txt'
pts_file = 'GeoPy/PyGimli/SRT/pts.txt'

topo = np.loadtxt(topo_file, skiprows=1)
pts = np.loadtxt(pts_file, skiprows=1)

x0 = 0 
topo_x = topo[:,0] + x0
topo_y = topo[:,1]
pts_i = pts[:,0]

bspl = make_interp_spline(topo[:,0] + x0, topo[:,1], k=3)
y_interp = bspl(pts_i)
print(y_interp)

pts_int = []
pts_int.append("x y\n")

for p in range(len(pts[:,0])):
    x = pts_i[p]
    y = y_interp[p]
    pts_int.append("{0:.2f} {1:.2f}\n".format(x, y))

out_file = pts_file.replace(".txt", "_int.txt")

with open(out_file, 'w') as ptos:
    ptos.writelines(pts_int)
