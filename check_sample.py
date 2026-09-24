"""check_sample.py：按 sample/samples.json 走一圈，打印验收面。"""
import json
import os
import sys

from clockdrift import ClockSync


def main() -> int:
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join("sample", "samples.json")
    with open(path, encoding="utf-8") as handle:
        spec = json.load(handle)
    sync = ClockSync(spec["threshold"])
    offsets = []
    jumps = []
    for sample in spec["samples"]:
        before = sync.stats()["abnormal"]
        offsets.append(sync.observe(sample)["offset"])
        if sync.stats()["abnormal"] > before:
            jumps.append(sample)
    nows = [sync.now() for _ in range(spec["reads"])]
    blob = sync.persist()
    reborn = ClockSync(spec["threshold"])
    restored = reborn.restore(blob)
    print("偏移估计序列 =", offsets)
    print("被判定为跳变的样本 =", jumps)
    print("单调时钟读数 =", nows)
    print("样本数 =", sync.stats().get("samples"))
    print("恢复后的偏移 =", restored.get("offset"))
    print("恢复后的跳变计数 =", restored.get("abnormal"))
    print("跳变阈值 =", spec["threshold"])
    print("不变量（单调不回退） =", spec["monotonic_invariant"])
    print("读取次数 =", spec["reads"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
