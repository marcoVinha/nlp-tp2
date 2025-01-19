from rich.console import Console
from rich.markdown import Markdown


def main():
    console = Console()

    with open("README.md") as readme_file:
        md = Markdown(readme_file.read())
        console.print(md)


if __name__ == "__main__":
    main()
