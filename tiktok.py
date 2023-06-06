
link ="https://vt.tiktok.com/ZSdxneX78/?k=1 "
def tk(link):
    import requests
    import json
    url = "https://tiktok-full-info-without-watermark.p.rapidapi.com/vid/index"

    querystring = {"url":link}

    headers = {
        "X-RapidAPI-Host": "tiktok-full-info-without-watermark.p.rapidapi.com",
        "X-RapidAPI-Key": "3f7b85e600msh163785d28acda05p113d81jsncbb31efb5ffc"
    },
       
    };

    const res = await axios.request(options);
    console.log(res.data);
    const result = {
      videoUrl: res.data.video ? res.data.video[0] : false,
      caption: res.data.author
        ? res.data.author[0] + "\n @UpperDownloaderBot"
        : false,
    };

    return result;
  } catch (err) {
    console.log(err);
  }
}
