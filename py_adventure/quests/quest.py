from .task import Task
from typing import List

class Quest:

    def __init__(self, quest_id: str, name: str, tasks: List[Task]) -> None:

        self._quest_id = quest_id
        self._name = name

        # for now, assuming linear chain of tasks. maybe later make little
        # state machine for branches etc
        self._tasks = tasks


    def get_quest_id(self) -> str:
        return self._quest_id