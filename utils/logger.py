import logging
import sys
from datetime import datetime
from logging import Logger
from logging.handlers import RotatingFileHandler
from pathlib import Path


class ComposeLogger:

    def __init__(self, log_dir: str = "logs") -> None:
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)

        # 创建logger
        self.logger = logging.getLogger("TTS")
        # 避免日志重复
        self.logger.propagate = False
        self.logger.setLevel(logging.DEBUG)

        # 避免重复添加handler
        if not self.logger.handlers:
            self._setup_handlers()

    def _setup_handlers(self) -> None:
        """设置日志处理器"""
        # 清除现有的handlers
        self.logger.handlers.clear()

        # 控制台处理器
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_format = logging.Formatter(
            "%(asctime)s - %(levelname)s: %(message)s", datefmt="%H:%M:%S"
        )
        console_handler.setFormatter(console_format)

        # 文件处理器
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file = self.log_dir / f"composer{current_time}.log"
        file_handler = RotatingFileHandler(
            self.log_file,
            maxBytes=10 * 1024 * 1024,
            backupCount=5,
            encoding="utf-8",  # 10MB
        )
        file_handler.setLevel(logging.DEBUG)
        file_format = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - "
            "%(filename)s:%(lineno)d - %(message)s"
        )
        file_handler.setFormatter(file_format)

        # 添加处理器
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    def get_logger(self) -> Logger:
        """获取logger实例"""
        return self.logger


# 创建全局logger实例
compose_logger_instance = ComposeLogger()
logger = compose_logger_instance.get_logger()
