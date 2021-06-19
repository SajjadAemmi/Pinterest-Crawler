import requests
import json
import src.img_download as img_download
import src.variables as constant



def main():
    connect("Software")

# TODO
def connect(query_string, bookmarks=""):
    SOURCE_URL = constant.SOURCE_URL(query_string),
    DATA = constant.IMAGE_DATA(query_string, bookmarks),
    URL_CONSTANT = constant.IMAGE_SEARCH_URL
    r = requests.get(URL_CONSTANT, params={"source_url": SOURCE_URL, "data": DATA})
    print(r.url)
    jsonData = json.loads(r.content)
    resource_response = jsonData["resource_response"]
    data = resource_response["data"]
    results = data["results"]
    img_download.image_download(results, query_string)
    if len(str(resource_response["bookmark"])) > 1 : connect(query_string, bookmarks=resource_response["bookmark"])



if __name__ == '__main__':
    main()
