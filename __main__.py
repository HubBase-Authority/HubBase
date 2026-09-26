from . import all_programs
from .Programs.Manager import Program
from .Changelog import find_version_info
from .Database import User
__version__ = "0.0.3.0.00b3"


def main():
    try:
        print(find_version_info(fullstr=__version__))
    except NotImplementedError:
        print("Warning: You are running an undocumented version of HubBase.")
    user = User()
    user.login(resetpau=True)
    for pr_id in all_programs:
        try:
            Program(pr_id).run(user)
        except ImportError as e:
            print(e)
        except Exception as e:
            print(f"Failed to run program {pr_id}: {e}")


if __name__ == '__main__':
    main()
