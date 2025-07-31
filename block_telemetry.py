import subprocess
import os
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def disable_service(service_name):
    subprocess.run(["sc", "stop", service_name], stdout=subprocess.DEVNULL)
    subprocess.run(["sc", "config", service_name, "start=", "disabled"], stdout=subprocess.DEVNULL)

def set_registry(path, name, value):
    reg_cmd = f'reg add "{path}" /v {name} /t REG_DWORD /d {value} /f'
    subprocess.run(reg_cmd, shell=True)

def patch_hosts():
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    telemetry_entries = [
        "0.0.0.0 vortex.data.microsoft.com",
        "0.0.0.0 telemetry.microsoft.com",
        "0.0.0.0 watson.telemetry.microsoft.com",
        "0.0.0.0 settings-win.data.microsoft.com",
        "0.0.0.0 telecommand.telemetry.microsoft.com"
    ]
    with open(hosts_path, "a") as f:
        f.write("\n# Blocked Microsoft Telemetry\n")
        for line in telemetry_entries:
            f.write(line + "\n")

def main():
    if not is_admin():
        print("[!] Dieses Script muss als Administrator ausgeführt werden.")
        return

    print("[*] Deaktiviere Telemetrie-Dienste...")
    disable_service("DiagTrack")
    disable_service("dmwappushservice")

    print("[*] Setze Registry-Werte...")
    set_registry(r"HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection", "AllowTelemetry", "0")
    set_registry(r"HKLM\SOFTWARE\Microsoft\Windows\Windows Error Reporting", "Disabled", "1")

    print("[*] Patche Hosts-Datei...")
    patch_hosts()

    print("[+] Fertig! Starte den PC neu, um alle Änderungen zu übernehmen.")

if __name__ == "__main__":
    main()
