"""clockdrift.py：时钟校正（基线：样本即时间）。"""
from __future__ import annotations


class ClockSync:
    def __init__(self, threshold: int = 10):
        self.threshold = threshold
        self.offset = 0
        self.last = None
        self.abnormal = 0
        self.samples = 0

    def observe(self, sample: int) -> dict:
        """基线：直接采用样本。"""
        self.offset = sample
        self.last = sample
        self.samples += 1
        return {"offset": self.offset, "abnormal": self.abnormal}

    def now(self) -> int:
        raise NotImplementedError("单调时钟还没实现")

    def persist(self) -> bytes:
        raise NotImplementedError("快照还没实现")

    def restore(self, blob: bytes = None) -> dict:
        raise NotImplementedError("重启恢复还没实现")

    def stats(self) -> dict:
        return {"offset": self.offset, "last": self.last, "abnormal": self.abnormal,
                "samples": self.samples, "threshold": self.threshold}
