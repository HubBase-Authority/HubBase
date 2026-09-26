from .Items import Item
from .Creature import Creature
import random

def create_key(): return Item("Key", "Opens locked doors", {"special_use_conditions": ["unlock"]})


def create_punch(): return Item("Punch", "Left on table for 2 weeks", {"HealAmount": random.randint(-150, 25), "Target": "Player"})


def create_stalker(): return Creature("Shadow Stalker")


def create_potion(): return Item("Potion", "Closes your wounds", {"HealAmount": 30, "Target": "Player"})


def get_layout(code: str = "default") -> list:
    code = code.lower()
    if code == "default":
        layout = see_default_layout()
    elif code == "dungeon":
        layout = see_dungeon_layout()
    elif code == "party":
        layout = see_party_layout()
    else:
        layout = get_layout()
    return layout


def get_transition_text(code: str = "default") -> str:
    code = code.lower()
    if code == "default":
        text = ""
    elif code == "dungeon":
        text = ""
    elif code == "party":
        text = "You get knocked out from the back... \n"
    else:
        text = get_transition_text()
    return text


# see_*_layout() or see_*_rp():
def see_default_layout():
    return [["Spawn", {}]]


def see_dungeon_layout():
    return [
             ["Spawn", {"north": "hallway", "east": "sewers"}],
             ["Hallway", {"south": "spawn", "east": "armory", "west": "library", "north": "pre-exit"}],
             ["Sewers", {"west": "spawn", "north": "armory"}],
             ["Armory", {"west": "hallway", "south": "sewers"}],
             ["Library", {"east": "hallway", "north": "ritual"}],
             ["Pre-Exit", {"south": "hallway", "east": "exit", "west": "ritual"}],
             ["Ritual", {"south": "library", "east": "pre-exit"}],
             ["Exit", {"west": "pre-exit"}]
        ]


def see_party_layout():
    return [
            ["Spawn", {"north": "exit", "south": "living_room"}],
            ["Exit", {"south": "spawn"}],
            ["Living Room", {"north": "spawn", "south": "kitchen"}],
            ["Kitchen", {"north": "living_room", "south": "hallway"}],
            ["Hallway", {"north": "kitchen", "south": "pre-exit"}],
            ["Pre-Exit", {"north": "hallway", "south": "transition"}],
            ["Transition", {"north": "pre-exit"}]
        ]


def see_party_rp():
    return {
        "Unknown": {"name": "Unknown", "description": "", "items": []},
        "Exit": {"name": "Open World", "description": "", "items": []},
        "Spawn": {"name": "Front Entrance", "description": "You step into the door.", "items": [create_key()]},
        "Kitchen": {"name": "Kitchen", "description": "You feel like you want to eat.", "items": [create_punch()]},
        "Living Room": {"name": "Living Room", "description": "", "items": []},
        "Pre-Exit": {"name": "Basement", "description": "A rusty old cell with an exit", "items": []},
        "Transition": {"name": "Empty Room", "description": "A rusty old room...", "items": []},
        "Hallway": {"name": "Dark Hallway", "description": "A creepy hallway", "items": [], "locked": True}
    }


def see_dungeon_rp():
    return {
        "Unknown": {"name": "Unknown", "description": "", "items": []},
        "Exit": {"name": "Open World", "description": "", "items": []},
        "Spawn": {"name": "Dungeon Cell", "description": "A rusty old cell", "items": [create_key()]},
        "Pre-Exit": {"name": "The Door of the exit", "description": "A door, rumored to contain the Exit", "items": [], "creature": create_stalker()},
        "Hallway": {"name": "Dark Hallway", "description": "A creepy hallway", "items": []},
        "Sewers": {"name": "Flooded Sewers",
                   "description": "Stagnant water covers the floor. Something useful might be down here.",
                   "items": [create_potion()]},
        "Armory": {"name": "Abandoned Armory",
                   "description": "Rusted weapons line the walls. Most are broken beyond use.", "items": []},
        "Library": {"name": "Dusty Library", "description": "Shelves tower overhead, filled with decaying books.",
                    "items": []},
        "Ritual": {"name": "Ritual Chamber",
                   "description": "Strange markings cover the floor. An altar stands in the center.", "items": []}
    }
