import requests
import re
from tqdm import tqdm
from multiprocessing import Pool
def fuckserver(x):
## -----------------------------------------------
    url = "http://tx4.crusadertrav.eu/a2b.php"

    payload = "t1=&t4=&t7=&t2=&t5=400&t8=200&t3=&t6=&t11=&x=45&y=13&c=3&s1=ok"
    headers = {
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        'accept-encoding': "gzip, deflate",
        'accept-language': "en-US,en;q=0.5",
        'connection': "keep-alive",
        'content-length': "62",
        'content-type': "application/x-www-form-urlencoded",
        'cookie': "__cfduid=d557279a346e75bd97ae56809a703654a1536491851; lang=en; builder=Off; PHPSESSID=dtcr129co8m699c4f6s3higc06; highlightsToggle=true; mapId1=%7B%22grid%22%3Atrue%7D; WMBlueprints=%5B%5D",
        'host': "tx4.crusadertrav.eu",
        'referer': "http://tx4.crusadertrav.eu/a2b.php?z=17633",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0",
        'Cache-Control': "no-cache",
        'Postman-Token': "bdf39435-0fb5-4cff-836d-fedbdaf39c75"
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
    headers = {
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        'accept-encoding': "gzip, deflate",
        'accept-language': "en-US,en;q=0.5",
        'connection': "keep-alive",
        'content-length': "81",
        'content-type': "application/x-www-form-urlencoded",
        'cookie': "__cfduid=d557279a346e75bd97ae56809a703654a1536491851; lang=en; builder=Off; PHPSESSID=dtcr129co8m699c4f6s3higc06; highlightsToggle=true; mapId1=%7B%22grid%22%3Atrue%7D; WMBlueprints=%5B%5D",
        'host': "tx4.crusadertrav.eu",
        'referer': "http://tx4.crusadertrav.eu/a2b.php",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0",
        'Cache-Control': "no-cache",
        'Postman-Token': "0296f017-8987-489e-8ce8-701f4f1394cb"
        }

    headers['content-length'] = payload.__len__()

    response = requests.request("POST", url, data=payload, headers=headers)

p = Pool(100)
print(p.map(fuckserver, [i for i in range(100)]))
