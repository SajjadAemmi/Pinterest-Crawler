import random
from itertools import combinations
from src import PinterestScraper, PinterestConfig


file = open("keywords.txt", "r")
keywords = file.read().split('\n')
keywords = [keyword.strip() for keyword in keywords]

print("start crawling...")
random.shuffle(keywords)
counter = 0
number_of_words = 4
for item in combinations(keywords, number_of_words):
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

        number = PinterestScraper(configs).download_images()  # download images directly
        print("number:", number)
        if number == 0:
            counter += 1
            break
        else:
            counter = 0
