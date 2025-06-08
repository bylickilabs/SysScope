import os
import json
import subprocess
import datetime
import shutil
from colorama import init, Fore, Style

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
    subprocess.run(["ufw", "status"])



def show_system_time():
    subprocess.run(["date"])



def show_cpu_usage():
    subprocess.run(["top", "-bn1"])



def show_ram_usage():
    subprocess.run(["free", "-h"])



def menu():
    while True:
        print(Fore.CYAN + Style.BRIGHT + "\nSysScope - System-Historien-Analyse")
        print(Fore.GREEN + "1. Snapshot erstellen")
        print("2. Ereignisse anzeigen")
        print("3. Systemkonfiguration prüfen")
        print("4. Snapshots auflisten")
        print("5. Snapshots sichern")
        print("6. Speicherplatz prüfen")
        print("7. Prozessliste anzeigen")
        print("8. Systemlogs anzeigen")
        print("9. Netzwerkverbindungen anzeigen")
        print("10. Nutzerinformationen anzeigen")
        print("11. Offene Ports prüfen")
        print("12. Firewall-Status anzeigen")
        print("13. Aktuelle Systemzeit anzeigen")
        print("14. CPU-Auslastung anzeigen")
        print("15. RAM-Nutzung anzeigen")
        print("16. Beenden")

        choice = input(Fore.YELLOW + "Wähle eine Option: ")

        functions = {'1': create_snapshot, '2': show_events, '3': check_sysconfig, '4': list_snapshots,
                     '5': backup_snapshots, '6': check_disk_usage, '7': show_processes, '8': show_logs,
                     '9': show_network_connections, '10': show_users, '11': check_open_ports,
                     '12': show_firewall_status, '13': show_system_time, '14': show_cpu_usage,
                     '15': show_ram_usage, '16': exit}

        if choice in functions:
            functions[choice]()
            if choice == '16':
                print(Fore.CYAN + "Programm beendet.")
                break
        else:
            print(Fore.RED + "Ungültige Option.")


if __name__ == "__main__":
    menu()
