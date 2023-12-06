
import time


def read_lines(file_path: str) -> list[str]:
    with open(file_path, encoding="utf-8") as f:
        lines = [line.rstrip() for line in f.readlines()]
    return lines


class Game:
    def __init__(self, game_string) -> None:
        game_id, game_data = game_string.split(": ")
        self.game_id = int(game_id.split(" ")[1])
        self.game_data = game_data
        
        self.is_possible = self.check_if_possible()
        self.min_cubes = self.calc_min_cubes()
        self.power = self.min_cubes["red"] * self.min_cubes["blue"] * self.min_cubes["green"]
        
    def check_if_possible(self, max_red: int = 12, max_green: int  = 13, max_blue: int = 14) -> bool:
        for draw in self.game_data.split("; "):
            color_dict = {"red": 0 , "green": 0, "blue": 0}
            for color_count in draw.split(", "):
                count, color = color_count.split(" ")
                color_dict[color] += int(count)
            if color_dict["red"] > max_red or color_dict["blue"] > max_blue or color_dict["green"] > max_green:
                return False
        return True

    def calc_min_cubes(self) -> dict[str, int]:
        max_color_dict = {"red": 0 , "green": 0, "blue": 0}
        for draw in self.game_data.split("; "):
            for color_count in draw.split(", "):
                count, color = color_count.split(" ")
                max_color_dict[color] = max(int(count), max_color_dict[color])
        return max_color_dict


def main(file_path):
    lines = read_lines(file_path)
    games = [Game(line) for line in lines]
    ans_1 = sum([game.game_id for game in games if game.is_possible])
    ans_2 = sum([game.power for game in games])
    return ans_1, ans_2
    
    
if __name__ == "__main__":
    ans_1_test, ans_2_test = main("data/02_test.txt")
    assert ans_1_test == 8
    assert ans_2_test == 2286
    
    start_time = time.time()
    ans_1, ans_2 = main("data/02.txt")
    elapsed = time.time() - start_time
    
    print(f"Ans 1 : {ans_1}")
    print(f"Ans 2 : {ans_2}")
    print(f"Elapsed : {elapsed*1000:.3f}ms")
    