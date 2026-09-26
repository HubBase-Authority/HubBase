from .Player import Player
import random
from typing import Any
if __name__ != '__main__':
    player = Player()


def ExitcodeToType(value: str | None, reverse:bool=False) -> str:
    if value is None: return "Unknown"
    if reverse:
        value = value.replace(" ", "_").lower()
    else:
        value = value.replace("_", " ").title()
    return value


class DamageCalculationError(ArithmeticError):
    pass


def DefaultDamage(israndom: bool = True) -> int:
    if israndom:
        return random.randint(10, 20)
    else:
        return 15


def CalculateDamage(DamageType: str = str(DefaultDamage(False))) -> int:
    if DamageType.startswith("rand-"):
        damageargs = DamageType.removeprefix("rand-").split("t", 1)
        try:
            a = int(damageargs[0])
            b = int(damageargs[1])
        except ValueError as e:
            raise DamageCalculationError() from e
        Damage = random.randint(a, b)
    elif DamageType.isdigit():
        Damage = int(DamageType)
    else:
        raise DamageCalculationError("Unknown damage form.")
    return Damage


def GuardedCalculateDamage(DamageType: str = str(DefaultDamage(False))) -> int:
    try:
        return CalculateDamage(DamageType)
    except DamageCalculationError:
        return DefaultDamage()


def gen_stats(Game):
    pass # Inspect Game state
    # set current_room, inventory, health, drank_punch, area, quit from inspected game state


def getvalidcmd() -> dict[str, dict[str, Any] | list[Any]]:
    return {"go": {"description": "Go to the specified direction, if it exists"},
            "inventory": {"description": "Look at inventory"},
            "take": {"description": "Take the specified item, if it exists"},
            "use": {"description": "Use the specified item, if it exists"},
            "help": {"description": "See the help message"},
            "look": {"description": "See the details of the room"},
            "quit": {"description": "Quit the game"},
            "fight": {"description": "Fight the specified creature, if it exists"},
            }


def help_cmd():
    cmds = getvalidcmd()
    str_cmd = ""
    for name, descriptiondict in cmds.items():
        description = descriptiondict.get('description')
        str_cmd += f"{name} - {description if description else '[BLANK]'}"
    return str_cmd


def isvalidcmd(cmd: str) -> bool:
    return (cmd in getvalidcmd().keys() or cmd.startswith("go ") or cmd.startswith("take ") or cmd.startswith("use ")
            or cmd.startswith("fight "))


def cmdinput(prompt: object = ">>> ") -> str:
    try:
        cmd = input(prompt)
        if isvalidcmd(cmd):
            return cmd
        else:
            raise NameError("Invalid command")
    except BaseException as e:
        print(e)
        return "pass"


def find_room_by_key(key: str, rooms: dict[str, Any] | None):
    if rooms is None:
        return None
    for room in rooms.values():
        if room.key == key:
            return room
    return None


def find_room_by_type(type: str, rooms: dict[str, Any] | None):
    if rooms is None:
        return None
    for room in rooms.values():
        if room.type == type:
            return room
    return None
