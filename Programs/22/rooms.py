from .Layout import see_party_rp, get_layout, see_dungeon_rp
from .Utils import ExitcodeToType

# imports ^

ROOM_POOL = see_party_rp()

ROOM_AMOUNT = {}

ROOMS = {}


class Room:  # class Room
    def __init__(self, type: str, exits: dict[str, str]):
        self.type = self.check_type(type)
        self.type_repeat = self.get_type_repeat(self.type)
        self.exits = self.check_exits(exits)
        self.key = f"{self.type} {self.type_repeat}"
        self.typeroomdata = ROOM_POOL[self.type]
        self.name = self.typeroomdata["name"]
        self.description = self.typeroomdata["description"]
        self.items = self.typeroomdata["items"]
        try:
            self.creature = self.typeroomdata["creature"]
        except KeyError:
            self.creature = None
        self.creature_alive = self.creature is not None
        try:
            self.locked = self.typeroomdata["locked"]
        except KeyError:
            self.locked = False

    @staticmethod
    def check_type(type: str) -> str:
        if type in ROOM_POOL.keys():
            return type
        else:
            type = "Unknown"
            return type

    @staticmethod
    def check_exits(exits: dict) -> dict:
        Validexits = {}
        for key in exits.keys():
            if not key in ["north", "south", "west", "east"]:
                continue
            elif not ExitcodeToType(exits[key]) in ROOM_POOL.keys():
                continue
            Validexits[key] = exits[key]
        return Validexits

    @staticmethod
    def get_type_repeat(type: str) -> int:
        try:
            ROOM_AMOUNT[type] += 1
        except KeyError:
            ROOM_AMOUNT[type] = 1
        return ROOM_AMOUNT[type]

    def adjacent_rooms(self):
        adj_rooms = []
        for roomdir in self.exits.keys():
            room = self.exits[roomdir]
            room = ExitcodeToType(room)
            adj_room = self.find_adjacent_room(roomdir, room)
            if isinstance(adj_room, Room):
                adj_rooms.append(adj_room)
        return adj_rooms

    def handle_unlock(self):
        used = False
        for roomdir in self.exits.keys():
            room = self.exits.get(roomdir)
            room = ExitcodeToType(room)
            adj_room = self.find_adjacent_room(roomdir, room)
            if isinstance(adj_room, Room):
                if adj_room.locked:
                    adj_room.locked = False
                    used = True
                    print(f"Unlocked {adj_room.name}. ")
        if not used:
            print("There are no locked rooms nearby.")
        return used

    def find_adjacent_room(self, dir: str, type: str) -> Room | None:
        if not dir in ["north", "south", "west", "east"]:
            return None
        room = ExitcodeToType(self.type, reverse=True)
        dir = self.flip_dir(dir)
        x = 1
        while f"{type} {x}" in ROOMS:
            self.searchforrooms(key=f"{type} {x}", param=f"exits-{dir}-{room}")
            x += 1
        final_room_key = self.searchforrooms(key=f"{type} {x-1}", param=f"exits-{dir}-{room}")
        try:
            return ROOMS[final_room_key]
        except KeyError:
            return None

    @staticmethod
    def flip_dir(dir: str) -> str | None:
        if dir == "north":
            return "south"
        if dir == "south":
            return "north"
        if dir == "west":
            return "east"
        if dir == "east":
            return "west"
        else:
            return None

    def searchforrooms(self, key: str, param: str | None = None):
        for roomkey in ROOMS.keys():
            params = self.unpack_params(ROOMS[roomkey], param)
            if key == roomkey and params:
                return roomkey
        return None

    @staticmethod
    def unpack_params(room: Room, params: str | None):
        params = params
        if not params:
            return True
        if params.startswith("exits-"):
            params = params.removeprefix("exits-")
            param1, param2 = params.split("-")
            try:
                return room.exits[param1] == param2
            except KeyError:
                return False
        return True

    def info(self):
        text = f"\n=== {self.name.upper()} === \n {self.description} \n"
        if self.items:
            items = ", ".join(item.name.lower() for item in self.items)
            text += f"You notice: {items} \n"
        if self.creature_alive:
            text += f"DANGER: {self.creature.name} lurks here! \n"
        text += f"Exits: {", ".join(self.exits.keys())}"
        return text

    def print_info(self):
        print(self.info())

    def take_item(self, name: str = ""):
        for item in self.items:
            if item.name.lower() == name: item.take(self)


def build_rooms(indungeon: bool = False) -> dict[str, Room]:
    global ROOM_AMOUNT, ROOM_POOL, ROOMS
    if indungeon:
        ROOM_POOL = see_dungeon_rp()
    else:
        ROOM_POOL = see_party_rp()
    ROOM_AMOUNT = {}
    area = "dungeon" if indungeon else "party"
    roomsu = get_layout(area)
    roomsp = {}
    for room in roomsu:
        roomobj = Room(*room)
        roomsp[roomobj.key] = roomobj
    ROOMS = roomsp
    return roomsp
