import structlog

logger = structlog.get_logger()


def f():
    advent = "2018-11-01 00:00:01"
    log = logger.bind(advent=advent)
    log.critical("Boom!!!!")
    log.error("Bang!")
    log.warning("Winter is coming")
    log.info("Knock, knock")
    log.debug("Beer detected")
    try:
        1 / 0
    except Exception:
        log.exception("Wow, exception")
