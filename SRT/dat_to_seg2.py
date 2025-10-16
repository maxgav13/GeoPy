import os
import shutil
import glob
# import pathlib
# import seisio
# from obspy import read

source_f = r"SRT/sample data/prueba/data/" # Source folder
dest_f = source_f + "SEG/" # Destination folder

os.makedirs(dest_f, exist_ok=True) # Create destination folder if it doesn't exist

matching_files = glob.glob(os.path.join(source_f, "*.dat")) # Find all .dat files in source folder

for file_path in matching_files: # Copy each .dat file to destination folder
    shutil.copy(file_path, dest_f)

for filename in os.listdir(dest_f): # Rename .dat files to .seg2 in destination folder
    if filename.endswith(".dat"):
        old_filepath = os.path.join(dest_f, filename)
        new_filename = filename.replace(".dat",".seg2")
        new_filepath = os.path.join(dest_f, new_filename)

        try:
            os.rename(old_filepath, new_filepath)
            print(f"Renamed '{filename}' to '{new_filename}'.")
        except OSError as e:
            print(f"Error renaming '{filename}': {e}")

## Alternative method using pathlib

# segfiles = pathlib.Path(dest_f)
# datlist = list(segfiles.glob("*.dat"))

# for d in datlist:
#     n_d = d.with_suffix(".seg2")
#     d.rename(n_d)

## seg2 to segy conversion using seisio or obspy

# seg2_files = glob.glob(os.path.join(dest_f, "*.seg2"))

# for f in seg2_files:
#     sio = seisio.input(f)
#     dataset = sio.read_dataset()
#     ntraces = sio.nt
#     nsamples = sio.ns
#     sampling_interval = sio.vsi
#     out = seisio.output(f.replace('seg2','sgy'), 
#                         ns=nsamples, 
#                         vsi=sampling_interval, 
#                         endian=">", 
#                         format=5, 
#                         txtenc="ebcdic")
#     out.init()
#     out.write_traces(data=dataset[0],headers=dataset[1])
#     out.finalize()

# seg2list = list(segfiles.glob("*.seg2"))

# for f in seg2list:
#     st = read(f)
#     f_str = str(f)
#     st.write(f_str.replace('seg2','segy'), format='SEGY')
