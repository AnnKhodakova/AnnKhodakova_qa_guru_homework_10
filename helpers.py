from pathlib import Path


def path(file_name) -> Path:
    return Path(__file__).parent.joinpath(f'tests/picture/{file_name}')
