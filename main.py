from stats import (
    generate_report_rows,
    get_book_text,
    get_number_characters,
    get_number_words,
)
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath: str = sys.argv[1]

    text: str = get_book_text(filepath)
    num_words: int = get_number_words(text)
    character_table: dict[str, int] = get_number_characters(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    report_rows: list[dict[str, int]] = generate_report_rows(character_table)

    for ch in report_rows:
        key, value = *ch.keys(), *ch.values()
        if str(key).isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
