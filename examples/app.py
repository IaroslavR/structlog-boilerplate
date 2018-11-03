import logging

import click

from libs import sdt_lib
from libs import structlog_lib
from structlog_boilerplate import colored, strict, print_json


@click.command()
@click.option("-v", "--verbose", count=True)
def main(verbose: int) -> None:
    level = {0: logging.ERROR, 1: logging.INFO, 2: logging.DEBUG}
    verbose = min(verbose, 2)
    if verbose:
        colored(level[verbose])
    else:
        strict(level[verbose])
    sdt_lib.f()
    structlog_lib.f()
    print_json({"event": "result", "value": 42})


if __name__ == "__main__":
    main()
