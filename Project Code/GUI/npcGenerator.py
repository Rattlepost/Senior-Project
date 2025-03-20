import random

class NPCGenerator:
    def __init__(self):
        self.healthPoints = 0
        self.name = ''
        self.race = ''
        self.class_ = ''
        self.alignment = ''

    def generate_health(self):
        self.healthPoints = random.randint(15, 70)
        return self.healthPoints

    def generate_name(self):
        with open('Project Code/GUI/Data Files/first-names.txt', 'r') as file_object:
            list_first_names = file_object.readlines()
            first_name = random.choice(list_first_names).strip()
        with open('Project Code/GUI/Data Files/last-names.txt', 'r') as file_object:
            list_last_names = file_object.readlines()
            last_name = random.choice(list_last_names).strip()
        self.name = first_name + ' ' + last_name
        return self.name

    def generate_race(self):
        with open('Project Code/GUI/Data Files/dnd-races.txt', 'r') as file_object:
            list_races = file_object.readlines()
            self.race = random.choice(list_races).strip()
        return self.race

    def generate_class(self):
        with open('Project Code/GUI/Data Files/dnd-classes.txt', 'r') as file_object:
            list_classes = file_object.readlines()
            self.class_ = random.choice(list_classes).strip()
        return self.class_

    def generate_alignment(self):
        with open('Project Code/GUI/Data Files/dnd-alignments.txt', 'r') as file_object:
            list_alignments = file_object.readlines()
            self.alignment = random.choice(list_alignments).strip()
        return self.alignment