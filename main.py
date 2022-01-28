import os
import random
import argparse
from itertools import combinations
from src import PinterestScraper, PinterestConfig


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--keywords", default="keywords.txt", help="path to input image")
    parser.add_argument('--output', help='output dir', default='photos', type=str)
    parser.add_argument("-nw", '--number-of-words', help='number of keywords for search', default=4, type=int)
    args = parser.parse_args()

    file = open(args.keywords, "r")
    keywords = file.read().split('\n')
    keywords = [keyword.strip() for keyword in keywords]

    print("start crawling...")
    random.shuffle(keywords)
    counter = 0
    for item in combinations(keywords, args.number_of_words):
        if counter == 4:
            break

        keyword = " ".join(word for word in item)
        print(keyword)

        while True:
            configs = PinterestConfig(search_keywords=keyword,  # Search word
                                    file_lengths=5000,  # total number of images to download (default = "100")
                                    image_quality="originals",  # image quality (default = "orig")
                                    bookmarks="",  # next page data (default= "")
                                    scroll=10000)

            number = PinterestScraper(configs).download_images(args.output)  # download images directly
            print("number:", number)
            if number == 0:
                counter += 1
                break
            else:
                counter = 0

    print("All images in dir:", len(os.listdir("photos")))