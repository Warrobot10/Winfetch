import json
import datetime
import wmi
import cpuinfo
from termcolor import colored, cprint
import time


def load_themes_from_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


# Load themes from JSON file
themes_file_path = "themes.json"  # Update with your themes file path
themes = load_themes_from_json(themes_file_path)

# Select a theme
selected_theme_name = "default"  # Change this to the theme name you want to use
selected_theme = themes[selected_theme_name]

start = time.time()

computer = wmi.WMI()

# Get GPU info
gpu_infos = [gpu.name for gpu in computer.Win32_VideoController()]

cpu = cpuinfo.get_cpu_info()["brand_raw"]

current_version = "1.0.1"

time_now = datetime.datetime.now()
formatted_date = time_now.strftime("%d-%m-%Y")
formatted_time = time_now.strftime("%I:%M")
day = time_now.strftime("%A")

# Print Winfetch status
cprint(
    colored("Winfetch version ", selected_theme["header"])
    + colored(current_version, selected_theme["value"])
)

# Print Date and time
cprint(
    colored("Date: ", selected_theme["header"])
    + colored(formatted_date, selected_theme["value"])
)
cprint(
    colored("Time: ", selected_theme["header"])
    + colored(formatted_time, selected_theme["value"])
)
cprint(
    colored("It is a ", selected_theme["header"])
    + colored(day, selected_theme["value"])
)

# Print System info
for i, gpu_info in enumerate(gpu_infos, start=1):
    cprint(
        colored(f"GPU {i}: ", selected_theme["header"])
        + colored(gpu_info, selected_theme["value"])
    )

cprint(
    colored("CPU: ", selected_theme["header"]) + colored(cpu, selected_theme["value"])
)

# Get CPU cores
cpu_cores = sum(int(cpu.NumberOfCores) for cpu in computer.Win32_Processor())
cprint(
    colored("CPU cores: ", selected_theme["header"])
    + colored(cpu_cores, selected_theme["value"])
)

end = time.time()

time_taken = end - start
time_taken_formatted = "{:.2f}".format(time_taken)
cprint(
    colored("Elapsed time: ", selected_theme["header"])
    + colored(time_taken_formatted, selected_theme["value"])
    + colored("s", selected_theme["value"])
)
