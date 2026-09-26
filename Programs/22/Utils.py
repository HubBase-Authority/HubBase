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


def gen_stats(Game) -> dict[str, Any]:
    drank = False
    for item in Game.player.inventory:
        if item.name == "Punch": break
    else:
        for item in Game.player.fullinventory:
            if item.name == "Punch":
                drank = True
                break
    stats = {
        "area": "Dungeon" if Game.indungeon else "Party",
        "in_dungeon": Game.indungeon,
        "current_room": Game.info.get("current_room"),
        "final_room": Game.info.get("current_room"),
        "prefinal_room": Game.info.get("prev_room"),
        "drank_punch": drank,
        "quit": Game.info.get("quit", True),
        "escaped": Game.info.get("current_room").startswith("Exit ") or Game.info.get("current_room") == "Transition 1",
        "health": Game.player.health,
        "move": Game.info.get("move", 0)
    }
    return stats


def getvalidcmd() -> dict[str, dict[str, Any]]:
    return {"go": {"description": "Go to the specified direction, if it exists"},
            "inventory": {"description": "Look at inventory"},
            "take": {"description": "Take the specified item, if it exists"},
            "use": {"description": "Use the specified item, if it exists"},
            "help": {"description": "See the help message"},
            "look": {"description": "See the details of the room"},
            "quit": {"description": "Quit the game"},
            "fight": {"description": "Fight the creature in the room, if it exists"},
            "health": {"description": "See health"},
            }


def help_cmd():
    cmds = getvalidcmd()
    str_cmd = ""
    for name, descriptiondict in cmds.items():
        description = descriptiondict.get('description')
        str_cmd += f"{name} - {description if description else '[BLANK]'} \n"
    return str_cmd


def isvalidcmd(cmd: str) -> bool:
    return cmd in getvalidcmd().keys() or cmd.startswith("go ") or cmd.startswith("take ") or cmd.startswith("use ")


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

def get_code(stats: dict):
    code = 0 if stats.get("in_dungeon") else 1000
    if stats.get("drank_punch"): code += 10
    if stats.get("escaped"):
        if stats.get("drank_punch"):
            code -= 10
        code += 1
        if stats.get("final_room") == "Exit 1" and stats.get("area") == "Party":
            code += 10
            if stats.get("drank_punch"): code += 1
    else:
        if stats.get("quit"): code += 2
        elif stats.get("health", 0) <= 0: code += 3
    return code
