"""Paper-facing binary detection metrics.

Labels use 1 for malicious and 0 for benign. These helpers match the
headline names used in the public benchmark write-up: Macro-F1,
malicious recall, and benign false-positive rate.
"""

from __future__ import annotations

from typing import Iterable


def _pairs(y_true: Iterable[int], y_pred: Iterable[int]) -> list[tuple[int, int]]:
    pairs = [(int(a), int(b)) for a, b in zip(y_true, y_pred)]
    if not pairs:
        raise ValueError("y_true and y_pred are empty")
    return pairs


def confusion(y_true: Iterable[int], y_pred: Iterable[int]) -> dict[str, int]:
    tp = fp = tn = fn = 0
    for truth, pred in _pairs(y_true, y_pred):
        if truth == 1 and pred == 1:
            tp += 1
        elif truth == 0 and pred == 1:
            fp += 1
        elif truth == 0 and pred == 0:
            tn += 1
        elif truth == 1 and pred == 0:
            fn += 1
        else:
            raise ValueError(f"labels must be 0 or 1, got {(truth, pred)}")
    return {"tp": tp, "fp": fp, "tn": tn, "fn": fn}


def accuracy(y_true: Iterable[int], y_pred: Iterable[int]) -> float:
    pairs = _pairs(y_true, y_pred)
    return sum(a == b for a, b in pairs) / len(pairs)


def _f1(precision: float, recall: float) -> float:
    if precision + recall == 0:
        return 0.0
    return 2 * precision * recall / (precision + recall)


def malicious_recall(y_true: Iterable[int], y_pred: Iterable[int]) -> float:
    counts = confusion(y_true, y_pred)
    denom = counts["tp"] + counts["fn"]
    return 0.0 if denom == 0 else counts["tp"] / denom


def benign_fpr(y_true: Iterable[int], y_pred: Iterable[int]) -> float:
    counts = confusion(y_true, y_pred)
    denom = counts["fp"] + counts["tn"]
    return 0.0 if denom == 0 else counts["fp"] / denom


def macro_f1(y_true: Iterable[int], y_pred: Iterable[int]) -> float:
    counts = confusion(y_true, y_pred)
    mal_p_denom = counts["tp"] + counts["fp"]
    mal_r_denom = counts["tp"] + counts["fn"]
    ben_p_denom = counts["tn"] + counts["fn"]
    ben_r_denom = counts["tn"] + counts["fp"]
    mal_p = 0.0 if mal_p_denom == 0 else counts["tp"] / mal_p_denom
    mal_r = 0.0 if mal_r_denom == 0 else counts["tp"] / mal_r_denom
    ben_p = 0.0 if ben_p_denom == 0 else counts["tn"] / ben_p_denom
    ben_r = 0.0 if ben_r_denom == 0 else counts["tn"] / ben_r_denom
    return (_f1(mal_p, mal_r) + _f1(ben_p, ben_r)) / 2


def detection_metrics(y_true: Iterable[int], y_pred: Iterable[int]) -> dict[str, float]:
    return {
        "accuracy": accuracy(y_true, y_pred),
        "macro_f1": macro_f1(y_true, y_pred),
        "malicious_recall": malicious_recall(y_true, y_pred),
        "benign_fpr": benign_fpr(y_true, y_pred),
        **confusion(y_true, y_pred),
    }
