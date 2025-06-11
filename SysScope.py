import os
import json
import subprocess
import datetime
import shutil
from colorama import init, Fore, Style
import sys

init(autoreset=True)

DATA_FILE = "system_history.json"
SNAPSHOT_DIR = "snapshots"
BACKUP_DIR = "backup"
LOG_FILE = "system_log.txt"

os.makedirs(SNAPSHOT_DIR, exist_ok=True)
os.makedirs(BACKUP_DIR, exist_ok=True)


def create_snapshot():
    snapshot_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    snapshot_path = os.path.join(SNAPSHOT_DIR, f"snapshot_{snapshot_time}.txt")
    with open(snapshot_path, "w") as file:
        subprocess.run(["dpkg", "-l"], stdout=file)
    save_event("Snapshot erstellt", snapshot_time)


def save_event(event, timestamp):
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    data.append({"event": event, "timestamp": timestamp})
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def show_events():
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
        for entry in data:
            print(Fore.YELLOW + f"{entry['timestamp']}: {entry['event']}")
    except (FileNotFoundError, json.JSONDecodeError):
        print(Fore.RED + "Keine Ereignisse gefunden.")


def check_sysconfig():
    subprocess.run(["uname", "-a"])
    subprocess.run(["lsb_release", "-a"])
    subprocess.run(["df", "-h"])


def list_snapshots():
    snapshots = os.listdir(SNAPSHOT_DIR)
    if snapshots:
        print(Fore.GREEN + "Vorhandene Snapshots:")
        for snap in snapshots:
            print(Fore.CYAN + snap)
    else:
        print(Fore.RED + "Keine Snapshots vorhanden.")


def backup_snapshots():
    backup_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_path = os.path.join(BACKUP_DIR, f"backup_{backup_time}")
    shutil.copytree(SNAPSHOT_DIR, backup_path)
    save_event("Snapshots gesichert", backup_time)
    print(Fore.GREEN + f"Snapshots erfolgreich nach {backup_path} gesichert.")


def check_disk_usage():
    subprocess.run(["df", "-h"])


def show_processes():
    subprocess.run(["ps", "aux"])


def show_logs():
    try:
        with open(LOG_FILE, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print(Fore.RED + "Keine Logdatei gefunden.")


def show_network_connections():
    subprocess.run(["ss", "-tulnp"])


def show_users():
    subprocess.run(["who"])


def check_open_ports():
    subprocess.run(["nmap", "localhost"])


def show_firewall_status():
    try:
        result = subprocess.run(["ufw", "status"], capture_output=True, text=True, check=True)
        print(result.stdout)
        
    except subprocess.CalledProcessError as e:
        # Check if the error message is about missing root permissions
        if "need to be root" in e.stderr.lower():
            print(Fore.RED + "Um diese Aktion auszuführen, benötigen Sie Root-Rechte von Ihrem Betriebssystem. Führen Sie bitte „sudo python SysScope“ aus und wählen Sie 12. Firewall-Status anzeigen")


def show_system_time():
    subprocess.run(["date"])


def show_cpu_usage():
    subprocess.run(["top", "-bn1"])


def show_ram_usage():
    subprocess.run(["free", "-h"])


def menu():
    while True:
        print(Fore.CYAN + Style.BRIGHT + "\nSysScope - System-Historien-Analyse")
        options = [
            "Snapshot erstellen", "Ereignisse anzeigen", "Systemkonfiguration prüfen", "Snapshots auflisten",
            "Snapshots sichern", "Speicherplatz prüfen", "Prozessliste anzeigen", "Systemlogs anzeigen",
            "Netzwerkverbindungen anzeigen", "Nutzerinformationen anzeigen", "Offene Ports prüfen",
            "Firewall-Status anzeigen", "Aktuelle Systemzeit anzeigen", "CPU-Auslastung anzeigen",
            "RAM-Nutzung anzeigen", "Beenden"
        ]
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")

        if not sys.stdin.isatty():
            print("CI environment detected – skipping interactive menu.")
            choice = 12
        else:
            choice = input(Fore.YELLOW + "Wähle eine Option: ")
        functions = [
            create_snapshot, show_events, check_sysconfig, list_snapshots, backup_snapshots,
            check_disk_usage, show_processes, show_logs, show_network_connections, show_users,
            check_open_ports, show_firewall_status, show_system_time, show_cpu_usage, show_ram_usage
        ]

        if choice.isdigit() and 1 <= int(choice) <= len(options):
            if int(choice) == len(options):
                print(Fore.CYAN + "Programm beendet.")
                break
            functions[int(choice) - 1]()
        else:
            print(Fore.RED + "Ungültige Option.")


if __name__ == "__main__":
    menu()
