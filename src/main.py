import src.custom_math as math
import src.custom_strings as strings
import random
import time


def simulate_calculations():
    print("Starting math operations...\n")
    for _ in range(5):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        print(f"Add: {a} + {b} = {math.add(a, b)}")
        print(f"Subtract: {a} - {b} = {math.subtract(a, b)}")
        print(f"Multiply: {a} * {b} = {math.multiply(a, b)}")
        print(f"Divide: {a} / {b} = {math.divide(a, b):.2f}")
        print("-" * 40)
        time.sleep(0.5)


def simulate_string_ops():
    print("Starting string operations...\n")
    examples = ["Hello World", "Python is great!", "Testing 123", "    spaced out   ", "UPPER lower"]
    for s in examples:
        print(f"Original: '{s}'")
        print(f"Upper: '{strings.to_upper(s)}'")
        print(f"Lower: '{strings.to_lower(s)}'")
        print(f"Capitalize: '{strings.capitalize_words(s)}'")
        print(f"Reversed: '{strings.reverse_string(s)}'")
        print(f"Stripped: '{strings.strip_spaces(s)}'")
        print("-" * 40)
        time.sleep(0.5)


def main():
    print("=" * 50)
    print("== Dummy Python Repo Demo ==")
    print("=" * 50)
    simulate_calculations()
    simulate_string_ops()
    print("Done!")


if __name__ == "__main__":
    main()
