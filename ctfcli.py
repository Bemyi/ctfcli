import os
import sys

def get_dirs(base_dir):

    return [directory for directory in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, directory)) and not directory.startswith('.')]

def install(base_dir):
    directories = get_dirs(base_dir)
    for directory in directories:
        command = f'ctf challenge install "{os.path.join(base_dir, directory)}"'
        os.system(command)

def update(base_dir):
    directories = get_dirs(base_dir)
    for directory in directories:
        command = f'ctf challenge sync "{os.path.join(base_dir, directory)}"'
        os.system(command)

if len(sys.argv) > 1:
    command = sys.argv[1]
    if command in ["install", "update"]:
        base_dir = sys.argv[2] if len(sys.argv) > 2 else "."
        if command == "install":
            install(base_dir)
        elif command == "update":
            update(base_dir)
    else:
        print("Comando no reconocido. Uso: python3 ctfcli.py install|update [base_directory]")
else:
    print("Uso: python3 ctfcli.py install|update [base_directory]")

