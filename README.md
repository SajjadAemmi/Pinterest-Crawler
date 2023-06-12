# Pinterest Image Download by Keywords

You can download as many images as you want about the searched words. You can also download images in a loop and use it to create a dataset for machine learning projects.

## Installation

Run following command for install requirements:

```
pip install -r requirements.txt
```

## Run

Set your favorite keywords in `keywords.txt` and run following command for collect some images:

```
python main.py
```

Due to some limitations of Pinterest, you can download 100 images per keyword. If you want to download more images, you can run following command for infinite execution:

```
python loop.py
```
