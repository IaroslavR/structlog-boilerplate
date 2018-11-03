import logging
import time

logger = logging.getLogger(__name__)


def f():
    logger.fatal("Boom!!!!")
    logger.error("Bang!")
    logger.warning("Winter is coming %s", time.clock())
    logger.info("Knock, knock")
    logger.debug("Beer detected")
    try:
        1 / 0
    except Exception:
        logger.exception("Wow, exception")
