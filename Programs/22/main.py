from .rooms import build_rooms
from .game import Game
from .Layout import get_transition_text
from . import ProgramInfo as Info
import time
import sys

# imports

endingsdata = {0: ["Unknown", 1, "\033[91mThis ending is a fallback, and should not be seen\033[0m"],
1: ["Escaped", 0, "You escaped into the open world!"],
2: ["Quit", 1, "You gave up and met your end in the dungeon."],
3: ["Slain", 1, "You met your end in the dungeon."],
1001: ["Knocked out", 666, "You fall into the ...dungeon?"],
1002: ["Stayed", 0, "You stayed at the party, and left with all of your friends."],
1011: ["Left", 0, "You left the party early."],
1012: ["Overindulged", 2, "Too much punch..."],
1013: ["Poisoned", 1, "The punch was poisoned..."]
}


def transition():
    print(get_transition_text("Party"), end="")


def end(ending:int=0):
    try:
        endingdata = endingsdata[ending]
        print(f"{"Party" if ending > 999 else "Dungeon"}{" specific" if ending % 1000 > 9 else ""} ending {ending % 1000 % 10}: {str(endingdata[0]).upper()}")
        print(f"Note: {endingdata[2]}")
        time.sleep(1)
        if int(endingdata[1]) != 666:
            sys.exit(int(endingdata[1]))
        else:
            transition()
    except KeyError:
        end()


def party():
    rooms = build_rooms()
    Party = Game(rooms, "Party")
    ending = Party.full()
    end(ending)


def dungeon():
    rooms = build_rooms(indungeon=True)
    Dungeon = Game(rooms, "Dungeon")
    ending = Dungeon.full()
    end(ending)


def run():
    print(f"{Info['Name']} v{Info['Version']} - {Info['Description']}")
    party()
    dungeon()


if __name__ == '__main__':
    run()
