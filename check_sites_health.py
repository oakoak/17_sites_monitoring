import requests
import datetime
import argparse
import whois
import socket


def load_urls4check(path):
    with open(path, "r") as file_with_url:
        return file_with_url.read().split()


def is_server_respond_with_ok(url):
    page = requests.get(url)
    return page.ok


def get_domain_expiration_date(domain_name):
    try:
        response = whois.whois(domain_name)
        expiration_date = response["expiration_date"]
        if isinstance(expiration_date, list):
            return expiration_date[0]
        else:
            return expiration_date
    except socket.error:
        return False
    except whois.parser.PywhoisError:
        return False


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
    if respond_200:
        print("Url 'https://{}' respond with code 200".format(url))
    else:
        print("Url 'https://{}' not respond with code 200".format(url))
    if check_payment_date(expiration_date, amount_of_days):
        print("Domain '{}' is paid for more then {} days\n"
              .format(url, amount_of_days))
    else:
        print("Domain '{}' isn't paid for {} days\n"
              .format(url, amount_of_days))


if __name__ == "__main__":
    argument = get_parse_args()
    try:
        urls = load_urls4check(argument.path)
        for url in urls:
            expiration_date = get_domain_expiration_date(url)
            respond_ok = is_server_respond_with_ok("https://" + url)
            pprint_url_information(
                url,
                expiration_date,
                respond_ok,
                argument.days
            )
    except FileNotFoundError:
        exit("Error:file {} not found".format(argument.path))
    except requests.exceptions.RequestException as error:
        exit(error)
