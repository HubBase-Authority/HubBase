from pathlib import Path
from .Database import JsonUser
from .Programs.Manager import Program
import importlib, sys


def get_all_progs() -> list:
    programs_dir = (Path(__file__).resolve().parent / "Programs")
    all_programs = programs_dir.iterdir()
    all_programsl = []

    for item in all_programs:
        if item.is_dir() and item.name != "__pycache__" and Path(item / "main.py").exists():
            all_programsl.append(item.name)

    all_programs = sorted(
        all_programsl,
        key=lambda x: (not x.isdigit(), int(x) if x.isdigit() else x)
    )

    return all_programs

def get_all_progsdata() -> dict[Path, dict]:
    programs_dir = (Path(__file__).resolve().parent / "Programs")
    all_programs = programs_dir.iterdir()
    all_programsd = {}
    project_root = Path(__file__).resolve().parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    for item in all_programs:
        if item.is_dir() and item.name != "__pycache__" and Path(item / "main.py").exists():
            md_module_name = f"Programs.{item.name}"
            metadata = {"loaded": False}
            try:
                md_module = importlib.import_module(md_module_name)
                metadata = md_module.ProgramInfo
            except (ImportError, AttributeError):
                pass
            all_programsd[item] = metadata

    return all_programsd


def run(id: int | str, user: User, *, name: str = "", source: Path | None = None, to_print: bool = False) -> tuple[bool, dict]:
    if name:
        for path, prog_md in get_all_progsdata().items():
            if prog_md.get("Name", "") == name:
                id = path.name
    try:
        prog = Program(id, source)
    except FileNotFoundError: return False, {"exited": True, "exit_type": FileNotFoundError}
    md: dict = {"exited": True, "exit_type": BaseException}
    try:
        results: tuple[bool, dict] = prog.run(user, to_print=to_print)
    except BaseException:
        results: tuple[bool, dict] = False, md
    return results
