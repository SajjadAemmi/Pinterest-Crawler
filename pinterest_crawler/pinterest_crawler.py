import os
import random
from itertools import combinations
from pinterest_crawler.scraper import Scraper
from pinterest_crawler.config import Config


class PinterestCrawler:
    def __init__(self, output_dir_path="./io/output"):
        self.output_dir_path = output_dir_path
        os.makedirs(self.output_dir_path, exist_ok=True)
        
    def __call__(self, keywords, number_of_words=2):
        keywords_list = self.create_keywords_list(keywords)
        print("Start crawling...")
        self.counter = 0
        if len(keywords_list) == 1:
            number_of_words = 1
        for item in combinations(keywords_list, number_of_words):
            if self.counter == 4:
                break

            keyword = " ".join(item)
            print(keyword)

            while True:
                configs = Config(
                    search_keywords=keyword,  # Search word
                    # total number of images to download (default = "100")
                    file_lengths=5000,
                    # image quality (default = "orig")
                    image_quality="originals",
                    # next page data (default= "")
                    bookmarks="",
                    scroll=10000)

                if not self.download(configs, self.output_dir_path):
                    break
        
        images = os.listdir(self.output_dir_path)
        print(f"{len(images)} images saved in directory: {self.output_dir_path}")

    def create_keywords_list(self, keywords):
        keywords_list = []
        for keyword in keywords:
            if os.path.isfile(keyword):
                file = open(keyword, "r", encoding="utf-8")
                keywords_list += [keyword.strip() for keyword in file.read().split('\n')]
            elif isinstance(keyword, str):
                keywords_list.append(keyword)
        random.shuffle(keywords_list)
        return keywords_list

    def download(self, configs, output_dir_path):
        number = Scraper(configs).download_images(output_dir_path)
        if number == 0:
            self.counter += 1
            return False
        else:
            self.counter = 0
            return True
