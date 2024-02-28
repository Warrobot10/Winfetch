import datetime
import wmi
import cpuinfo
from termcolor import colored, cprint
import time

start = time.time()

computer = wmi.WMI()

# Get GPU info
gpu_infos = [gpu.name for gpu in computer.Win32_VideoController()]

cpu = cpuinfo.get_cpu_info()['brand_raw']

current_version = "0.5.0"

time_now = datetime.datetime.now()
formatted_date = time_now.strftime("%d-%m-%Y")
formatted_time = time_now.strftime("%I:%M")
day = time_now.strftime("%A")

# Print Winfetch status
cprint(colored("Winfetch version ", "white") + colored(current_version, "cyan"))

# Print Date and time
cprint(colored("Date: ", "white") + colored(formatted_date, "cyan"))
cprint(colored("Time: ", "white") + colored(formatted_time, "cyan"))
cprint(colored("It is a ", "white") + colored(day, "cyan"))

# Print System info
for i, gpu_info in enumerate(gpu_infos, start=1):
    cprint(colored(f"GPU {i}: ", "white") + colored(gpu_info, "cyan"))

cprint(colored("CPU: ", "white") + colored(cpu, "cyan"))

# Get CPU cores
cpu_cores = sum(int(cpu.NumberOfCores) for cpu in computer.Win32_Processor())
cprint(colored("CPU cores: ", "white") + colored(cpu_cores, "cyan"))

end = time.time()

time_taken = end - start
time_taken_formatted = "{:.2f}".format(time_taken)
cprint(colored("Elapsed time: ", "white") + colored(time_taken_formatted, "cyan") + colored("s", "cyan"))
