from dataclasses import dataclass


@dataclass
class Task:
    title: str
    description: str
    priority: str
