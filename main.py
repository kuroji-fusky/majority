from argparse import ArgumentParser


parser = ArgumentParser(
    description="Converts any media file straight out of 2000s YouTube Poops"
)

parser.add_argument("-vu", "--volume",
                    help="The output's volume", type=float)

parser.add_argument("-P", "--preset",
                    help="Gets the preset specified from presets.yml by default", type=str)

parser.add_argument("--preset-config",
                    help="Optional: Path to the preset config", type=float)

parser.add_argument("--no-preserve-metadata",
                    help="Strips any metadata from an input file. By default, FFmpeg preserves any metadata you input it with", type=bool)

parser.add_argument("-F", "--file-format",
                    help="The specified filename pattern when saving",
                    default="%fn%_gmajor",
                    type=str)

parser.add_argument("--no-auto-invert",
                    help="Disables automatically inverting the video")

args = parser.parse_args()


def main():
    pass


if __name__ == "__main__":
    main()
