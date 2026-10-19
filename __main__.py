from . import all_programs as progs
from .Programs import add_deps
from .Programs.Manager import Program
from .Changelog import find_version_info
from .Database import User
__version__ = "0.0.3.0.00rc2" # In-dev build 9.


def main(mode: str = "C#r*"):
    all_programs = add_deps(progs)
    try:
        print(find_version_info(fullstr=__version__))
    except NotImplementedError:
        print("Warning: You are running an undocumented version of HubBase.")
    user = User()
    user.login(resetpau=True)
    for pr_id in all_programs:
        try:
            Program(pr_id).run(user)
        except BaseException as e:
            print(f"[HubBase Engine] Shutting down... {e}")
            break


if __name__ == '__main__':
    main()
