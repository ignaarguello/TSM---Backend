class Task:
    def __init__(self, name, date, type):
        self.name = name
        self.date = date
        self.type = type

    def TaskDbColletion(self):
        return {
            "name": self.name,
            "date": self.date,
            "type": self.type,
        }
