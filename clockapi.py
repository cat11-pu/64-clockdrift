"""clockapi.py：对外门面（老接口 observe 不能改）。"""
from __future__ import annotations

from clockdrift import ClockSync


class Clock:
    def __init__(self, threshold: int = 10):
        self.sync = ClockSync(threshold)

    def observe(self, sample: int) -> dict:
        return self.sync.observe(sample)

    def now(self) -> int:
        return self.sync.now()

    def snapshot(self) -> bytes:
        return self.sync.persist()

    def rebuild(self, blob: bytes = None) -> dict:
        return self.sync.restore(blob)
