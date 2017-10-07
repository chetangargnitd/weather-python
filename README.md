#weather-python

**_A simple utility script which assists in getting weather of a city._**

**Modules used:**

- Requests
  * It can be installed using `sudo pip install requests` or `sudo apt-get install python-requests`



It is implemented using the **requests** module, along with **os**, **sys** and **json** modules.

* The first feature is implemented using the json response generated, after making a request via the **requests** module to the [openweathermap API](https://openweathermap.org) after generating an API key from the website. The json response is thereafter processed and the information is extracted using the **json** module.

**How to use:** Enter the choice and city when asked for.

**To run the script:** Type `python weather.py` from your terminal.

All the results will be displayed on the terminal, as well as saved in a file called _info.txt_ in the same directory where the script is present.