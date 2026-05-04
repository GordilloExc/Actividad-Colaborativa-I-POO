from abc import ABC, abstractmethod

class Volador(ABC):

    @abstractmethod
    def volar(self):
        pass