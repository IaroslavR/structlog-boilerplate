import json
import logging
import sys

import structlog

# noinspection PyPackageRequirements
from pygments import highlight, lexers, formatters

STRICT = True


def colorize(payload: str) -> str:
    return highlight(payload, lexers.JsonLexer(), formatters.TerminalFormatter())


def print_json(payload: dict, echo=True) -> str:
    payload.update(time_stamper(None, None, {}))
    if STRICT:
        as_str = json.dumps(payload, sort_keys=True)
    else:
        as_str = colorize(json.dumps(payload, indent=1, sort_keys=True))
    if echo:
        print(as_str)
    return as_str


time_stamper = structlog.processors.TimeStamper(fmt="iso")

shared_processors = [
    structlog.stdlib.add_logger_name,
    structlog.stdlib.add_log_level,
    structlog.stdlib.PositionalArgumentsFormatter(),
    time_stamper,
    structlog.processors.StackInfoRenderer(),
    structlog.processors.format_exc_info,
    structlog.processors.UnicodeDecoder(),
]

structlog.configure(
    processors=shared_processors
    + [structlog.stdlib.ProcessorFormatter.wrap_for_formatter],
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

formatter = structlog.stdlib.ProcessorFormatter(
    processor=structlog.dev.ConsoleRenderer(), foreign_pre_chain=shared_processors
)


def strict(level=logging.ERROR) -> None:
    logging.basicConfig(format="%(message)s", stream=sys.stdout, level=level)
    global STRICT
    STRICT = True


def colored(level=logging.ERROR) -> None:
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    root_logger.setLevel(level)
    global STRICT
    STRICT = False
