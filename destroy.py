import requests

def destroy():
    url = "http://tx4.crusadertrav.eu/build.php"

    querystring = {"gid":"15","demolish":"1","cancel":"0","c":"CxHhl"}

    payload = "type=37"
    headers = {
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        'accept-encoding': "gzip, deflate",
        'accept-language': "en-US,en;q=0.5",
        'connection': "keep-alive",
        'content-length': "7",
        'content-type': "application/x-www-form-urlencoded",
        'cookie': "__cfduid=d557279a346e75bd97ae56809a703654a1536491851; lang=en; builder=Off; PHPSESSID=dtcr129co8m699c4f6s3higc06; highlightsToggle=true; mapId1=%7B%22grid%22%3Atrue%7D; t4level=1; WMBlueprints=%5B%5D",
        'host': "tx4.crusadertrav.eu",
        'referer': "http://tx4.crusadertrav.eu/build.php?id=26",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0",
        'Cache-Control': "no-cache",
        'Postman-Token': "c354d222-ad15-4b92-add8-c4f7f0fb3d70"
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    print(response.text)

for i in range(19):
    destroy()
