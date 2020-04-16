import os
import os.path

# Get unique machine ids
dev_ids = []
with open("../raw_data/machine_ids.txt") as f:
    for line in f.readlines():
        dev_ids.append(line.strip())

# Get the unique variable names from the raw data file

# filename = "../raw_data/data_2019_05_06_to_2019_09_08.csv"
filename = "../raw_data/OpenAg_CooperHewittData_2019_05_06-2020_01_21.csv"

# the file has the following columns: 
# device,report_time,var,name,value,values
#  we're interest in splitting out the var into individual files.

# First pass is we'll get all the var names
print("Getting Unique Vars")
total_lines = 0
varnames = []
with open(filename, "r") as f:
    for line in f.readlines():
        total_lines = total_lines + 1
        linesplit = line.split(',')
        if [linesplit[2], linesplit[3]] not in varnames and linesplit[2] != 'var':
            varnames.append([linesplit[2], linesplit[3]])
            print("Found var name: " + linesplit[2] + " - " + linesplit[3])

print("Done finding vars")


# create files for each var/name set.
def genfilename(varname):
    return varname[0] + "_" + varname[1] + ".csv"


def gendevicevarfile(deviceid, varname):
    data_dir = os.path.join(".", deviceid)
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
    return os.path.join(data_dir, genfilename(varname))


readings_files = {}
for dev_id in dev_ids:
    for vn in varnames:
        readings_files[gendevicevarfile(dev_id, vn)] = open(gendevicevarfile(dev_id, vn), 'w')
        readings_files[gendevicevarfile(dev_id, vn)].write("variable,sensor_name,timestamp_utc,value,value_json\n")

# loop through main raw data generating the new datafiles
current_line = 0
with open(filename, 'r') as f:
    current_line = current_line + 1
    if int((current_line/total_lines)*100) % 10 == 0:
        print(int((current_line/total_lines)*100) + "%")
    # skip the first one
    first_line = True
    for line in f.readlines():
        if not first_line:
            linesplit = line.split(',')
            dev_id = linesplit[0]
            report_time = linesplit[1]
            varname = linesplit[2:4]
            value = linesplit[4]
            values_json = ",".join(linesplit[5:])
            filename = gendevicevarfile(dev_id, varname)
            if filename in readings_files.keys():
                newline = ",".join(varname + [report_time, value, values_json])
                readings_files[filename].write(newline)
        else:
            first_line = False

for f in readings_files.keys():
    readings_files[f].close()
