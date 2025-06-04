import logging 

class ColorFormatter(logging.Formatter):
    COLORS = {
        'INFO': '\033[92m',    # Green
        'ERROR': '\033[91m',   # Red
        'WARNING': '\033[93m', # Yellow
        'DEBUG': '\033[94m',   # Blue
        'CRITICAL': '\033[95m',# Magenta
    }
    RESET = '\033[0m'

    def format(self, record):
        # Save the original levelname
        original_levelname = record.levelname
        color = self.COLORS.get(record.levelname, '')
        reset = self.RESET if color else ''
        # Color only the levelname
        if color:
            record.levelname = f"{color}{record.levelname}{reset}"
        msg = super().format(record)
        # Restore the original levelname to avoid side effects
        record.levelname = original_levelname
        return msg

handler = logging.StreamHandler()
handler.setFormatter(ColorFormatter(
    "%(asctime)s [%(levelname)s] MODULE=%(name)s: MSG=%(message)s"
))
logging.basicConfig(
    level=logging.INFO,
    handlers=[handler]
)

logger = logging.getLogger(__name__)
logger.info("Core Initialized")