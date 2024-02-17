import datetime
import wmi
import cpuinfo
from termcolor import colored, cprint
import time

start = time.time()

computer = wmi.WMI()

# Iterates over Video cards windows finds and puts them in a list
gpu_infos = [gpu.name for gpu in computer.Win32_VideoController()]

cpu = cpuinfo.get_cpu_info()['brand_raw']

current_version = "0.2.0"

time_now = datetime.datetime.now()

formatted_time = time_now.strftime("%d-%m-%Y")

day = time_now.strftime("%A")

cprint(colored("Winfetch version ", "white") + colored(current_version, "cyan"))

cprint(colored("Date: ", "white") + colored(formatted_time, "cyan"))

cprint(colored("It is a ", "white") + colored(day, "cyan"))

# Iterates over the list of Video cards and prints them neatly
for i, gpu_info in enumerate(gpu_infos, start=1):
    cprint(colored(f"GPU {i}: ", "white") + colored(gpu_info, "cyan"))

cprint(colored("CPU: ", "white") + colored(cpu, "cyan"))

end = time.time()

time_taken = end - start

# Formats time_taken to display only the first two decimal places
time_taken_formatted = "{:.2f}".format(time_taken)

cprint(colored("Elapsed time: ", "white") + colored(time_taken_formatted, "cyan") + colored("s", "cyan"))
