"""Examples of imports."""

from lessons import helpers
# from __ package, importing what module?

from lessons import helpers as hp
# Import using an alias; helps with longer module names

from lessons.helpers import THE_ANSWER, powerful
# Import names directly from globals of a module


def main() -> None:
    print(helpers.powerful(2, 4))
    # Access the first import

    print(hp.THE_ANSWER)
    # Access the aliased import

    print(powerful(2, 10))
    print(THE_ANSWER)
    # Call the imported function directly

    print(f"imports.py: {__name__}")


if __name__ == "__main__":
    main()