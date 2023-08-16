# A Bypass using Selenium

The Bypass Bot is a Python script designed to automate browser interactions using the `selenium-wire` libraries, utilizing a detected Chrome browser instance. This bot is created to navigate websites while evading detection mechanisms, providing a versatile tool for various web scraping, automation, or testing tasks.

## Features

- **Network Manipulation**: Utilizing `selenium-wire`, the bot has the ability to intercept and modify network requests, which can be useful for debugging, data manipulation, or other advanced use cases.

- **Stealthy Browsing**: The bot employs `selenium-stealth` to mimic human-like browsing behavior, including user agents, languages, and other attributes, reducing the chances of being detected as a bot.

- **Detected Chrome Browser**: The bot leverages a detected Chrome browser instance, enabling compatibility with websites that use anti-bot mechanisms to detect automated browser sessions.

## Installation

- Python 3.x
- Chrome browser
- ChromeDriver
- undetected-chromedriver
- Required Python packages (install using `pip3`):
  - selenium
  - selenium-stealth
  - selenium-wire

```bash
pip3 install selenium selenium-stealth selenium-wire undetected-chromedriver
```

## Notion

[✅ Selenium_Bypass](https://www.notion.so/haminpark/Selenium_Bypass-Cloudflare-f4fb5934e63147c29d1623e6de556e0f)

## Comments

Remember to always respect the website's robots exclusion standard (robots.txt) and check their terms of service while developing.

## License

This project is licensed under the [MIT License](LICENSE).
