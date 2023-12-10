from pathlib import Path
from typing import List

from aoc_2023.utils import PUZZLE_VARIANT, PuzzleSolver

PUZZLE_INPUT = str(Path(__file__).parent.absolute().joinpath("day4_puzzle_input.txt"))


class Day4PuzzleSolver(PuzzleSolver):
    @staticmethod
    def __extract_card_info(card: str) -> tuple[int, List[str], List[str]]:
        card_name, card_numbers = card.split(":")
        card_id = card_name.split()[-1]

        if not card_id.isdigit():
            raise ValueError(f"Invalid card id: {card_id}")

        winning_numbers, possessed_numbers = card_numbers.split("|")

        return int(card_id), winning_numbers.split(), possessed_numbers.split()

    @staticmethod
    def __get_card_matching_numbers_count(winning_numbers, possessed_numbers):
        possessed_winning_numbers = [
            number for number in possessed_numbers if number in winning_numbers
        ]

        possessed_winning_numbers_count = len(possessed_winning_numbers)
        return possessed_winning_numbers_count

    @staticmethod
    def __get_card_score(
        winning_numbers: List[str], possessed_numbers: List[str]
    ) -> int:
        matching_numbers_count = Day4PuzzleSolver.__get_card_matching_numbers_count(
            winning_numbers, possessed_numbers
        )

        return pow(2, matching_numbers_count - 1) if matching_numbers_count else 0

    def solve_part_1(self):
        sum_of_scratch_cards_scores = 0

        for card in self.puzzle_data:
            (
                _,
                winning_numbers,
                possessed_numbers,
            ) = Day4PuzzleSolver.__extract_card_info(card)

            sum_of_scratch_cards_scores += Day4PuzzleSolver.__get_card_score(
                winning_numbers, possessed_numbers
            )

        self.solution = sum_of_scratch_cards_scores

    def solve_part_2(self):
        all_cards_count = len(self.puzzle_data)
        card_clones_tracker = all_cards_count * [0]

        for card_idx, card in enumerate(self.puzzle_data):
            (
                _,
                winning_numbers,
                possessed_numbers,
            ) = Day4PuzzleSolver.__extract_card_info(card)

            card_matching_numbers_count = (
                Day4PuzzleSolver.__get_card_matching_numbers_count(
                    winning_numbers, possessed_numbers
                )
            )

            if card_matching_numbers_count == 0:
                continue

            card_clone_count = card_clones_tracker[card_idx]
            card_score_bump = card_clone_count + 1

            card_clones_won_range = range(
                card_idx + 1,
                min(card_idx + card_matching_numbers_count + 1, all_cards_count),
            )

            for card_clone_won_idx in card_clones_won_range:
                card_clones_tracker[card_clone_won_idx] += card_score_bump

        scratch_cards_won_count = sum(card_clones_tracker) + all_cards_count
        self.solution = scratch_cards_won_count

    def solve(self):
        if self.puzzle_variant == PUZZLE_VARIANT.PART1:
            self.solve_part_1()
        else:
            self.solve_part_2()


if __name__ == "__main__":
    puzzle_solver = Day4PuzzleSolver(PUZZLE_INPUT, puzzle_variant=PUZZLE_VARIANT.PART2)
    puzzle_solver.solve()
    print(puzzle_solver.solution)
