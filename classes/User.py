from dataclasses import dataclass


@dataclass
class User:
    user_uuid: str
    username: str
    profile_image: str
    email: str
    role: str
    password: str
    attempts: int = 3
