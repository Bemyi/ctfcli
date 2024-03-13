import os
import sys
import yaml

def get_dirs(base_dir):
    return [directory for directory in os.listdir(base_dir) 
    if os.path.isdir(os.path.join(base_dir, directory)) and not directory.startswith('.')]

def read_challenge(directory):
    challenge_path = os.path.join(directory, "challenge.yml")
    with open(challenge_path, "r") as file:
        challenge_data = yaml.safe_load(file)
    
    return challenge_data

if len(sys.argv) > 2:
    action = sys.argv[1]
    difficulties = ["basico", "intermedio", "avanzado"]
    actions = ["instalar", "actualizar"]

    if action in actions:
        base_dir = sys.argv[2] 
        difficulty_arg = sys.argv[3] if len(sys.argv) > 3 else None
        if difficulty_arg is None:
            difficulties_to_process = difficulties
        else:
            difficulties_to_process = difficulty_arg.split(",")

        for difficulty in difficulties_to_process:
            if difficulty.strip() not in difficulties:
                print("Error: las opciones de dificultades son 'basico' 'intermedio' 'avanzado'")
                sys.exit(1)

        directories = get_dirs(base_dir)

        for directory in directories:
            challenge_data = read_challenge(os.path.join(base_dir, directory))
            tags = [tag.lower() for tag in challenge_data.get("tags", [])]

            if not difficulties_to_process or any(difficulty in tags for difficulty in difficulties_to_process):
                if action == "instalar":
                    command = f'ctf challenge install "{os.path.join(base_dir, directory)}"'
                else:
                    command = f'ctf challenge sync "{os.path.join(base_dir, directory)}"'
                os.system(command)
    else:
        print("Comando no reconocido. Uso: python3 ctfcli.py instalar|actualizar directorio_categoria dificultad1,dificultad2")
else:
    print("Uso: python3 ctfcli.py instalar|actualizar directorio_categoria dificultad1,dificultad2")
