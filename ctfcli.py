import os
import sys
import yaml

def get_dirs(base_dir):
    return [directory for directory in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, directory)) and not directory.startswith('.')]

def read_challenge(directory):
    challenge_path = os.path.join(directory, "challenge.yml")
    with open(challenge_path, "r") as f:
        challenge_data = yaml.safe_load(f)
    
    return challenge_data

def install(base_dir, difficulty):
    directories = get_dirs(base_dir)

    for directory in directories:
        challenge_data = read_challenge(os.path.join(base_dir, directory))
        tags = [tag.lower() for tag in challenge_data.get("tags", [])]

        if difficulty is None or difficulty in tags:
            print("entro")
            command = f'ctf challenge install "{os.path.join(base_dir, directory)}"'
            os.system(command)

def update(base_dir, difficulty):
    directories = get_dirs(base_dir)
    for directory in directories:
        challenge_data = read_challenge(os.path.join(base_dir, directory))
        tags = [tag.lower() for tag in challenge_data.get("tags", [])]

        if difficulty is None or difficulty in tags:
            command = f'ctf challenge sync "{os.path.join(base_dir, directory)}"'
            os.system(command)

if len(sys.argv) > 1:
    command = sys.argv[1]
    if command in ["install", "update"]:
        base_dir = sys.argv[2] if len(sys.argv) > 2 else "."
        difficulty = sys.argv[3] if len(sys.argv) > 3 else None

        if command == "install":
            install(base_dir, difficulty)
        elif command == "update":
            update(base_dir, difficulty)
    else:
        print("Comando no reconocido. Uso: python3 ctfcli.py [install|update] [base_directory] [difficulty]")
else:
    print("Uso: python3 ctfcli.py install|update [base_directory] [difficulty]")

