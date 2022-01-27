class Wizard:
    def __init__(self, name, month, day, year):
        self.name = name
        self.month = month
        self.day = day
        self.year = year
    
    def hash_code(self):
        return self.day*12 + self.month
    
    def get_all_info_str(self):
        return "{}: {}/{}/{}".format(self.name, self.month, self.day, self.year)

    def __eq__(self, other):
        return self.name == other.name and self.month == other.month and self.day == other.day and self.year == other.year

    def __str__(self):
        return self.name

def get_all_wizards():
    """
    Return a list of all of the wizards in the database
    """
    wizards = []
    fin = open("HarryPotter.csv")
    for line in fin.readlines():
        name, month, day, year = line.split(",")
        wizards.append(Wizard(name, int(month), int(day), int(year)))
    return wizards


if __name__ == '__main__':
    wizards = get_all_wizards()
    for w in wizards:
        print(w, w.hash_code())