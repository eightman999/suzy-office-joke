import os
from pathlib import Path

TEXT = "My boss said 'let's circle back,' so I have been walking in a circle since March and my step count is incredible."


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT + "\n")


if __name__ == "__main__":
    main()
