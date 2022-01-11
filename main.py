from src import PinterestScraper, PinterestConfig


keywords = [
    "Interiors",
    "coffeeshop interior",
    "penthouse",
    "bathroom",
    "کتابخانه",
    "library interior",
    "traditional interior",
    "store interior design",
    "boutique interior design",
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
    "دکوراسیون",
    "اتاق",
    "پذیرایی",
]

for k in keywords:
    while True:
        configs = PinterestConfig(search_keywords=k, # Search word
                                file_lengths=5000,     # total number of images to download (default = "100")
                                image_quality="originals", # image quality (default = "orig")
                                bookmarks="")         # next page data (default= "")

        number = PinterestScraper(configs).download_images()     # download images directly
        if number == 0:
            break
