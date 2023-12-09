from pathlib import Path

from aoc_2023.day2.day2 import Day2PuzzleSolver
from aoc_2023.utils import PUZZLE_VARIANT

TEST_PUZZLE_INPUT = (
    Path(__file__).parent.absolute().joinpath("test_day2_puzzle_input.txt")
)

TEST_PUZZLE_PART_1_SOLUTION = 8
TEST_PUZZLE_PART_2_SOLUTION = 2286


def test_solve_part_1():
    solver = Day2PuzzleSolver(TEST_PUZZLE_INPUT)
    solver.solve()
    assert solver.solution == TEST_PUZZLE_PART_1_SOLUTION


def test_solve_part_2():
    solver = Day2PuzzleSolver(TEST_PUZZLE_INPUT, puzzle_variant=PUZZLE_VARIANT.PART2)
    solver.solve()
    assert solver.solution == TEST_PUZZLE_PART_2_SOLUTION
