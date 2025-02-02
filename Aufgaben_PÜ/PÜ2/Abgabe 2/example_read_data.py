# %% Import der nötigen Pakete
import numpy as np
import matplotlib.pyplot as plt

# %% Öffnen der Datei und konvertieren zu numpy-Array


def Leistungsdaten(i):
        file_name= "input_data/power_data_" + str(i) + ".txt"
        power_data_watts = open(file_name).read().split("\n")
        x = np.array(power_data_watts)
        
        print(file_name)
        plt.title("Line graph " + str(i)) #nummerierung der Plots
        plt.plot(x, color="red")

        plt.show()

# %% Erstellen des Plots
for i in range(1,4):
    Leistungsdaten(i)
    
# Bewertung: Gute Lösung. Nächstes mal die For-Schleife um die Leisutngsdaten herum schreiben. siehe unten:
# for i in range(1,4):
#    Leistungsdaten(i)

# %%

# %%
