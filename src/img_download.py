import urllib
import os

def image_download(results, folder, quality="orig"):
    folder = "photos/"+folder.replace(" ","-")
    number = 0
    try:
        os.makedirs(folder)
        print("Directory ", folder, " Created ")
    except FileExistsError:
        a=1
    arr = os.listdir(folder+"/")
    for i in results:
        if str(i["image_signature"]) + ".jpg" not in arr:
            try:
                print("Download ::: ", i["images"][quality]["url"])
                urllib.request.urlretrieve(i["images"]["orig"]["url"],  str(folder) + "/" + str(i["image_signature"]) + ".jpg")
                number = number + 1
            except Exception as e: print(e)
