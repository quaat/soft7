from abc import ABC, abstractmethod
from soft.dataspace.database import Database
from typing import List

class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def read(self, database: Database):
        pass
    
    @abstractmethod
    def write(self, databases: List[Database]):
        pass


class Context():
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, strategy: Strategy) -> None:
        """
        Usually, the Context accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.
        """

        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self._strategy = strategy
            
    def read(self, database: Database) -> None:
        print ("reading data")
        result = self._strategy.read(database)
        print (result)
    
    def write(self, databases: List[Database]) -> None:    
        print ("writing data")
        result = self._strategy.write(databases)
        print (result)
        
