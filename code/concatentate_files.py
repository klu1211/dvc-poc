import click
import yaml 
from pathlib import Path

@click.command()
@click.option('--config_file_path')
def main(config_file_path):
    all_words = []
    with Path(config_file_path).open("r") as f:
        config = yaml.load(f)
    file_path = Path(config["FilePaths"]["input"])
    save_path = Path(config["FilePaths"]["save"])
    for path in file_path.glob("*"):
        with path.open("r") as f:
            for i, line in enumerate(f):
                print(f"Line {i} is: {line}!")
                all_words.append(line)
    all_words = " ".join(all_words)
    print(all_words)
    save_path.parent.mkdir(exist_ok=True, parents=True)
    with save_path.open("w") as f:
        f.write(all_words)

        

main()

