from exercice1 import Robot

class Human():
    __sexe=["male","female"]
    __stomach=[]
    

    def __init__(self,sexe,stomach):
        self.sexe = sexe
        self.stomach = stomach

    @property
    def sexe(self):
        return self.__sexe

    @sexe.setter
    def sexe(self,new_sexe):
        self.__sexe = new_sexe

    @property
    def stomach(self):
        return self.__stomach


class Cyborg(Robot, Human):   

    def __init__(self, name, sexe):   
        Robot.__init__(self, name)
        Human.__init__(self, sexe)



cyborg = Cyborg('Deux Ex Machina', 'M')

print(cyborg.name, 'sexe', cyborg.sexe)
print('Charging battery...')
cyborg.charge()
cyborg.status()
cyborg.eat('banana')
cyborg.eat(['coca', 'chips'])
cyborg.digest()

# cyborg.truc_fun()