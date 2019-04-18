import yaml
import click
from pathlib import Path

@click.command()
@click.option("--config_file_path")
def main(config_file_path):
    with Path(config_file_path).open("r") as f:
        config = yaml.load(f)
    file_path = Path(config["FilePaths"]["save"])
    for line in file_path.open("r"):
        print(line)

main()

