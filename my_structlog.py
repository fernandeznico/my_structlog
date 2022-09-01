import logging
from inspect import getframeinfo, stack
from types import FrameType
from typing import cast

import structlog
from structlog.dev import ConsoleRenderer

my_structlog = structlog


class FileNameRenderer(object):
    def __init__(self, stack_depth):
        self._stack_depth = stack_depth

    def __call__(self, logger, name, event_dict):
        caller = getframeinfo(cast(FrameType, stack()[self._stack_depth][0]))
        event_dict["file_name"] = f"{caller.filename}:{caller.lineno}"
        return event_dict


logging.basicConfig(level=logging.DEBUG, format="")

structlog.configure(
    processors=[
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M.%S"),
        structlog.processors.StackInfoRenderer(),
        FileNameRenderer(stack_depth=4),
        structlog.dev.ConsoleRenderer(level_styles=ConsoleRenderer.get_default_level_styles()),
    ],
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)
