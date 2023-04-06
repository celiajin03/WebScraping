# :woman_technologist: Web Scraping for Slots Scanning	:mag:

This project aims to scrape a website to check for availability of a course on a particular start date. If the course is available, it sends a text message to a specified phone number using the **Twilio API**.

This project can be used as a starting point and general template for building more complex web scraping and automated messaging applications. With some modification, the script can be easily adapted to work with a wide range of websites and data sources. For example, it can be used to check for product availability on an e-commerce website, monitor stock prices or weather conditions, or track changes in public data sets.

## Getting Started
To run this project, you'll need Python 3 installed on your system. You'll also need to install a couple packages using `pip`:

```
pip install time urllib ast twilio
```

> - The `time` library is used to introduce time delays in the script.
> - The `urllib` library is used to open a URL and make HTTP requests. 
> - The `ast` library is used to convert a string representation of a dictionary to an actual dictionary. 
> - The `twilio` library is used to send text messages through the Twilio API.

## Usage
1. Clone the repository to your local machine.
`
2. Open the `scraper.py file and replace the Twilio API account SID, auth token, receiving phone number, and Twilio phone number with your own.

3. In the values dictionary, replace the selected value with the ID of the course you're interested in. You can find this ID by inspecting the HTML code of the booking form on the tracked website.

4. Run the scraper.py script using the `nohup` command to run the script in the background and avoid interruption by the SIGHUP signal:
```
nohup python scraper.py &
```

The script will run indefinitely, checking for availability of the selected course every 5 minutes. If the course is available on the specified start date (May 16, 2022), it will send a text message to your phone number using the Twilio API. <br> <br>
You can view the output and any errors that occur by checking the nohup.out file in the project directory.


## Disclaimer:
This script is for educational purposes only. Use of this script to scrape websites or send unsolicited text messages may be a violation of website terms of use and can lead to legal issues. The developer is not responsible for any misuse of this script.
