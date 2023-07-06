from event import *

class day:
    def __int__(self, name, event: None):
        self.__name = name
        if event is None:
            self.__event = []

    def ajouter_Event(self,event : Event):
        if isinstance(event,Event):
            self.__event.append(event)
            print("Evenement ajouté à " + self.__name)
        else:
            print("Mauvais ajout recommencer")

    def supprimerEvent(self, event):
        for evenement in self.__event:
            if event == evenement:
                self.__event.pop(evenement)
            else:
                print("Evenement non trouvé")

    def modifierEvent(self, event):
        pass