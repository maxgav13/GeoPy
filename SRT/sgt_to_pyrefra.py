import numpy as np

shots = [2001, 2002, 2003, 2004, 2005] # número de disparos (nombre de los archivos)
n_geophones = 24 # número de geófonos
error = 0.003  # error fijo en segundos

sgt_file = 'SRT/picks/prueba.sgt'
pyrefra_file = sgt_file.replace(".sgt", ".dat")

t = []
e = []

with open(sgt_file, 'r') as sgt:
    line1 = sgt.readline().split()
    n_sensors = int(line1[0])
    start_line_number = n_sensors + 4
    for i, line in enumerate(sgt, 1):  # enumerate starts counting from 1
        if i >= start_line_number:
            line_split = line.split()
            if len(line_split) == 3:
                t.append(line_split[2])
                e = error
            elif len(line_split) == 4:
                t.append(line_split[2])
                e.append(line_split[3])

t_array = np.array(t, dtype=float)
e_array = np.array(e, dtype=float)

t_upper = t_array + e_array
t_lower = t_array - e_array

comb = []
for item1 in shots:
    for item2 in np.arange(1,n_geophones+1):
        comb.append((item1, int(item2)))

combined_array = np.array(comb)
print(combined_array[:10])

final_array = np.hstack((combined_array, 
                         t_array.reshape(-1,1), 
                         t_lower.reshape(-1,1), 
                         t_upper.reshape(-1,1)))
print(final_array[:10])

np.savetxt(pyrefra_file, final_array, fmt='%d %i %.5f %.5f %.5f')

# with open(sgt_file, 'r') as sgt:
#     lines = sgt.readlines()
#     line1 = lines[0].split()

# n_sensors = int(line1[0])
# n_obs = int(lines[2 + n_sensors].split()[0])
# sensors = lines[2:2 + n_sensors]
# data = lines[4 + n_sensors:4 + n_sensors + n_obs]

# sensor_array = np.array([list(map(float, line.split())) for line in sensors])
# data_array = np.array([list(map(float, line.split())) for line in data])
# times = data_array[:, 2]

# if data_array.shape[1] == 3:
#     error = error
# else:
#     error = data_array[:, 3]

# times_upper = times + error
# times_lower = times - error

# # combined_array = np.zeros((n_shots * n_geophones, 3))
# comb = []

# for item1 in shots:
#     for item2 in np.arange(1,n_geophones+1):
#         comb.append((item1, int(item2)))

# combined_array = np.array(comb)
# print(combined_array[:10])

# final_array = np.hstack((combined_array, 
#                          times.reshape(-1,1), 
#                          times_lower.reshape(-1,1), 
#                          times_upper.reshape(-1,1)))
# print(final_array[:10])

# np.savetxt(pyrefra_file, final_array, fmt='%d %i %.5f %.5f %.5f')
