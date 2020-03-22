import logging


def setup_logging(level=logging.INFO):
    """Setup logging configuration"""
    logging_config = dict(
        version=1,
        disable_existing_loggers=False,
        formatters={
            "simple": {
                "format": "%(asctime)s %(levelname)s %(name)s: %(message)s",
                "datefmt": "%y/%m/%d %H:%M:%S",
            }
        },
        handlers={
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "stream": "ext://sys.stdout",
            }
        },
        root={"level": "DEBUG", "handlers": ["console"],},
    )

    try:
        config = logging_config.copy()
        config["root"]["level"] = level
        logging.config.dictConfig(config)

        logger = logging.getLogger(__name__)
        logger.info("Log set-up successful.")
    except Exception as e:
        logging.basicConfig(level=level)
        logger = logging.getLogger(__name__)
        logger.error(
            "Error occurred while attempting to configure logging", exc_info=True
        )
