import math
import speedtest

def bytes_to_mb(size_bytes):
    i = int(math.floor(math.log(size_bytes, 1024)))
    power = math.pow(1024, i)
    size = round(size_bytes / power, 2)
    return f"{size} mpbs"

##speedtest

wifi = speedtest.Speedtest()

print("getting download speed...")
download_speed = wifi.download()

print("getting upload speed...")
upload_speed = wifi.upload()

print("Download: ", bytes_to_mb(download_speed))
print("upload: ", bytes_to_mb(upload_speed))
