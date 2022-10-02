# Ziggo Network Device Names
## Prerequisites
- Ziggo as your ISP 😞 (Dutch ISP)
- A Ziggo modem (i.e. ConnectBox Giga)
- [Python 3.8+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/)

## How to use:
1. Login to your Ziggo modem
2. Open the (Chrome) Devtools
3. Open the Network tab in the (Chrome) DevTools
4. Copy the Cookie request header to `config.example.py` (`src/network_device_names/config.example.py`)
5. Copy the csrf_nonce request header to `config.example.py`
6. Rename `config.example.py` to `config.py`
7. Rename `devices.example.py` to `devices.py`
8. Fill in `devices.py` by entering your device's MAC address and name seperated by a comma, 1 line for each device
9. Install [Poetry](https://python-poetry.org/docs/)
10. Run `poetry install`
11. Run `poetry run python -m network_device_names`

Tested on ConnectBox Giga

## Why?
Ziggo delivered a web interface that lacks basic functionality and is littered with bugs.
They don't care at all about these bugs and haven't fixed them even though the bugs have 
been there for a long time. Since I like to have a clear overview about who/what is on 
my network, I decided to write a script myself to regain this broken but basic 
functionality. Thanks Ziggo!
