import os
from pathlib import Path

TEXT = "I asked for a raise and got a pizza party. At this exchange rate I now own 0.3% of a pepperoni."


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT + "\n")


if __name__ == "__main__":
    main()
