import click
import yaml 
from pathlib import Path

@click.command()
@click.option('--config_file_path')
def main(config_file_path):
    with Path(config_file_path).open("r") as f:
        config = yaml.load(f)
    file_path = Path(config["FilePaths"]["input"])
    for path in file_path.glob("*"):
        with path.open("r") as f:
            for i, line in enumerate(f):
                print(f"Line {i} is: {line}!")

main()

