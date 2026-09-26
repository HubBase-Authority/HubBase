from typing import Any
from .Utils import player, gen_stats, cmdinput, help_cmd, find_room_by_type, ExitcodeToType, get_code
from .rooms import Room
# imports


class Game:
    def __init__(self, rooms: dict[str, Room], area: str):
        self.player = player
        self.stats = {}
        self.info: dict[str, Any] = {"quit": False, "current_room": "Spawn 1", "prev_room": "", "move": 0}
        self.indungeon = area != "Party"
        self.rooms = rooms

    def play(self):
        move: int = 1
        current_room = "Spawn 1"
        prev_room = ""
        while True:
            if self.player.health <= 0: break
            if current_room.startswith("Exit ") or current_room.startswith("Transition "): break
            if prev_room != current_room: self.rooms[current_room].print_info()
            prev_room = current_room
            cmd = cmdinput()
            if cmd == "help": print(help_cmd())
            elif cmd == "quit":
                self.info["quit"] = True
                break
            elif cmd == "look": self.rooms[current_room].print_info()
            elif cmd == "health": print(player.health)
            elif cmd == "inventory":
                for item in player.inventory: item.print_info()
            elif cmd.startswith("take "): self.rooms[current_room].take_item(cmd.removeprefix("take ").lower())
            elif cmd.startswith("use "):
                to_use = cmd.removeprefix("use ").lower()
                for item in player.inventory:
                    if item.name.lower() == to_use: item.use(self.rooms[current_room])
            elif cmd.startswith("go "):
                try:
                    targetdir = cmd.removeprefix("go ")
                    if targetdir in self.rooms[current_room].exits:
                        target_room = find_room_by_type(
                            ExitcodeToType(self.rooms[current_room].exits[targetdir]),
                            self.rooms
                        )
                        if target_room.locked:
                            print("The door is locked. You need a key.")
                            continue
                        if self.rooms[current_room].creature and self.rooms[current_room].creature_alive:
                            print(f"The {self.rooms[current_room].creature.name} blocks your path! Defeat it to get out!")
                            continue
                        current_room = target_room.key
                    else:
                        print(f"There is no exit at direction '{targetdir}'")
                except IndexError:
                    print("There is no exit at [BLANK]")
            elif cmd.startswith("fight"):
                creature = self.rooms[current_room].creature
                if creature is None: print("There is no creature here.")
                else:
                    while not (player.dead or creature.dead): creature.fight_player()
                    if creature.dead: self.rooms[current_room].creature_alive = False
            move += 1
        self.info["current_room"] = current_room
        self.info["prev_room"] = prev_room
        self.info["move"] = move

    def eval(self) -> int:
        self.stats = gen_stats(self)
        stats = self.stats if self.stats else {"health": -2147483648}
        if stats.get("health") == -2147483648: return 0
        code = get_code(stats)
        return code

    def full(self) -> int:
        self.play()
        return self.eval()
