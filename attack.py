import requests
import re
from tqdm import tqdm
from multiprocessing import Pool
def fuckserver(x):
## -----------------------------------------------

    url = "http://tx4.crusadertrav.eu/a2b.php"

    payload = "t1=&t7=&t2=&t3=1&t6=&t11=&x=9&y=2&c=4&s1=ok"
    headers = {
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        'accept-encoding': "gzip, deflate",
        'accept-language': "en-US,en;q=0.5",
        'connection': "keep-alive",
        'content-length': "43",
        'content-type': "application/x-www-form-urlencoded",
        'cookie': "__cfduid=d557279a346e75bd97ae56809a703654a1536491851; t4level=1; lang=en; builder=Off; PHPSESSID=dtcr129co8m699c4f6s3higc06; mapId1=%7B%22grid%22%3Atrue%7D; highlightsToggle=true; WMBlueprints=%5B%5D",
        'host': "tx4.crusadertrav.eu",
        'referer': "http://tx4.crusadertrav.eu/a2b.php?z=19808",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0",
        'Cache-Control': "no-cache",
        'Postman-Token': "f7704498-1db6-4ad5-8525-f4883177e216"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

##-----------------------------------------------------


    timestamp = re.findall('<input name="timestamp" value="(.*)" type="hidden">', response.text)[0]
    timestamp_checksum = re.findall('<input name="timestamp_checksum" value="(.*)" type="hidden">', response.text)[0]
    ckey = re.findall('<input name="ckey" value="(.*)" type="hidden">', response.text)[0]
    id = re.findall('<input name="id" value="(.*)" type="hidden">', response.text)[0]
    a = re.findall('<input name="a" value="(.*)" type="hidden">', response.text)[0]
    c = re.findall('<input name="c" value="(.*)" type="hidden">', response.text)[0]

    url = "http://tx4.crusadertrav.eu/a2b.php"

    payload = "ctar1=999&ctar2=999&timestamp={}&timestamp_checksum={}&ckey={}&id={}&a={}&c={}&s1=ok".format(timestamp, timestamp_checksum, ckey, id, a, c)
    print(payload)

    headers['content-length'] = payload.__len__()

    response = requests.request("POST", url, data=payload, headers=headers)

p = Pool(100)
print(p.map(fuckserver, [i for i in range(100)]))
