
link ="https://vt.tiktok.com/ZSdxneX78/?k=1 "
def tk(link):
    import requests
    import json
    url = "https://tiktok-full-info-without-watermark.p.rapidapi.com/vid/index"

    querystring = {"url":link}

    headers = {
        "X-RapidAPI-Host": "tiktok-full-info-without-watermark.p.rapidapi.com",
        "X-RapidAPI-Key": "3f7b85e600msh163785d28acda05p113d81jsncbb31efb5ffc"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    result = response.text
    rest = json.loads(result)
    return {"video":rest["video"][0],"music": rest["music"][0]}

