from typing import Callable, Dict, Type

from audsync.synchronizer import Synchronizer

SYNCHRONIZERS: Dict[str, Synchronizer] = {}


def register(name: str) -> Callable[[Synchronizer], Synchronizer]:
    def decorator_fn(cls: Synchronizer) -> Synchronizer:
        pass


def get_synchronizer(name: str) -> Synchronizer:
    return SYNCHRONIZERS[name]
