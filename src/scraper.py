import requests
import json
import os
import urllib


URL = None


def search(d):
    global URL
    if isinstance(d, dict):
        for k, v in d.items():
            if isinstance(v, dict):
                if k == "orig":
                    URL = v["url"]
                else:    
                    search(v)
            elif isinstance(v, list):
                for item in v:
                    search(item)
        

class Scraper:
    def __init__(self, config, image_urls=[]):
        self.config = config
        self.image_urls = image_urls

    # Set config for bookmarks (next page)
    def setConfig(self, config):
        self.config = config

    # Download images
    def download_images(self, output_path):
        # prev get links
        results = self.get_urls()
        try:
            os.makedirs(output_path)
            print("Directory ", output_path, " Created ")
        except FileExistsError:
            pass
        
        number = 0
        listdir = os.listdir(output_path)
        if results != None:
            for i in results:
                file_name = i.split("/")[-1]
                if file_name not in listdir:
                    try:
                        number += 1
                        print("Download ::: ", i)
                        urllib.request.urlretrieve(i, os.path.join(output_path, file_name))
                    except Exception as e:
                        print("Error:", e)

        return number

    # get_urls return array
    def get_urls(self):
        global URL

        SOURCE_URL = self.config.source_url,
        DATA = self.config.image_data,
        URL_CONSTANT = self.config.search_url

        r = requests.get(URL_CONSTANT, params={
                         "source_url": SOURCE_URL, "data": DATA})
        jsonData = json.loads(r.content)
        resource_response = jsonData["resource_response"]
        data = resource_response["data"]
        results = data["results"]
        
        for i in results:
            try:
                self.image_urls.append(i["objects"][0]["cover_images"][0]["originals"]["url"])
            except:
                URL = None
                search(i)
                if URL != None:
                    self.image_urls.append(URL)

        if len(self.image_urls) < int(self.config.file_length):
            try:
                print("Creating links", len(self.image_urls))
                return self.image_urls[0:self.config.file_length]
            except:
                pass
