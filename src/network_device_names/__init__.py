# devices = [
#     0"DesktopPC-icon.svg",
#     1"Laptop-Icon.svg",
#     2"Mobile-icon.svg",
#     3"Tablet-icon.svg",
#     4"Printer-icon.svg",
#     5"Unknown-device.svg"
# ]
import csv
import typing
import urllib.parse
from pathlib import Path

from . import config


def _get_device_names() -> typing.Generator:
    devices_csv_path = Path.cwd() / "devices.csv"
    with devices_csv_path.open(mode="r") as csv_content:
        reader = csv.DictReader(f=csv_content)
        yield from reader


def _name_network_device(device: typing.Dict):
    import requests
    data = urllib.parse.quote_plus(
        string=f'assocDevData={{"FriendlyName":"{device["FriendlyName"]}","MACAddress":"{device["MACAddress"]}"}}&opType=WRITE',
        safe="=&"
    )
    response = requests.post(
        url=config.url,
        data=data,
        headers={
            **config.headers,
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,nl;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'DNT': '1',
            'Origin': 'http://192.168.178.1',
            'Pragma': 'no-cache',
            'Referer': 'http://192.168.178.1/?home&mid=Home',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        },
    )
    response.raise_for_status()

    if response.text.strip() == "0":
        raise Exception("Check your configuration")

    print(f"{device['FriendlyName']} configured with MAC {device['MACAddress']}")


def run():
    devices = _get_device_names()
    for device in devices:
        _name_network_device(device=device)


if __name__ == "__main__":
    run()
