# logger.py
import logging
from contextvars import ContextVar

# ContextVar for run_id (safe across async/threaded contexts)
# _run_id_ctx: ContextVar[str] = ContextVar("run_id", default="unknown")
_run_id_ctx = "unknowm"

def set_run_id(run_id: str):
    _run_id_ctx.set(run_id)
    # global _run_id_ctx 
    # _run_id_ctx = run_id

def get_run_id() -> str:
    # global _run_id_ctx
    # return _run_id_ctx
    return _run_id_ctx.get()


class RunIDFormatter(logging.Formatter):
    def format(self, record):
        record.run_id = get_run_id()
        return super().format(record)

def get_logger(name: str = __name__) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = RunIDFormatter('[%(run_id)s] %(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False
    return logger
