import requests
import datetime
import argparse
import whois
import socket


def load_urls4check(path):
    with open(path, "r") as file_with_url:
        return file_with_url.read().split()


def is_server_respond_with_ok(url):
    try:
        response = requests.get(url)
        return response.ok
    except requests.exceptions.RequestException as error:
        return None


def get_domain_expiration_date(domain_name):
    try:
        response = whois.whois(domain_name)
        expiration_date = response["expiration_date"]
        if isinstance(expiration_date, list):
            return expiration_date[0]
        else:
            return expiration_date
    except (socket.error, whois.parser.PywhoisError):
        return None


def get_parse_args():
    parser = argparse.ArgumentParser(
        description="Check the site's response and domain registration date"
    )
    parser.add_argument(
        "path",
        default="urls.txt",
        help="path to the file with urls"
    )
    parser.add_argument(
        "days",
        type=int,
        default=30,
        help="Amount of days to check the payment date"
    )

    return parser.parse_args()


def check_payment_date(expiration_date, amount_of_days):
    date_now = datetime.datetime.today()
    check_day = date_now + datetime.timedelta(amount_of_days)
    return check_day < expiration_date


def pprint_url_information(url, expiration_date, respond_200, amount_of_days):
    if respond_200 is None:
        print("Could not connect to url '{}'".format(url))
    elif respond_200 is True:
        print("Url '{}' respond with ok code".format(url))
    else:
        print("Url '{}' not respond with ok code".format(url))

    if expiration_date is None:
        print("Could not connect to domain '{}'".format(url))
    elif check_payment_date(expiration_date, amount_of_days):
        print("Domain '{}' is paid for more then {} days\n"
              .format(url, amount_of_days))
    else:
        print("Domain '{}' isn't paid for {} days\n"
              .format(url, amount_of_days))


if __name__ == "__main__":
    argument = get_parse_args()
    try:
        urls = load_urls4check(argument.path)
    except FileNotFoundError:
        exit("Error:file {} not found".format(argument.path))
    for url in urls:
        expiration_date = get_domain_expiration_date(url)
        respond_ok = is_server_respond_with_ok(url)
        pprint_url_information(
            url,
            expiration_date,
            respond_ok,
            argument.days
        )

