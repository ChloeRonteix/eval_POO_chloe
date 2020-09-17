from statistics import mean
from note import Note

class Etudiant:

    def __init__(self, name):
        self.name = name
        self.notes = list()
        self.avg = float

    def __str__(self):
        return f'{self.name} a {self.avg} de moyenne'

    def add_note(self, note):
        pass

    def get_avg(self):
        pass
        


    