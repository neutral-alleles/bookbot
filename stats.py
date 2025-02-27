def get_number_words(text: str) -> int:
    return len(text.split())


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return "".join(f.readlines())


def get_number_characters(text: str) -> dict[str, int]:
    table: dict[str, int] = {}

    for character in text:
        lo_char = character.lower()
        table[lo_char] = table.get(lo_char, 0) + 1

    return table

def generate_report_rows(table: dict[str, int]) -> list[dict[str, int]]:

    rows: list[dict[str, int]] = [{ch: table[ch]} for ch in table]
    rows = sorted(rows, key=lambda x: list(x.values())[0])

    return rows


