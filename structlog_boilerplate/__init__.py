import json
import logging
import sys

import structlog
from pygments import highlight, lexers, formatters


def colorize(payload: str):
    return highlight(payload, lexers.JsonLexer(), formatters.TerminalFormatter())


def to_json(payload: dict, pretty=False):
    payload.update(time_stamper(None, None, {}))
    if pretty:
        return colorize(json.dumps(payload, indent=1, sort_keys=True))
    else:
        return json.dumps(payload, sort_keys=True)


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


def strict(level=logging.ERROR):
    logging.basicConfig(format="%(message)s", stream=sys.stdout, level=level)


def colored(level=logging.ERROR):
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    root_logger.setLevel(level)
