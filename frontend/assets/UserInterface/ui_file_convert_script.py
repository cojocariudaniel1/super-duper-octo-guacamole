import os
import subprocess

from backend.global_path import get_absolute_file_path

# Specifică folderul care conține fișierele .ui
folder_path = get_absolute_file_path(r"frontend\assets\UserInterface")

# Parcurge toate fișierele din folder și subfoldere
for root, _, files in os.walk(folder_path):
    for filename in files:
        # Verifică dacă fișierul are extensia .ui
        if filename.endswith(".ui"):
            ui_file_path = os.path.join(root, filename)

            # Creează numele fișierului .py
            py_file_path = os.path.join(root, f"{os.path.splitext(filename)[0]}.py")

            # Rulează comanda pyside6-uic pentru a converti fișierul .ui într-un fișier .py
            command = ["pyside6-uic", ui_file_path, "-o", py_file_path]

            try:
                # Execută comanda
                subprocess.run(command, check=True)
                print(f"Fișierul {filename} a fost convertit cu succes în {py_file_path}")
            except subprocess.CalledProcessError:
                print(f"Eroare la conversia fișierului {filename}")
