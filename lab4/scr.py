import os

# Put do direktorija sa skriptama
scripts_directory = "scripts"

# Generiraj <script> oznake
for script_file in os.listdir(scripts_directory):
    if script_file.endswith(".js"):
        print(f'<script src="{scripts_directory}/{script_file}"></script>')
