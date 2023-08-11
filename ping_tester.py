import requests
import time

def test_ping(url):
    try:
        response = requests.get(url, timeout=5)
        return f"{url} - Status: {response.status_code}, Ping: {response.elapsed.total_seconds()}s\n"
    except requests.RequestException:
        return f"{url} - Status: Failed to connect\n"

def main():
    urls = [
        "http://www.google.com",
        "http://www.example.com",
        # Adicione mais URLs aqui
    ]

    while True:
        with open("ping_results.txt", "a") as f:
            f.write(time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
            for url in urls:
                result = test_ping(url)
                f.write(result)
                print(result)
            f.write("\n")
        
        time.sleep(6)  # Espera 10 minutos (10 minutos = 600 segundos)

if __name__ == "__main__":
    main()
