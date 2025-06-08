|![SysScope](https://github.com/bylickilabs/SysScope/actions/workflows/python-app.yml/badge.svg)|![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)|
|---|---|

# SysScope
  - SysScope ist eine Python-basierte Terminalanwendung, speziell entwickelt für Kali/Linux. Es bietet eine umfassende Systemüberwachung, Protokollierung und Analysefunktionen direkt aus dem Terminal heraus.

<br>

---

<br>

## Inhaltsverzeichnis

- [Funktionen](#funktionen)
- [Ordnerstruktur](#ordnerstruktur)
- [Installation](#installation)
- [Benutzung](#benutzung)
- [Abhängigkeiten](#abhängigkeiten)
- [Lizenz](#lizenz)

<br>

---

<br>

## Funktionen

- **Snapshot erstellen:** Speichert den Zustand der aktuell installierten Pakete.
- **Ereignisse anzeigen:** Übersicht der gespeicherten Systemereignisse.
- **Systemkonfiguration prüfen:** Zeigt Systeminformationen wie Kernel-Version und Speicherplatz.
- **Snapshots auflisten:** Listet vorhandene Snapshots auf.
- **Snapshots sichern:** Erstellt Backups der vorhandenen Snapshots.
- **Speicherplatz prüfen:** Überprüft die Speichernutzung.
- **Prozessliste anzeigen:** Zeigt eine Liste aller laufenden Prozesse.
- **Systemlogs anzeigen:** Gibt den Inhalt der Systemlogs aus.
- **Netzwerkverbindungen anzeigen:** Zeigt aktive Netzwerkverbindungen.
- **Nutzerinformationen anzeigen:** Gibt Informationen zu aktuellen Nutzern.
- **Offene Ports prüfen:** Prüft auf offene Netzwerkports.
- **Firewall-Status anzeigen:** Zeigt den Status der Firewall an.
- **Aktuelle Systemzeit anzeigen:** Gibt die aktuelle Systemzeit aus.
- **CPU-Auslastung anzeigen:** Zeigt die aktuelle CPU-Nutzung.
- **RAM-Nutzung anzeigen:** Gibt Informationen zur RAM-Nutzung aus.

<br>

---

<br>

## Ordnerstruktur

```
SysScope/
├── backup/                 # Gesicherte Snapshots
├── snapshots/              # Erstellte Snapshots
├── .gitignore              # Git Ignore-Datei
├── README.md               # Dokumentation
├── requirements.txt        # Benötigte Python-Abhängigkeiten
└── sys_scope.py            # Hauptprogramm
```

<br>

---

<br>

## Installation

### Schritt 1: Repository klonen

```bash
git clone <Repository-URL>
cd SysScope
```

### Schritt 2: Virtuelle Umgebung erstellen und aktivieren (optional, aber empfohlen)

```bash
python3 -m venv venv
source venv/bin/activate
```

### Schritt 3: Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

### Schritt 4: Programm ausführen

```bash
python sys_scope.py
```

<br>

---

<br>

## Benutzung
   - Beim Start von SysScope öffnet sich ein interaktives Terminalmenü, aus dem du alle Funktionen bequem auswählen und ausführen kannst.

<br>

---

<br>

## Abhängigkeiten

- Python 3.x
- colorama

Installiere Abhängigkeiten direkt über:

```bash
pip install colorama
```

<br>

---

<br>

## Lizenz
   - Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen findest du in der Datei `LICENSE` im Repository.
