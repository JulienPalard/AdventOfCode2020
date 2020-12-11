from pathlib import Path


def seat_code_reader(seat_code):
    row = int(seat_code[:7].replace("F", "0").replace("B", "1"), 2)
    column = int(seat_code[7:].replace("R", "1").replace("L", "0"), 2)
    seat_id = row * 8 + column
    return row, column, seat_id


def seat_id(seat_code):
    return seat_code_reader(seat_code)[2]


highest_seat = max(Path("day5.txt").read_text().split(), key=seat_id)
print("Highest seat id:", seat_id(highest_seat))

known_seat_ids = {seat_id(seat) for seat in Path("day5.txt").read_text().split()}
print("Missing seats:")
print(set(range(seat_id(highest_seat))) - known_seat_ids)
