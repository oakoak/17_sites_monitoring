import requests
import datetime
import argparse
import re


def load_urls4check(path):
    with open(path, "r") as file_with_url:
        return file_with_url.read().split()


def is_server_respond_with_200(url):
    page = requests.get(url)
    return page.ok


def get_domain_expiration_date(domain_name):
    string_expiration_date = re.findall(
        r'Expiration Date:</div><div class="df-value">\d{4}-\d{2}-\d{2}',
        requests.get("https://www.whois.com/whois/{}".format(domain_name)).text
    )
    if string_expiration_date:
        expiration_date = datetime.datetime.strptime(
            string_expiration_date[0],
            'Expiration Date:</div><div class="df-value">%Y-%m-%d'
        )
        return expiration_date
    return False


def get_parse_args():
    parser = argparse.ArgumentParser(
        description="Check the site's response and domain registration date"
    )
    parser.add_argument(
        "path",
        help="path to the file with urls"
    )

    return parser.parse_args()


def pprint_url_information(url, expiration_date, respond_200):
    if respond_200:
        print("Url 'https://{}' respond with code 200".format(url))
    else:
        print("Url 'https://{}' not respond with code 200".format(url))
    print("Domain '{}' paid up before {}\n".format(url, expiration_date.date()))


if __name__ == '__main__':
    argument = get_parse_args()
    try:
        urls = load_urls4check(argument.path)
        for url in urls:
            expiration_date = get_domain_expiration_date(url)
            respond_200 = is_server_respond_with_200("https://" + url)
            pprint_url_information(url, expiration_date, respond_200)
    except FileNotFoundError:
        exit("Error:file {} not found".format(argument.path))
    except requests.exceptions.RequestException as error:
        exit(error)
