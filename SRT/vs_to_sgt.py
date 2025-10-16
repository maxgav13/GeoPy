vs_file = 'SRT/sample data/prueba/picks/prueba.vs'
sgt_file = vs_file.replace(".vs", "_vs.sgt")
# sgt_file = 'Refrapy/sample data/prueba/picks/prueba_vs.sgt'

shot_l = []
sgt_obs = []

with open(vs_file, 'r') as vs:
        #   lines = vs.readlines()
          line1 = vs.readline()
          line2 = vs.readline()
          line1 = line1.split()
          line2 = line2.split()
          num_shots = int(line2[1])
          sta_spacing = float(line2[2])
          linenum = 2
          shot_sta = 0

          for line in vs:
            linenum += 1
            line_split = line.split()
            if len(line_split) != 3:
                if int(float(line_split[0])) == 0 and int(float(line_split[1])) == 0:
                    print("Encountered end of observations at line {0}".format(linenum))
                    break
                else:
                    raise ValueError('Invalid line format')
            if int(float(line_split[2])) == 0:
                shot_loc = float(line_split[0])
                shot_l.append(shot_loc)
                shot_sta += 1
                # shot_sta = int((shot_loc - first_shot) / sta_spacing + 1)
                continue
            if int(line_split[2]) == 1:
                geophone_loc = float(line_split[0])
                geophone_num = int((geophone_loc) / sta_spacing) + 1 + num_shots
                # geophone_num = int((geophone_loc - first_shot) / sta_spacing) + 1
                time_ms = float(line_split[1])
                time_s = time_ms / 1000
                line = "{0} {1} {2:.6f}\n".format(shot_sta, geophone_num, time_s)
                sgt_obs.append(line)

num_geophones = geophone_num - num_shots
# num_geophones = int((last_geophone - first_geophone) / sta_spacing) + 1
num_obs = len(sgt_obs)

station_lines = []
num_stations = int(geophone_num)
station_lines.append("{0} # shot/geophone points\n".format(num_stations))
station_lines.append("#x y\n")
y = 0.0

for s in range(len(shot_l)):
    x = shot_l[s]
    station_lines.append("{0:.2f} {1:.2f}\n".format(x, y))

for sta in range(num_geophones):
    x = sta * sta_spacing
    station_lines.append("{0:.2f} {1:.2f}\n".format(x, y))

print("Writing to file")
output = station_lines
output.append("{0} # measurements\n".format(num_obs))
output.append("#s g t\n")
output.extend(sgt_obs)
with open(sgt_file, 'w') as sgt:
    sgt.writelines(output)
print("Wrote {0} observations to {1}".format(num_obs, sgt_file))