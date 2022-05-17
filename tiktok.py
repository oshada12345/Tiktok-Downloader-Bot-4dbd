
link ="https://vt.tiktok.com/ZSdxneX78/?k=1 "
def tk(link):
    import requests
    import json
    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

    querystring = {"url":link}

    headers = {
        "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com",
        "X-RapidAPI-Key": "5e086dc085mshd0d98d3fe50d5ecp19c3e8jsnf3bd64e931ff"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    result = response.text
    rest = json.loads(result)
    return {"video":rest["video"][0],"music": rest["music"][0]}

