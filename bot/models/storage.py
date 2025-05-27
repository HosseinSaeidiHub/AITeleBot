"""
Abstract storage interface + concrete adapters.
"""
from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def add_task(self, user_id: int, text: str): pass

    @abstractmethod
    def list_tasks(self, user_id: int): pass

class SQLiteStorage(Storage):
    def __init__(self, db_path="bot.db"):
        # TODO: connect…
        pass

    def add_task(self, user_id: int, text: str):
        pass

    def list_tasks(self, user_id: int):
        return []
