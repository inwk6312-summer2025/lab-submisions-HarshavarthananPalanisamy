import logging
import requests
from requests.auth import HTTPBasicAuth
import json
import yaml

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

# RESTCONF credentials
USER = 'student'
PASS = 'Meilab123'

# Load YAML configuration
def load_yaml_config(file_path):
    try:
        with open(file_path) as f:
            return yaml.safe_load(f)
    except Exception as e:
        logging.error(f"Error loading YAML file: {e}")
        return None

# Function to configure interface on a router
def set_interface_config(host, interface):
    BASE_URL = f"http://{host}/restconf/api/running/"
    url = BASE_URL + "interfaces/interface/" + interface["name"]
    auth = HTTPBasicAuth(USER, PASS)
    headers = {
        'Accept': 'application/vnd.yang.data+json',
        'Content-Type': 'application/vnd.yang.data+json'
    }

    data = {
        "ietf-interfaces:interface": {
            "name": interface["name"],
            "description": "Configured via RESTCONF and YAML",
            "type": "iana-if-type:ethernetCsmacd",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": interface["ip"],
                        "netmask": interface["netmask"]
                    }
                ]
            },
            "ietf-ip:ipv6": {}
        }
    }

    try:
        response = requests.put(url, auth=auth, headers=headers, data=json.dumps(data))
        if response.status_code == 204:
            logging.info(f"Configured {interface['name']} on {host} successfully.")
        else:
            logging.error(f"Failed to configure {interface['name']} on {host}. "
                          f"Code: {response.status_code}, Message: {response.text}")
    except Exception as e:
        logging.error(f"Request failed for {interface['name']} on {host}: {e}")

# Main logic
def main():
    config = load_yaml_config('interfaces_config.yaml')
    if not config:
        return

    for router in config.get("routers", []):
        host = router["mgmt_ip"]
        for iface in router.get("interfaces", []):
            set_interface_config(host, iface)

if __name__ == "__main__":
    main()
