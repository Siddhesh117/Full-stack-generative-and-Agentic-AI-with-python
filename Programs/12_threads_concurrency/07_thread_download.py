import threading
import requests
import time

def download(url):
    print(f"Starting download from {url}")
    resp = requests.get(url)
    print(f"Finished downloading from {url}, size: {len(resp.content)} bytes")


urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]

start = time.time()

threads = []

for url in urls:
    t = threading.Thread(target=download, args=(url, )) # accept tuple thats why add , and space
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()

print(f"All downloads done in {end - start:.2f} seconds")

# Starting download from https://httpbin.org/image/jpeg
# Starting download from https://httpbin.org/image/png
# Starting download from https://httpbin.org/image/svg
# Finished downloading from https://httpbin.org/image/png, size: 8090 bytes
# Finished downloading from https://httpbin.org/image/svg, size: 8984 bytes
# Finished downloading from https://httpbin.org/image/jpeg, size: 35588 bytes
# All downloads done in 2.13 seconds