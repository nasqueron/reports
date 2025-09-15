#   -------------------------------------------------------------
#   Rhyne-Wise :: Client
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    MediaWiki client
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


from typing import Dict

import pywikibot
from pywikibot.login import ClientLoginManager

from rhyne_wyse.credentials import vault


#   -------------------------------------------------------------
#   Wiki authentication
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def fetch_credentials(credentials_config: Dict) -> Dict:
    try:
        driver = credentials_config["driver"]
    except KeyError:
        raise ValueError("Missing config key: wiki.credentials.driver")

    if driver == "vault":
        client = vault.connect_to_vault()
        return vault.read_app_secret(client, credentials_config["secret"])

    raise ValueError(f"Unknown credentials driver: {driver}")


def connect_to_site(config: Dict):
    site = pywikibot.Site()

    credentials = fetch_credentials(config["credentials"])
    manager = ClientLoginManager(
        site=site,
        user=credentials["username"],
        password=credentials["password"],
    )
    manager.login()
    site.login()

    return site
