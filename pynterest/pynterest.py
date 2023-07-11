import os
import random
import argparse
from itertools import combinations
from src import PinterestScraper, PinterestConfig


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--keywords", help="keywords as path of file or list of words", nargs='+', default=[])
    parser.add_argument('--output', help='output dir', default='io/output', type=str)
    parser.add_argument("-nw", '--number-of-words', help='number of keywords for search', default=2, type=int)
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    keywords = []
    for keyword in args.keywords:
        if os.path.isfile(keyword):
            file = open(keyword, "r", encoding="utf-8")
            keywords += [keyword.strip() for keyword in file.read().split('\n')]
        elif isinstance(keyword, str):
            keywords.append(keyword)
    random.shuffle(keywords)
    
    print("start crawling...")
    counter = 0
    if len(keywords) == 1:
        args.number_of_words = 1
    for item in combinations(keywords, args.number_of_words):
        if counter == 4:
            break

        keyword = " ".join(word for word in item)
        print(keyword)

        while True:
            configs = PinterestConfig(search_keywords=keyword,  # Search word
                                      # total number of images to download (default = "100")
                                      file_lengths=5000,
                                      # image quality (default = "orig")
                                      image_quality="originals",
                                      # next page data (default= "")
                                      bookmarks="",
                                      scroll=10000)

            # download images directly
            number = PinterestScraper(configs).download_images(args.output)  
            print("number:", number)
            if number == 0:
                counter += 1
                break
            else:
                counter = 0

    print("All images in dir:", len(os.listdir(args.output)))


if __name__ == "__main__":
    main()
