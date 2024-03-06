import requests
import time

def ping_codespace():
    codespace_url = "https://redesigned-waffle-wjwjx7wp9w5c995q.github.dev/"
    while True:
        try:
            response = requests.get(codespace_url)
            print(f"Ping successful! Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error pinging codespace: {e}")
        time.sleep(100)  

if __name__ == "__main__":
    ping_codespace()
