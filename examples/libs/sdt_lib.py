import logging

logger = logging.getLogger(__name__)


def f():
    advent = "2018-11-01 00:00:01"
    logger.fatal("Boom!!!! advent=%s", advent)
    logger.error("Bang! advent=%s", advent)
    logger.warning("Winter is coming, advent=%s", advent)
    logger.info("Knock, knock advent=%s", advent)
    logger.debug("Beer detected  advent=%s", advent)
    try:
        1 / 0
    except Exception:
        logger.exception("Wow, exception  advent=%s", advent)
