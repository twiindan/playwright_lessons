from dataclasses import dataclass


@dataclass
class User:
    email: str
    username: str
    firstname: str
    lastname: str
    password: str
