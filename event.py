class Event:
    def __int__(self, titre, date_debut, date_fin, description, type):
        self.__titre = titre
        self.__date_debut = date_debut
        self.__date_fin = date_fin
        self.__description = description
        self.__type = type


    def get_titre(self):
        return self.__titre

    def get_date_debut(self):
        return self.__date_debut

    def get_date_fin(self):
        return self.__date_fin

    def get_description(self):
        return self.__description

    def get_type(self):
        return self.__type
