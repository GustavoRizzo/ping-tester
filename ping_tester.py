import requests
import time
import csv
from urllib.parse import urlparse

def test_ping(url):
    try:
        response = requests.get(url, timeout=5)
        status = response.status_code
        ping = response.elapsed.total_seconds()
        return status, ping
    except requests.RequestException:
        return "Failed to connect", None

def main():
    urls = [
        "http://www.google.com",
        "http://www.example.com",
        # Adicione mais URLs aqui
    ]

    while True:
        for url in urls:
            status, ping = test_ping(url)
            name = url.split(".")[1]
            filename = f"result/{name}_ping.csv"  # Nome do arquivo CSV baseado no nome do site
            
            with open(filename, "a", newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                
                if csvfile.tell() == 0:  # Adicionar o cabeçalho apenas se o arquivo estiver vazio
                    header = ["datetime", "url", "domain_name", "status", "ping"]
                    csvwriter.writerow(header)
                
                csvwriter.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), url, name, status, ping])
                print(f"URL: {url}, Domain: {name}, Status: {status}, Ping: {ping}")
        
        time.sleep(600)  # Espera 10 minutos (10 minutos = 600 segundos)

if __name__ == "__main__":
    main()
