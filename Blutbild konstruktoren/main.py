class Blutbild: 
    def __init__(self, Erythrozyten, Leukozyten):
        self.Eryhrozyten = Erythrozyten
        self.Leukozyten = Leukozyten
class GrossesBlutbild(Blutbild):
    def __init__(self, Erythrozyten, Leukozyten, HbWert):
        self.Eryhrozyten=Erythrozyten
        self.Leukozyten=Leukozyten
        self.HbWert=HbWert
    
    def print(self):
        

class  KleinesBlutbild(Blutbild):
    def __init__(self, Erythrozyten, Leukozyten):
        self.Leukozyten = Leukozyten
        self.Eryhrozyten = Erythrozyten

        Blutbild.__init__(self,Erythrozyten,Leukozyten)

new_Blutbild=Blutbild(200,300)
new_big_blutbild=GrossesBlutbild(200,300,2)
new_big_blutbild.HbWert
