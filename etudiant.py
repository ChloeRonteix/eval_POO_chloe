from statistics import mean

class Etudiant:

    def __init__(self, name):
        self.name = name
        self.notes = list()
        self.avg = float

    def __str__(self):
        return f'{self.name} a {self.avg} de moyenne'

    def add_notes(self, note):
        self.notes.append(note)
        print(f'{self.name} a eu un {note}/20!')
    
    def get_avg(self):
        avg = sum(self.notes)/len(self.notes)
        self.avg += avg
        return self.avg
        


    