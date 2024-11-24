import argparse
import logging
import signal
import threading
import time

import coloredlogs

from hal_hw_emu.arcus import Arcus
from hal_hw_emu.pcb import PCB

logging.basicConfig(level=logging.DEBUG)
coloredlogs.install(
    level="DEBUG",
    fmt="[%(levelname)s] [%(name)s] %(message)s",
    field_styles={
        "asctime": {"color": "green"},
        "hostname": {"color": "magenta"},
        "levelname": {"bold": True, "color": "black"},
        "name": {"color": "green"},
        "programname": {"color": "cyan"},
        "username": {"color": "yellow"},
    },
    level_styles={
        "critical": {"bold": True, "color": "red"},
        "debug": {"faint": True},
        "error": {"color": "red"},
        "info": {},
        "notice": {"color": "magenta"},
        "spam": {"color": "green", "faint": True},
        "success": {"bold": True, "color": "green"},
        "verbose": {"color": "blue"},
        "warning": {"color": "yellow"},
    },
)

logger = logging.getLogger("Main")
arcus_instance = None
pcb_instance = None


def signal_handler(sig, frame):
    logger.info("Graceful shutdown initiated...")
    stop()


def main():
    global arcus_instance, pcb_instance

    arcus_instance = Arcus()
    pcb_instance = PCB()

    arcus_thread = threading.Thread(target=arcus_instance.start)
    pcb_thread = threading.Thread(target=pcb_instance.start)

    arcus_thread.start()
    pcb_thread.start()

    try:
        # Loop to keep the service alive while threads run
        while arcus_thread.is_alive() or pcb_thread.is_alive():
            time.sleep(0.5)
    except Exception as e:
        logger.error(f"Error in main loop: {e}")
    finally:
        # Join threads when the service stops
        arcus_thread.join()
        pcb_thread.join()
        logger.info("All connections closed. Exiting.")


def stop():
    logger.info("Service stop initiated...")
    # Stop the Arcus and PCB instances
    if arcus_instance:
        arcus_instance.stop()
    if pcb_instance:
        pcb_instance.stop()


if __name__ == "__main__":
    if hasattr(signal, "SIGINT"):
        signal.signal(signal.SIGINT, signal_handler)

    main()
