from pathlib import Path
import importlib, sys, subprocess


def load_deps() -> list[str]:
    deps = []
    requirementspath = Path(__file__).resolve().parent.parent / "requirements.txt"
    with open(requirementspath, "r", encoding="utf-8") as f:
        for line in f.readlines():
            deps.append(line.replace(" =", "STOP").replace(" ~", "STOP").replace(" >", "STOP").replace(" <", "STOP").split("STOP")[0])
    return deps


programs_dir = Path(__file__).resolve().parent
all_programs = programs_dir.iterdir()
all_programsl = []

for item in all_programs:
    if item.is_dir() and item.name != "__pycache__" and Path(item / "main.py").exists():
        all_programsl.append(item.name)

all_programs = sorted(
    all_programsl,
    key=lambda x: (not x.isdigit(), int(x) if x.isdigit() else x)
)

def add_deps(all_programsl: list[str | int]) -> list[str | int]:
    all_programsl = list[str | int](all_programsl)
    for module in load_deps():
        try:
            module_obj = importlib.import_module(module)
        except ImportError:
            print(f"You don`t have {module} installed.", end=" ")
            install_prompt = input("Install it?[Y/N] -- ").upper()
            if install_prompt == "Y":
                try:
                    requirements_path = str((Path(__file__).resolve().parent.parent / "requirements.txt").resolve())
                    _ = subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_path], check=True,
                                       capture_output=True)
                    print("Module installed.")
                    sys.exit(0)
                except subprocess.CalledProcessError:
                    print("Install failed.")
                    sys.exit(1)
            else:
                sys.exit(1)
        try:
            for item in module_obj.all_programs:
                if item.is_dir() and item.name != "__pycache__" and Path(item / "main.py").exists():
                    if item.name not in all_programsl:
                        item.copy(programs_dir / item.name)
                    all_programsl.append(item.name)
        except AttributeError:
            print(f"AttributeError: module '{module}' has no attribute 'all_programs' therefore it is outdated")
    all_programs = sorted(
        all_programsl,
        key=lambda x: (not x.isdigit(), int(x) if x.isdigit() else x)
    )
    return all_programs
