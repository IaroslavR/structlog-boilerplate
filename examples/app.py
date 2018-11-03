import logging

import click

from libs import sdt_lib
from libs import structlog_lib
from structlog_boilerplate import colored, strict, to_json


@click.command()
@click.option("-v", "--verbose", count=True)
def main(verbose):
    level = {0: logging.ERROR, 1: logging.INFO, 2: logging.DEBUG}
    verbose = min(verbose, 2)
    if verbose:
        colored(level[verbose])
    else:
        strict(level[verbose])
    sdt_lib.f()
    structlog_lib.f()
    print(to_json({"event": "result", "value": 42}, pretty=bool(verbose)))


if __name__ == "__main__":
    main()
