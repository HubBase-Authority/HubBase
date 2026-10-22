from pathlib import Path
from . import all_programs as progs
from .Programs import add_deps
from .Programs.Manager import Program
from .Changelog import find_version_info
from .Database import JsonUser, User
__version__ = "0.0.3.0.00rc2" # In-dev build 11.
self_path = Path(__file__)


def default_entrance(intr: bool = True, user_e: JsonUser | None = None):
    user_e = user_e or JsonUser()
    if intr:
        all_programs = add_deps(progs)
        try:
            print(find_version_info(fullstr=__version__))
        except LookupError:
            print("Warning: You are running an undocumented version of HubBase.")
        user = JsonUser()
        upath = self_path.parent / "Data" / "user.json"
        if upath.is_file(): user.login(upath, load=True)
        else: user.login()
        return all_programs, user
    else:
        return progs, user_e


def main(mode: str = "C#r*", *, intr: bool = True, user_e: JsonUser | None = None, adddeps: bool = False, _return: bool = False):
    all_programs, user = default_entrance(intr, user_e)
    if adddeps: all_programs = add_deps(all_programs)
    if mode.startswith("C#"):
        if mode == "C#r*":
            for pr_id in all_programs:
                try:
                    Program(pr_id).run(user)
                except BaseException as e:
                    print(f"[HubBase Engine] Shutting down... {e}")
                    break
        elif mode == "C#ri":
            while True:
                pr_id = input("Launch program -- ")
                try:
                    Program(pr_id).run(user)
                except FileNotFoundError:
                    print(f"There is no program with id {pr_id}")
                except BaseException as e:
                    print(f"[HubBase Engine] Shutting down... {e}")
                    break
        elif mode.startswith("C#r"):
            pr_id = mode.removeprefix("C#r")
            try:
                Program(pr_id).run(user)
            except FileNotFoundError:
                print(f"There is no program with id {pr_id}")
            except BaseException as e:
                print(f"[HubBase Engine] Shutting down... {e}")
        elif mode.startswith("C#G"):
            to_get = mode.removeprefix("C#G")
            if to_get == "v": print(__version__)
            elif to_get == "lf" or to_get == "l": print(self_path)
            elif to_get == "ld": print(self_path.parent)
            elif to_get == "ap": print(all_programs)
        else:
            raise LookupError(f"Mode {mode} is not valid")
    elif mode.lower() == "skip": pass
    else: raise LookupError(f"Mode {mode} is not valid")
    if intr: user.save(self_path.parent / "Data" / "user.json")
    if _return:
        return user, all_programs, self_path, __version__
    return None



if __name__ == '__main__':
    main()
