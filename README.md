🚀 Anwendung
Speichere das Script z. B. als block_telemetry.py.

Starte es mit Adminrechten:

bash
Kopieren
Bearbeiten
# CMD mit Adminrechten:
python block_telemetry.py
💣 Optional: Erweiterung (Taskplaner, Firewall etc.)
Wenn du willst, kann ich dir noch folgende Funktionen dazupacken:

Deaktivieren aller Microsoft-Telemetrie-Tasks via schtasks

Firewall-Regeln setzen mit netsh advfirewall

Ausgabe in Log-Datei

Möchtest du das in einer erweiterten Version? Sag Bescheid – ich kann dir auch ein GUI-Tool draus bauen.






Du:
schreibe mir fü github was es macht und alle infos 


ChatGPT:
Perfekt – hier ist eine vollständige README.md für dein GitHub-Repository, inklusive Beschreibung, Funktionen, Anforderungen und rechtlicher Hinweise. Sie ist so geschrieben, dass du sie direkt auf GitHub verwenden kannst:

📦 Projekt: Windows Telemetrie Blocker (Python)
🛡️ Ein einfaches Python-Script zum Blockieren von Windows-Telemetrie, Tracking-Diensten und Microsoft-Domains – vollständig lokal, quelloffen und ohne zusätzliche Tools.

📋 Funktionen
Dieses Script deaktiviert oder blockiert folgende Windows-Telemetrie-Komponenten:

🛑 DiagTrack (Connected User Experiences and Telemetry) – wird gestoppt und deaktiviert

🛑 dmwappushservice – wird gestoppt und deaktiviert

🛠️ Registry-Hardening:

Setzt AllowTelemetry = 0 (nur sicherheitsrelevante Daten)

Deaktiviert Windows Error Reporting

📛 Modifiziert Hosts-Datei – blockiert bekannte Microsoft-Telemetrie-Endpunkte:

vortex.data.microsoft.com

telemetry.microsoft.com

watson.telemetry.microsoft.com

settings-win.data.microsoft.com

telecommand.telemetry.microsoft.com

⚙️ Systemanforderungen
✅ Windows 10 / 11 (alle Editionen)

✅ Python 3.7+

🛠 Muss als Administrator ausgeführt werden

🚀 Nutzung
🔽 Download des Repos:

bash
Kopieren
Bearbeiten
git clone https://github.com/Brunoido90/block_telemetry.py
cd windows-telemetry-blocker
🏁 Ausführen mit Administratorrechten:

bash
Kopieren
Bearbeiten
python block_telemetry.py
📌 Tipp: Rechtsklick auf cmd.exe → "Als Administrator ausführen"

📜 Was wird geändert?
Komponente	Aktion
DiagTrack	Stop + Deaktivierung
dmwappushservice	Stop + Deaktivierung
Registry: AllowTelemetry	Auf 0 gesetzt
Registry: Error Reporting	Deaktiviert
hosts Datei	Telemetrie-Domains blockiert

🧠 Warum?
Windows 10/11 überträgt regelmäßig Daten an Microsoft, z. B. zu:

App-Nutzung

Hardware

Systemabstürzen

Verhalten bei Updates

Optional: Standort & Kontakte (wenn aktiviert)

Dieses Script reduziert diese Übertragungen auf ein Minimum – ohne Zusatztools oder Eingriffe ins System über Drittanbieter.

❗ Wichtiger Hinweis
Dieses Script deaktiviert keine Firmware-Telemetrie wie Intel ME oder AMD PSP.

Funktionen wie Cortana, Windows Hello oder Telemetrie-basierte Diagnosefunktionen könnten eingeschränkt werden.

Bei Windows Home oder Pro kann Microsoft gewisse Telemetrie nicht vollständig abschalten (nur begrenzen).

Nutze dieses Script auf eigenes Risiko.

🔐 Haftungsausschluss
Dieses Projekt ist zu Bildungs- und Datenschutz-Zwecken gedacht. Der Autor übernimmt keine Verantwortung für Schäden, Datenverlust oder Systeminstabilität. Es liegt in deiner Verantwortung, das Script zu prüfen, bevor du es auf Produktivsystemen einsetzt.

📁 Lizenz
MIT License – du darfst alles verwenden, verändern, verteilen – bitte verlinke zurück, wenn du's weitergibst oder forkst.

