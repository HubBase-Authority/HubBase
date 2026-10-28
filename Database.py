from pathlib import Path
import json


class UserLike:
    def __init__(self, login: str = "", password: str = "1041", vip: bool = False):
        self.VipAccess = vip
        self.username = login
        self.password = password

    def __str__(self) -> str:
        return f"{self.username} (pass: {self.password}, VIP: {self.VipAccess})"

    def login(self, username: str, password: str = "1041", *, reset: bool = False):
        if reset: self.username, self.password = username, password
        else:
            if not (self.username == username and self.password == password): return
        self.VipAccess = input("VIP password -- ") == "5280"
        if not self.VipAccess:
            print("Incorrect.")
        else:
            print("Correct.")


class User(UserLike):
    def login(self, *, resetpau: bool = False):
        if resetpau:
            self.username, self.password = input("Username -- "), input("Password -- ")
        self.VipAccess = input("VIP password -- ") == "5280"
        if not self.VipAccess:
            print("Incorrect.")
        else:
            print("Correct.")


class JsonUser(User):
    def login(self, path: Path | None = None, *, load: bool = True):
        if load and path is not None:
            try:
                self.load(path)
            except Warning:
                super().login(resetpau=True)
        else:
            super().login(resetpau=True)

    def save(self, path: Path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.__dict__, f, indent=2)

    def load(self, path: Path):
        with open(path, "r", encoding="utf-8") as f:
            try:
                user: dict = json.load(f)
            except ValueError as e:
                raise Warning(f"No loaded user in {path.name}") from e
            if not isinstance(user, dict): raise Warning(f"No loaded user in {path.name}")
            for key in self.__dict__:
                try: self.__dict__[key] = user[key]
                except (KeyError, TypeError): continue
