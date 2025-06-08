|![SysScope](https://github.com/bylickilabs/SysScope/actions/workflows/SysScope.yml/badge.svg)|![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)|
|---|---|

# SysScope
  - SysScope ist eine Python-basierte Terminalanwendung, speziell entwickelt für Kali/Linux.
    - Es bietet eine umfassende Systemüberwachung, Protokollierung und Analysefunktionen direkt aus dem Terminal heraus.

|![sysScope 1280x640](https://github.com/user-attachments/assets/c406bdf8-dcde-454c-9e14-077a52515f8b)|
|---|

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
├── backup/                  # Gesicherte Snapshots
├── snapshots/               # Erstellte Snapshots
├── .github/
│   └── workflows/
│       └── sys-scope.yml    # CI Workflow YAML
├── .gitignore               # Git-Ignore Datei
├── README.md                # Projektdokumentation
├── LICENSE                  # Lizensierung
├── Security          
├── requirements.txt         # Python Abhängigkeiten
└── SysScope.py              # Hauptprogramm
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

| Option                         | Beschreibung                                       |
|          :---                  |                    :---:                           |
|                                |                                                    |
| Snapshot erstellen             | Speichert aktuellen Paketstand als Snapshot.       |
| Ereignisse anzeigen            | Zeigt alle gespeicherten Ereignisse.               |
| Systemkonfiguration prüfen     | Zeigt detaillierte Systeminformationen.            |
| Snapshots auflisten            | Listet gespeicherte Snapshots auf.                 |
| Snapshots sichern              | Sichert Snapshots in Backup-Ordner.                |
| Speicherplatz prüfen           | Zeigt aktuellen Speicherplatzverbrauch.            |
| Prozessliste anzeigen          | Listet alle laufenden Prozesse auf.                |
| Systemlogs anzeigen            | Gibt den Inhalt der Systemlogs aus.                |
| Netzwerkverbindungen anzeigen  | Listet aktive Netzwerkverbindungen auf.            |
| Nutzerinformationen anzeigen   | Zeigt eingeloggte Benutzer.                        |
| Offene Ports prüfen            | Prüft offene Netzwerkports.                        |
| Firewall-Status anzeigen       | Zeigt Firewall-Status an.                          |
| Systemzeit anzeigen            | Zeigt aktuelle Systemzeit an.                      |
| CPU-Auslastung anzeigen        | Prüft aktuelle CPU-Auslastung.                     |
| RAM-Nutzung anzeigen           | Zeigt aktuelle RAM-Auslastung an.                  |

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

<br>

---

<br>

## ❓ FAQs

### Welche Systeme werden unterstützt?
SysScope wurde speziell für Kali Linux entwickelt, läuft aber grundsätzlich auch auf anderen Debian-basierten Systemen.

### Wie melde ich einen Fehler?
Erstelle einfach ein Issue im Repository und beschreibe den Fehler möglichst präzise.

### Wie kann ich neue Features vorschlagen?
Erstelle ebenfalls ein Issue mit dem Label `enhancement`.

<br>

---

<br>

## 🤝 Mitwirken

Möchtest du am Projekt mitarbeiten? Großartig!

**Schritte zum Mitwirken:**
- Forke das Repository
- Erstelle einen neuen Branch: `git checkout -b dein-feature`
- Implementiere deine Änderungen
- Committe die Änderungen: `git commit -m "Dein Feature hinzugefügt"`
- Pushe deinen Branch: `git push origin dein-feature`
- Erstelle einen Pull Request auf GitHub

<br>

---

<br>

## 🚀 Zukunft von SysScope

- SysScope entwickelt sich kontinuierlich weiter. <p>

  - In Zukunft planen wir spannende neue Features, darunter eine automatisierte Snapshot-Planung, erweiterte Sicherheitsanalysen, eine interaktive Web-Oberfläche und verbesserte Performance für größere Systemlandschaften. <p>
  
    - Deine Vorschläge und dein Feedback sind essenziell, um SysScope stetig weiterzuentwickeln und deine Arbeit effizienter, sicherer und angenehmer zu gestalten. Sei ein Teil dieser Reise und gestalte mit uns die Zukunft von SysScope!

<br>

---

<br>

## 📜 Lizenz

Dieses Projekt steht unter der **MIT-Lizenz**. 
- Weitere Details findest du in der Datei [LICENNSE](https://github.com/bylickilabs/SysScope/blob/main/LICENSE).
