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

    def formatTime(self, record, datefmt=None):
        # Only show time, no date, and remove last decimal (show milliseconds as 3 digits)
        ct = self.converter(record.created)
        t = "%02d:%02d:%02d" % (ct.tm_hour, ct.tm_min, ct.tm_sec)
        msecs = int(record.msecs)
        return f"{t}.{msecs:03d}"

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
    "%(asctime)s %(levelname)s | mod=%(name)s: msg=%(message)s",
    datefmt=None  # We'll override formatTime anyway
))
logging.basicConfig(
    level=logging.INFO,
    handlers=[handler]
)

logger = logging.getLogger(__name__)
logger.info("Core Initialized")