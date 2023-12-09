from abc import ABC, abstractmethod
from enum import Enum
from typing import List


def read_file(file_path: str) -> List[str]:
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]
        return lines


PUZZLE_VARIANT = Enum("PuzzleVariant", "PART1 PART2")


class PuzzleSolver(ABC):
    def __init__(
        self, puzzle_input_file_path: str, puzzle_variant=PUZZLE_VARIANT.PART1
    ):
        self.puzzle_data = read_file(puzzle_input_file_path)
        self.solution = None
        self.puzzle_variant = puzzle_variant

    @abstractmethod
    def solve(self):
        ...
