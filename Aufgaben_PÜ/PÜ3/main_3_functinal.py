#%% UC 2.0

#Importieren der nötigen Packete
import os
import pandas as pd
import neurokit2 as nk
import json
#%% UC 2.1 Einlesen der Daten

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

## Überprüfen ob Dateien vorhanden sind

folder_current = os.path.dirname(__file__) 
folder_input_data = os.path.join(folder_current, 'input_data')

list_of_new_tests = einlesen(folder_input_data)
new_ecg_data = list_of_new_tests[2]
ecg_data_3 = new_ecg_data["Subject_3"]



#%% UC 2.2 Vorverarbeiten der Daten

## Anlegen einer Zeitreihe der Herzfrequenz aus den EKG-Daten von Subject_3

def vorverarbeiten(new_ecg_data):
    """EKG Zeitreihe von Subject 3 erstellen mit average HR und Testdauer"""
    ekg_data=pd.DataFrame()
    ekg_data["ECG"] = new_ecg_data

    # Find peaks
    peaks, info = nk.ecg_peaks(ekg_data["ECG"], sampling_rate=1000)

    number_of_heartbeats = peaks["ECG_R_Peaks"].sum()

    duration_test_min = ekg_data.size/1000/60

    average_hr_test = number_of_heartbeats / duration_test_min

    ## Calculate heart rate moving average

    peaks['average_HR_10s'] = peaks.rolling(window=10000).mean()*60*1000
    peaks['average_HR_10s'].plot()

    return average_hr_test, peaks

average_hr_test, peaks = vorverarbeiten(ecg_data_3)



#%% UC 2.3 Analysieren der Daten auf Abbruch-Kriterium

# Wird im vorhinein nicht abgebrochen
termination = False

folder_input_data = os.path.join(folder_current, 'input_data')

#Json datei von Subject 3 geöffnet 
file_name = os.path.join(folder_input_data, 'subject_3.json')

f = open(file_name)

# returns JSON object as
# a dictionary
subject_data = json.load(f)

## Vergleich der Maximalen Herzfrequenz mit Alter des Patienten
def abbruch_check(subject_data):
    """Funktion vergleicht HF mit alter des Patienten und erkennt Abbruchkriterium"""
    
    maximum_hr = peaks['average_HR_10s'].max()

    subject_max_hr = 220 - (2022 - subject_data["birth_year"])

    if maximum_hr > subject_max_hr*0.90:
        termination = True

    return maximum_hr, subject_max_hr, termination

maximum_hr, subject_max_hr, termination = abbruch_check(subject_data)



#%% UC 2.4 Erstellen einer Zusammenfassung

## Ausgabe einer Zusammenfassung



#%% UC 2.5 Visualisierung der Daten

## Erstellung eines Plots




#%% UC 2.6 Manuelle Eingabe eines Abbruchkritierums

## Abfrage an Nutzer:in, ob Abgebrochen werden soll

manual_termination = False
manual_termination = input("Is this test invalid? (leave blank if valid): ")

if manual_termination != False:
    termination = True




#%% UC 2.7 Speichern der Daten

# Speichern der Daten

data = {"User ID": subject_data["subject_id"], "Reason for test termation": manual_termination, "Average Heart Rate": average_hr_test, "Maximum Heart Rate": subject_max_hr, "Test Length (s)": len(power_data_watts), "Test Power (W)": subject_data["test_power_w"], "Average Power": peaks_downsampled["Power (Watt)"].mean()}

json_data_to_save = json.dumps(data)

folder_current = os.path.dirname(__file__) 
folder_input_data = os.path.join(folder_current, 'result_data')
results_file = os.path.join(folder_input_data, 'data.json')

with open(results_file, 'w', encoding='utf-8') as f:
    json.dump(json_data_to_save, f, ensure_ascii=False, indent=4)