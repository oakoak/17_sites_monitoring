# Sites Monitoring Utility

---
The script determines if the site is available and up to what date the domain is paid for
---

## Description
+ The script takes an input file with a list of sites
+ Checks if the site with code 200 is responding
+ Checks up to what date a domain is paid on whois.com

## Example using
```commandline
python check_sites_health.py urls.txt 30
```

## Example input file *urls.txt*
```text
google.ru
yandex.ru
stackoverflow.com
```

## Example output
```commandline
Url 'https://yandex.ru' respond with code 200
Domain 'yandex.ru' is paid for more then 30 days

Url 'https://stackoverflow.com' respond with code 200
Domain 'stackoverflow.com' is paid for more then 30 days
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
