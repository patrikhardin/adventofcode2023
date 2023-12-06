import re
import time


def read_lines(file_path: str) -> list[str]:
    with open(file_path, encoding="utf-8") as f:
        lines = [line.rstrip() for line in f.readlines()]
    return lines

class EngineSchematic:
    def __init__(self, schematic_lines: list[str]):
        self.schematic_lines = schematic_lines
        self.numbers = self.find_numbers()
        self.part_numbers = self.find_part_numbers()
        self.sum_of_part_numbers = sum([int(num) for num in self.part_numbers])
        
    def find_numbers(self) -> list[tuple[int, list[tuple[int, int]]]]:
        numbers = []
        for y, row_items in enumerate(self.schematic_lines):
            for m in re.finditer(r"\d+", row_items):
                numbers.append((int(m.group()), [(x, y) for x in range(m.start(), m.start() + len(m.group()))]))
        return numbers

    def find_part_numbers(self) -> list[int]:
        part_numbers = []
        neighbour_offsets = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if not (i == 0 and j == 0)]
        for number, positions in self.numbers:
            checked_neighbours = set()  # Keep track of checked neighbours for this number
            for position in positions:
                x, y = position
                for dx, dy in neighbour_offsets:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) not in checked_neighbours:  # Check if this neighbour has not been checked before
                        if 0 <= nx < len(self.schematic_lines[0]) and 0 <= ny < len(self.schematic_lines) and (nx, ny) not in positions:  # Check that the neighbour is within the grid and not another point of the number
                            if self.schematic_lines[ny][nx] != ".":
                                part_numbers.append(number)
                            checked_neighbours.add((nx, ny))  # Add this neighbour to the checked neighbours
        return part_numbers


def main(file_path):
    schematic_lines = read_lines(file_path)
    
    # Part 1
    engine_schematic = EngineSchematic(schematic_lines)
    
    # Part 2
    
    return engine_schematic.sum_of_part_numbers, None


    
if __name__ == "__main__":
    ans_1_test, ans_2_test = main("data/03_test.txt")
    assert ans_1_test == 4361
    
    start_time = time.time()
    ans_1, ans_2 = main("data/03.txt")
    elapsed = time.time() - start_time
    
    print(f"Ans 1 : {ans_1}")
    print(f"Ans 2 : {ans_2}")
    print(f"Elapsed : {elapsed*1000:.3f}ms")
    