import logging
import os
from logging.handlers import RotatingFileHandler
from src.utils.config import cfg


class LoggerConfigurator:
    def __init__(self):
        self.root_logger = logging.getLogger()
        self.root_logger.setLevel(self._get_level_from_string(cfg["logger"]["level"]))
        self._rotate: int = cfg["logger"]["rotate"]
        self._path: str = cfg["logger"]["path"]
        self._max_bytes: int = cfg["logger"]["max_bytes"]
        self._backup_count: int = cfg["logger"]["backup_count"]

    def _get_level_from_string(self, level_str):
        levels = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL,
        }
        return levels.get(level_str.upper(), logging.NOTSET)

    def _setup_formatter_full(self):
        return logging.Formatter(
            "%(asctime)s.%(msecs)03d] [%(levelname)-5s] [%(process)d] "
            "%(filename)s:%(lineno)d %(funcName)s() - %(message)s",
            datefmt="[%d-%m-%Y] [%H:%M:%S",
        )

    def _setup_formatter(self):
        return logging.Formatter("%(asctime)s %(levelname)-8s %(message)s")

    def _setup_handlers(self):
        handlers = []
        if self._rotate:
            if not os.path.exists(self._path):
                os.makedirs(self._path)
            log_handler = RotatingFileHandler(
                f"{self._path}/all_log.log",
                maxBytes=self._max_bytes,
                backupCount=self._backup_count,
            )
        else:
            log_handler = logging.FileHandler(
                f"{self._path}/all_log_{os.getpid()}.log", mode="w"
            )

        log_handler.setLevel(self._get_level_from_string(cfg["logger"]["level"]))
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(self._get_level_from_string(cfg["logger"]["level"]))
        if cfg["logger"]["format_full"]:
            log_handler.setFormatter(self._setup_formatter())
            stream_handler.setFormatter(self._setup_formatter())
        else:
            log_handler.setFormatter(self._setup_formatter_full())
            stream_handler.setFormatter(self._setup_formatter_full())

        handlers.append(log_handler)
        if cfg["logger"]["file_write"]:
            handlers.append(stream_handler)

        return handlers

    def configure(self):
        self.root_logger.handlers = self._setup_handlers()
