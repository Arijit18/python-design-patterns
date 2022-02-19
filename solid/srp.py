"""
Single responsibility principle AKA Seperation of Concern:

A class should have single responsibility. In the following example, a class Journal is created.
This class lets user to add journal entries and remove them. The responsibility of persistance is
offloaded to another class called PersistenceManager.
"""


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    """Doesnt conform to SRP"""
    # def save(self, filename):
    #     file = open(filename, "w")
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename):
    #     ...
    #
    # def load_from_web(self, uri):
    #     ...


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("I ate pizza")
j.add_entry("I slept like a baby")

print(f"Journal entries: \n{j}")

file = r"journal.txt"
PersistenceManager.save_to_file(j, file)
