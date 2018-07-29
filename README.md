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
python check_sites_health.py urls.txt
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
Domain 'yandex.ru' paid up before 2018-09-30

Url 'https://stackoverflow.com' respond with code 200
Domain 'stackoverflow.com' paid up before 2019-02-02

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
