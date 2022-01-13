from src import PinterestScraper, PinterestConfig


keywords = [
    "Kid's Room",
    "modsy",
    "ikea",
    "ikea room",
    "offices",
    "bussines office",
    "Interiors",
    "coffeeshop interior",
    "penthouse",
    "bathroom",
    "library interior",
    "traditional interior",
    "hotel interior",
    "lobby hotel",
    "apartement",
    "salon",
    "office", 
    "living room", 
    "Inside design", 
    "room", 
    "sofa", 
    "modern house decor",
]

for k in keywords:
    print("keyword:", k)
    while True:
        configs = PinterestConfig(search_keywords=k, # Search word
                                file_lengths=5000, # total number of images to download (default = "100")
                                image_quality="originals", # image quality (default = "orig")
                                bookmarks="", # next page data (default= "")
                                scroll=1000)         

        number = PinterestScraper(configs).download_images()     # download images directly
        if number == 0:
            break
