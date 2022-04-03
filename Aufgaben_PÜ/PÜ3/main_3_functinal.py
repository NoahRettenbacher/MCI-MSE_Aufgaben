# UC 2.0
#%% UC 2.1 Einlesen der Daten

import os
import pandas as pd

def einlesen(folder_input_data):
    """Überprüft, ob im Datenordner Daten vorhanden sind und gibt eine Liste mit den zu verarbeitenden Daten zurück."""
    list_of_new_tests = []
    
    for file in os.listdir(folder_input_data):
    
        if file.endswith(".csv"):
            file_name = os.path.join(folder_input_data, file)
            #subject_id = file_name.split(".")[0][-1]
            new_ecg_data= pd.read_csv(file_name)
            ## Erstellen einer Liste von Tests, die zu verarbeiten sind
            list_of_new_tests.append(new_ecg_data)
    
    return list_of_new_tests

folder_current = os.path.dirname(__file__) 
folder_input_data = os.path.join(folder_current, 'input_data')

list_of_new_tests = einlesen(folder_input_data)


#new_ecg_data["Subject_3"].plot()

list_of_new_tests[0].plot()





#%% UC 2.2 Vorverarbeiten der Daten

## Anlegen einer Zeitreihe der Herzfrequenz aus den EKG-Daten



#%% UC 2.3 Analysieren der Daten auf Abbruch-Kriterium

## Vergleich der Maximalen Herzfrequenz mit Alter des Patienten



#%% UC 2.4 Erstellen einer Zusammenfassung

## Ausgabe einer Zusammenfassung



#%% UC 2.5 Visualisierung der Daten

## Erstellung eines Plots




#%% UC 2.6 Manuelle Eingabe eines Abbruchkritierums

## Abfrage an Nutzer:in, ob Abgebrochen werden soll




#%% UC 2.7 Speichern der Daten

# Speichern der Daten