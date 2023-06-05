import os
import PyPDF2
from pdf2image import convert_from_path
from tqdm import tqdm
import subprocess
import time
import pyautogui

def execute_command_terminal(command):
    try:
        # Starten Sie den 'mokuro'-Befehl
        subprocess.Popen('start cmd /k {}'.format(command), shell=True)
        time.sleep(3)

        # Automatisches Eingeben von 'yes' und Drücken von Enter
        pyautogui.write('yes\n')

    except Exception as e:
        print("Error: ", e)


def build_mokuro_command(path):
    # Liste aller Dateien und Verzeichnisse im angegebenen Pfad
    entries = os.listdir(path)

    # Speichern der Verzeichnisnamen in einer Liste
    directory_names = []

    # Durchlaufen aller Einträge
    for entry in entries:
        # Vollständiger Pfad zum Eintrag
        full_path = os.path.join(path, entry)

        # Überprüfen, ob der Eintrag ein Verzeichnis ist
        if os.path.isdir(full_path):
            # Hinzufügen des Verzeichnisnamens zur Liste
            directory_names.append(f'"{full_path}"')

    # Erstellen des Befehls
    command = 'mokuro ' + ' '.join(directory_names)
    return command


def pdf_to_jpg(pdf_folder, output_folder):
    # Liste aller PDF-Dateien im Verzeichnis
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]

    # Erstellen Sie eine Fortschrittsleiste mit der Anzahl der PDF-Dateien
    pbar = tqdm(total=len(pdf_files), desc="Verarbeitete PDFs")

    # Überprüfen Sie alle Dateien in der Liste
    for filename in pdf_files:
        # Erstellen Sie für jedes PDF einen separaten Ausgabeordner
        pdf_output_folder = os.path.join(output_folder, filename.rstrip('.pdf'))
        os.makedirs(pdf_output_folder, exist_ok=True)

        # Pfad zur PDF-Datei
        pdf_path = os.path.join(pdf_folder, filename)

        # Anzahl der Seiten in der PDF ermitteln
        pdf_file_obj = open(pdf_path, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
        num_pages = len(pdf_reader.pages)
        pdf_file_obj.close()

        try:
            # Convert each page to an image
            for page_num in range(1, num_pages + 1):
                images = convert_from_path(pdf_path, first_page=page_num, last_page=page_num)
                images[0].save(pdf_output_folder + '/output' + str(page_num - 1) + '.jpg', 'JPEG')

            # Ausführen des 'marakudo'-Befehls
            # os.system('marakudo')

        except Exception as e:
            print("Error: ", e)

        # Aktualisieren Sie die Fortschrittsleiste
        pbar.update(1)

    # Schließen Sie die Fortschrittsleiste
    pbar.close()


pdf_folder = 'F:\mokuro\yotsuba\pdfs/'
output_folder = 'F:\mokuro\yotsuba\oleg/'

pdf_to_jpg(pdf_folder, output_folder)
command = build_mokuro_command(output_folder)

execute_command_terminal(command)
