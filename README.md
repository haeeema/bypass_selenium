# A Bypass using Selenium

I attempted to create a web scraping bot to gather job information. Initially, I utilized the `Selenium` library; however, I encountered a challenge since Selenium doesn't directly provide status codes like traditional web requests. To address this, I turned to the `selenium-wire` library. Unfortunately, I encountered issues with anti-bot measures, which prevented me from accessing the target website. Subsequently, I tried using both `selenium-stealth` and `undetected chromebrowser` solutions, but unfortunately, these attempts were also unsuccessful.

Please help me.

## Features

- **Network Manipulation**: Utilizing `selenium-wire`, the bot has the ability to intercept and modify network requests, which can be useful for debugging, data manipulation, or other advanced use cases.

- **Stealthy Browsing**: The bot employs `selenium-stealth` to mimic human-like browsing behavior, including user agents, languages, and other attributes, reducing the chances of being detected as a bot.

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
