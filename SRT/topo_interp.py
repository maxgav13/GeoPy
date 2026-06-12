import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline
import os
import matplotlib.pyplot as plt

topo_file = 'topo.csv'
pts_file = 'pts.txt'

# Logic to read topo_file
if topo_file.endswith('.txt'):
    topo = np.loadtxt(topo_file, skiprows=1)
elif topo_file.endswith('.csv'):
    topo_df = pd.read_csv(topo_file)
    topo = topo_df.values 
else:
    raise ValueError(f"Unsupported file format for {topo_file}. Only .txt and .csv are supported.")

# Logic to read pts_file
if pts_file.endswith('.txt'):
    pts = np.loadtxt(pts_file, skiprows=1)
elif pts_file.endswith('.csv'):
    pts_df = pd.read_csv(pts_file)
    pts = pts_df.values 
else:
    raise ValueError(f"Unsupported file format for {pts_file}. Only .txt and .csv are supported.")

x0 = 0 
topo_x = topo[:,0] + x0
topo_y = topo[:,1]
pts_i = pts[:,0]

bspl = make_interp_spline(topo_x + x0, topo_y, k=3)
y_interp = bspl(pts_i)
print(y_interp)

pts_int = []
pts_int.append("x y\n")

for p in range(len(pts[:,0])):
    x = pts_i[p]
    y = y_interp[p]
    pts_int.append("{0:.2f} {1:.2f}\n".format(x, y))

# Robust file naming for output
base_name = os.path.splitext(pts_file)[0]
out_file_txt = f"{base_name}_int.txt"

with open(out_file_txt, 'w') as ptos:
    ptos.writelines(pts_int)

dat = pd.DataFrame(dict(x=pts_i, y=y_interp))
print(dat.head())

out_file_csv = f"{base_name}_int.csv"
dat.to_csv(out_file_csv, index=False, header=True)

plt.figure(figsize=(10, 6))
plt.plot(pts_i, y_interp,
         marker='o',
         linestyle='-',
         color='blue',
         label='Interpolated Elevation')
plt.xlabel('x (distance)')
plt.ylabel('y (elevation)')
plt.title('Interpolated Elevation Profile')
plt.grid(True)
plt.legend()
plt.show()