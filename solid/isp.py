"""
Interface segregation principle:

Avoid making too many things in single interface
"""
from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplemented

    def fax(self, document):
        raise NotImplemented

    def scan(self, document):
        raise NotImplemented


class MultifunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldPrinter(Machine):
    def print(self, document):
        # Ok
        pass

    def fax(self, document):
        # Not OK: noop
        pass

    def scan(self, document):
        # Not Ok: noop
        pass

# Ok implementation
class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        print(document)


class PhotoCopier(Printer, Scanner):
    def scan(self, document):
        ...

    def print(self, document):
        ...
