import requests
import os
import sqlite3
from datetime import datetime

conn = sqlite3.connect(r"database/database.db", check_same_thread=False)
db = conn.cursor()

# https://developer.twitter.com/en/portal/dashboard
bearer_token = os.environ.get("BEARER_TOKEN")

interested_accounts = {
    "GME": "GameStop",
    "AMC": "AMCTheatres",
    "CLOV": "CloverHealth",
    "BB": "BlackBerry",
    "AMD": "AMD",
    "UWMC": "UWMlending",
    "NIO": "NIO",
    "TSLA": "Tesla",
    "AAPL": "Apple",
    "NOK": "Nokia",
    "NVDA": "Nvidia",
    "MSFT": "Microsoft",
    "RBLX": "Roblox",
    "F": "Ford",
    "PLTR": "PalantirTech",
    "COIN": "CoinBase",
    "RKT": "RocketCompanies",
    "MVIS": "MicroVision",
    "FUBO": "fuboTV",
    "VIAC": "ViacomCBS",
    "SNDL": "sundialcannabis",
    "SPCE": "virgingalactic",
    "SNAP": "Snapchat",
    "OCGN": "Ocugen",
    "ROKU": "Roku",
    "BABA": "AlibabaGroup",
    "SE": "SeaGroup",
    "EXPR": "express",
    "SOFI": "SoFi",
    "WKHS": "Workhorse_Group",
    "TLRY": "tilray",
    "CLNE": "CE_NatGas",
    "WISH": "WishShopping",
    "CLF": "CliffsNR",
    "GOEV": "canoo",
    "DKNG": "DraftKings",
    "AMZN": "amazon",
    "TWTR": "Twitter",
    "FB": "Facebook",
    "PYPL": "PayPal",
    "SQ": "Square",
    "XPEV": "XPengMotors",
    "NKLA": "nikolamotor",
    "BNGO": "bionanogenomics",
    "SKLZ": "SKLZ",
    "CRSR": "CORSAIR",
    "CRSP": "CRISPRTX",
    "XELA": "ExelaTech",
    "MMAT": "Metamaterialtec",
    "HOOD": "RobinhoodApp",
    "LCID": "LucidMotors",
    "NVAX": "Novavax",
    "MRNA": "moderna_tx",
    "NFLX": "Netflix",
    "BA": "Boeing",
    "GOOG": "Google",
    "GOOGL": "Google",
    "BAC": "BankofAmerica",
    "BNTX": "BioNTech_Group",
    "DIS": "Disney",
    "SBUX": "Starbucks",
    "INTC": "intel",
    "AAL": "AmericanAir",
    "COKE": "CocaCola",
    "MCD": "McDonalds",
    "C": "Citi",
    "T": "ATT",
    "V": "Visa",
    "PEP": "pepsi",
    "NKE": "Nike",
    "JPM": "jpmorgan",
    "ADBE": "Adobe",
    "WMT": "Walmart",
    "IBM": "IBM",
    "GS": "GoldmanSachs",
    "SHOP": "Shopify",
    "TWLO": "Twilio",
    "Z": "zillow",
    "CRWD": "CrowdStrike",
    "SNOW": "SnowflakeDB",
    "NET": "Cloudflare",
    "WEN": "Wendys",
    "DPZ": "dominos",
    "PINS": "Pinterest",
    "ORCL": "Oracle",
    "UA": "UnderArmour",
    "LUMN": "lumentechco",
    "JD": "JD_Corporate",
    "CSCO": "Cisco",
    "JNJ": "JNJNews",
    "U": "unity3d",
    "ZM": "Zoom",
    "SPOT": "Spotify",
    "MSTR": "MicroStrategy",
    "UBER": "UBER"
}
date_updated = str(datetime.now()).split()[0]


def create_url(username):
    url = "https://api.twitter.com/1.1/users/show.json?screen_name={}".format(username)
    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth,)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    for symbol, account in interested_accounts.items():
        url = create_url(account)
        json_response = connect_to_endpoint(url)
        print(symbol, json_response["followers_count"])
        db.execute("INSERT OR IGNORE INTO twitter_followers VALUES (?, ?, ?)",
                   (symbol, json_response["followers_count"], date_updated))
        conn.commit()


if __name__ == "__main__":
    main()
