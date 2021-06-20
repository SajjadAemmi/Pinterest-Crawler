
from src import PinterestScraper, PinterestConfig


configs = PinterestConfig(search_keywords="Atatürk", # Search word
                          file_lengths=200,     # total number of images to download (default = "100")
                          image_quality="orig", # image quality (default = "orig")
                          bookmarks="")         # next page data (default= "")


PinterestScraper(configs).download_images()     # download images directly
print(PinterestScraper(configs).get_urls())     # just bring image links
