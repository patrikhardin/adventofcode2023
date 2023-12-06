import time


def read_lines(file_path: str) -> list[str]:
    with open(file_path, encoding="utf-8") as f:
        lines = [line.rstrip() for line in f.readlines()]
    return lines


def find_first_number(text: str) -> str:
    """Finds the first number in a string an returns it"""
    for char in text:
        if char.isdigit():
            return char
    return ""

def parse_line(text: str, map_strings: bool) -> str:
    numbers_mapping = {
        "one": "1", "two": "2", "three": "3",
        "four": "4", "five": "5", "six": "6",
        "seven": "7","eight": "8","nine": "9"
    }
    result = ""
    for pos in range(len(text)):
        if text[pos].isdigit():
            result += text[pos]
        else:
            for word, digit in numbers_mapping.items():
                if text[pos:].startswith(word):
                    result += digit
    return result


def main(file_path: str):

    lines = read_lines(file_path)
    
    calibration_values_1 = []
    calibration_values_2 = []
    
    for i, line in enumerate(lines):
        
        # Part 1
        result_1 = find_first_number(line) + find_first_number(line[::-1])
        calibration_values_1.append(int(result_1))
        
        # Part 2
        parsed_line = parse_line(line, map_strings=True)
        result_2 = int(parsed_line[0] + parsed_line[-1])
    
        calibration_values_2.append(int(result_2))
        print(f"Line {i} : {line} Result : {result_1} Parsed line : {parsed_line} Updated result : {result_2}")
        
    ans_1 = sum(calibration_values_1)
    ans_2 = sum(calibration_values_2)

    return ans_1, ans_2
    

if __name__ == "__main__":
    start_time = time.time()
    ans_1, ans_2 = main("data/01.txt")
    elapsed = time.time() - start_time
    
    print(f"Ans 1 : {ans_1}")
    print(f"Ans 2 : {ans_2}")
    print(f"Elapsed : {elapsed*1000:.3f}ms")
    