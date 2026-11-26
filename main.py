"""Fortune Cookie Funnies for Engineers (make.fun bounty
u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a).

Writes one fortune cookie message for a software engineer to
/output/entry.txt. Gate: UTF-8, 1-120 characters, a single line,
not only whitespace.
"""

import os

LINE = "Your pager will stay silent tonight. It is lying."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
