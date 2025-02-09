import os
import subprocess

from backend.global_path import get_absolute_file_path

# Specifică folderul care conține fișierele .ui
folder_path = get_absolute_file_path(r"frontend\assets\ui_files")

# Parcurge toate fișierele din folder
for filename in os.listdir(folder_path):
    # Verifică dacă fișierul are extensia .ui
    if filename.endswith(".ui"):
        ui_file_path = os.path.join(folder_path, filename)
        
        # Creează numele fișierului .py
        py_file_path = os.path.join(folder_path, f"{os.path.splitext(filename)[0]}.py")
        
        # Rulează comanda pyside6-uic pentru a converi fișierul .ui într-un fișier .py
        command = ["pyside6-uic", ui_file_path, "-o", py_file_path]
        
        try:
            # Execută comanda
            subprocess.run(command, check=True)
            print(f"Fișierul {filename} a fost convertit cu succes în {py_file_path}")
        except subprocess.CalledProcessError:
            print(f"Eroare la conversia fișierului {filename}")
