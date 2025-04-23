"""Acquire, decode, normalize and store ADS-B data with dump1090, pyModeS and MariaDB."""

import pyModeS as pms
from pyModeS.extra.tcpclient import TcpClient


class ADSBClient(TcpClient):
    """Custom pyModeS TcpClient for ADS-B messages."""

    def __init__(self, host, port, datatype):
        """Initialize ADSBClient object.

        @params
            host (str): TCP host, either an IP
                or 'localhost'
            port (int): The TCP port to connect
                to.
            datatype (str): The datatype of the
                output, must be in ["raw", "beast",
                "skysense"]
        """
        super(ADSBClient, self).__init__(host, port, datatype)

    def handle_messages(self, messages):
        """Handle the decoded messaged received.

        @params
            msg: ADS-B decoded by pyModeS
        """
        for msg, timestamp in messages:
            # invalid data length (1 even (112b), 1 odd (112b) = 224b = 28B)
            if len(msg) != 28:
                continue

            # ADS-B downlink format is 17
            if pms.df(msg) != 17:
                continue

            # message does not pass cyclic redundancy check (i.e. corrupted)
            if pms.crc(msg) != 0:
                continue

            process_message(msg)


def process_message(msg):
    """Process a verified ADS-B message.

    @params
        msg: ADS-B decoded by pyModeS
    """
    ...
