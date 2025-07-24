from collections.abc import Callable
from typing import Any

startup_hooks: list[Callable[[], Any]] = []

def append_startup(func: Callable[[], Any]):
    global startup_hooks
    startup_hooks.append(func)
