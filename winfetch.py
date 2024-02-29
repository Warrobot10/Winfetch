import json
import datetime
import time
import wmi
import cpuinfo
from termcolor import colored, cprint


def load_themes_from_json(file_path):
    """
    Load themes from a JSON file.

    Args:
        file_path (str): The path to the JSON file containing themes.

    Returns:
        dict: A dictionary containing the loaded themes.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


# Load themes from JSON file
THEMES_FILE_PATH = "themes.json"  # Update with your themes file path
THEMES = load_themes_from_json(THEMES_FILE_PATH)

# Select a theme
SELECTED_THEME_NAME = "default"  # Change this to the theme name you want to use
SELECTED_THEME = THEMES[SELECTED_THEME_NAME]

start = time.time()

computer = wmi.WMI()

# Get GPU info
gpu_infos = [gpu.name for gpu in computer.Win32_VideoController()]

cpu = cpuinfo.get_cpu_info()["brand_raw"]

CURRENT_VERSION = "1.0.1"

time_now = datetime.datetime.now()
formatted_date = time_now.strftime("%d-%m-%Y")
formatted_time = time_now.strftime("%I:%M")
day = time_now.strftime("%A")

# Print Winfetch status
cprint(
    colored("Winfetch version ", SELECTED_THEME["header"])
    + colored(CURRENT_VERSION, SELECTED_THEME["value"])
)

# Print Date and time
cprint(
    colored("Date: ", SELECTED_THEME["header"])
    + colored(formatted_date, SELECTED_THEME["value"])
)
cprint(
    colored("Time: ", SELECTED_THEME["header"])
    + colored(formatted_time, SELECTED_THEME["value"])
)
cprint(
    colored("It is a ", SELECTED_THEME["header"])
    + colored(day, SELECTED_THEME["value"])
)

# Print System info
for i, gpu_info in enumerate(gpu_infos, start=1):
    cprint(
        colored(f"GPU {i}: ", SELECTED_THEME["header"])
        + colored(gpu_info, SELECTED_THEME["value"])
    )

cprint(
    colored("CPU: ", SELECTED_THEME["header"]) + colored(cpu, SELECTED_THEME["value"])
)

# Get CPU cores
cpu_cores = sum(int(cpu.NumberOfCores) for cpu in computer.Win32_Processor())
cprint(
    colored("CPU cores: ", SELECTED_THEME["header"])
    + colored(cpu_cores, SELECTED_THEME["value"])
)

end = time.time()

time_taken = end - start
time_taken_formatted = "{:.2f}".format(time_taken)
cprint(
    colored("Elapsed time: ", SELECTED_THEME["header"])
    + colored(time_taken_formatted, SELECTED_THEME["value"])
    + colored("s", SELECTED_THEME["value"])
)
