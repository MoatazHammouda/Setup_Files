import os

#Create folders for logging, streaming, quaternion and testing
desktop = "/home/pi/Desktop/"

lst = os.listdir(desktop)

if "MetaBase-CSV-Bash-Stream" not in lst:
	os.mkdir(desktop+"MetaBase-CSV-Bash-Stream")
	os.mkdir(desktop+"MetaBase-CSV-Bash-Stream/Old")

if "MetaBase-CSV-Bash" not in lst:
	os.mkdir(desktop+"MetaBase-CSV-Bash")
	os.mkdir(desktop+"MetaBase-CSV-Bash/Old")

if "MetaBase-CSV-Bash-Test" not in lst:
	os.mkdir(desktop+"MetaBase-CSV-Bash-Test")
	os.mkdir(desktop+"MetaBase-CSV-Bash-Test/Old")

if "MetaBase-CSV-Bash-Quat" not in lst:
	os.mkdir(desktop+"MetaBase-CSV-Bash-Quat")
	os.mkdir(desktop+"MetaBase-CSV-Bash-Quat/Old")

if "RSSI" not in lst:
	os.system(f"sudo git clone https://github.com/MoatazHammouda/RSSI_Node.git {desktop}RSSI")

if "Configs_Test" not in lst:
	os.system(f"sudo git clone -b test https://github.com/MoatazHammouda/ConfigFilesMB.git {desktop}Configs_Test")

if "Configs" not in lst:
	os.system(f"sudo git clone https://github.com/MoatazHammouda/ConfigFilesMB.git {desktop}Configs")

if "Synchronize_Data" not in lst:
	os.system(f"sudo git clone https://github.com/MoatazHammouda/synchronize_data.git {desktop}Synchronize_Data")

if "Bash_Scripts" not in lst:
	os.system(f"sudo git clone -b develop https://github.com/MoatazHammouda/Bash_Scripts.git {desktop}Bash_Scripts")
	os.system(f"sudo chmod u+x {desktop}Bash_Scripts/*")


