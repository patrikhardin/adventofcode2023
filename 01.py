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

def extract_numbers(text: str) -> str:
    numbers = {
        "one": "1", "two": "2", "three": "3",
        "four": "4", "five": "5", "six": "6",
        "seven": "7","eight": "8","nine": "9"
    }
    result = ""
    i = 0
    while i < len(text):
        for word, digit in numbers.items():
            if text[i:].startswith(word):
                result += digit
                i += 1
                break
        else:
            if text[i].isdigit():
                result += text[i]
            i += 1
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
        line_updated = extract_numbers(line)
        result_2 = find_first_number(line_updated) + find_first_number(line_updated[::-1])
        calibration_values_2.append(int(result_2))
        print(f"Line {i} : {line} Result : {result_1} Updated line : {line_updated} Updated result : {result_2}")
        
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
    