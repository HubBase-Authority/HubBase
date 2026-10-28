from pathlib import Path
from .Programs import all_programs
from .Database import JsonUser, User
from .Programs.Manager import Program
import importlib, sys


def get_all_progs() -> list:
    return list(all_programs)

def get_all_progsdata(source: Path | None = None) -> dict[Path, dict]:
    project_root = source or Path(__file__).resolve().parent
    programs_dir = project_root / "Programs"
    all_programs = programs_dir.iterdir()
    all_programsd = {}
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    for item in all_programs:
        if item.is_dir() and item.name != "__pycache__" and Path(item / "main.py").exists():
            md_module_name = f"Programs.{item.name}"
            metadata = {"loaded": False}
            try:
                md_module = importlib.import_module(md_module_name)
                metadata = md_module.ProgramInfo
            except Exception:
                pass
            all_programsd[item] = metadata

    return all_programsd


def run(id: int | str, user: User, *, name: str = "", source: Path | None = None, to_print: bool = False) -> tuple[bool, dict]:
    if name:
        for path, prog_md in get_all_progsdata(source).items():
            if prog_md.get("Name", "").lower().replace(" ", "-") == name.lower().replace(" ", "-"):
                id = path.name
                break
        else:
            return False, {"name_found": False}
    try:
        prog = Program(id, source)
    except FileNotFoundError: return False, {"exited": True, "exit_type": FileNotFoundError}
    md: dict = {"exited": True, "exit_type": BaseException}
    try:
        results: tuple[bool, dict] = prog.run(user, to_print=to_print)
    except BaseException:
        results: tuple[bool, dict] = False, md
    return results
