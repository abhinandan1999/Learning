import asyncio
import time
from logging_utils import get_logger, set_run_id
logging = get_logger(__name__)

from test_1 import test_1
from test_2 import test_2

async def main(id: str):
    # logging.info("pre set main")
    set_run_id(id)
    logging.info("main")
    test_1()
    await asyncio.sleep(5)
    test_2()

async def run_all():
    await asyncio.gather(main("A"), main("B"))

if __name__ == "__main__":
    asyncio.run(run_all())
