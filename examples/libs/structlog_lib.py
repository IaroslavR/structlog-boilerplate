import time

import structlog

log = structlog.get_logger()


def f():
    log.critical("Boom!!!!")
    log.error("Bang!")
    log.warning("Winter is coming", then=time.clock())
    log.info("Knock, knock")
    log.debug("Beer detected")
    try:
        1 / 0
    except Exception:
        log.exception("Wow, exception")
