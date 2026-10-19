import importlib, sys, inspect
from pathlib import Path
from typing import Callable
from ..Database import User


def print_ImportError(error: BaseException, module_name: str, message: str | None=None):
    if message:
        raise Exception(f"[HubBase Engine] {message}")
    else:
        raise ImportError(f"[HubBase Engine] Failed to import {module_name}: {error}")


class Program:
    def __init__(self, id: int | str, source: None | Path = None):
        self.id = str(id)
        self.project_root = Path(__file__).resolve().parent.parent if source is None else source
        if str(self.project_root) not in sys.path:
            sys.path.insert(0, str(self.project_root))
        self.program_dir = self.project_root / "Programs" / self.id
        self.path = self.program_dir / "main.py"
        if not self.path.exists():
            raise FileNotFoundError(f"[HubBase Engine] Programs.{self.id}.main not found")

    def load(self, user: User) -> tuple[Callable, list, dict]:
        module_name = f"Programs.{self.id}.main"
        md_module_name = f"Programs.{self.id}"
        metadata = {"loaded": False}
        try:
            module = importlib.import_module(module_name)
            try:
                md_module = importlib.import_module(md_module_name)
                metadata = md_module.ProgramInfo
            except (AttributeError, ImportError):
                metadata = {"loaded": False}
            args = []
            if "user" in inspect.signature(module.run).parameters.keys():
                args.append(user)
            return module.run, args, metadata
        except ImportError as e:
            return print_ImportError, [e, module_name], metadata
        except AttributeError as e:
            return print_ImportError, [e, module_name, f"[HubBase Engine] {module_name} doesn`t have a `run()` method. "], metadata

    def run(self, user: User, *, to_print: bool = True) -> tuple[bool, dict]:
        metadata: dict = {"loaded": False}
        try:
            to_run, args, metadata = self.load(user)
            if to_print: print(f"[HubBase Engine] Launching", self.info(metadata))
            to_run(*args)
            return True, metadata
        except Exception as e:
            if to_print: print(f"[HubBase Engine] Failed to run program №{self.id}: {e}")
            return False, metadata
        except SystemExit as e:
            if to_print: print(f"Program {self.id} caught a SystemExit. Continuing...")
            metadata["exit_code"] = e.code
            metadata["exited"] = True
            metadata["exit_type"] = SystemExit
            return False, metadata

    def info(self, metadata: dict, *, extra: bool = False, titled: bool = False, indent: int = 2) -> str:
        p = "P" if titled else "p"
        if extra:
            ind: str = ' ' * indent
            return (f"{p}rogram №{self.id}: \n" +
                f"{ind}Name - {metadata.get('Name', '')} " +
                f"v{metadata.get('Version', '')} \n" if metadata.get("Version") is not None else "\n" +
                f"{ind}Built on v{metadata.get('Build', '')}")
        else:
            return f"{p}rogram №{self.id} - {metadata.get('Name', '')}"
