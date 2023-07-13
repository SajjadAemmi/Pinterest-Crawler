# Pinterest Crawler

[![Upload Python Package](https://github.com/SajjadAemmi/Pinterest-Crawler/actions/workflows/python-publish.yml/badge.svg)](https://github.com/SajjadAemmi/Pinterest-Crawler/actions/workflows/python-publish.yml)
[![Python package](https://github.com/SajjadAemmi/Pinterest-Crawler/actions/workflows/python-package.yml/badge.svg)](https://github.com/SajjadAemmi/Pinterest-Crawler/actions/workflows/python-package.yml)
[![Python application](https://github.com/SajjadAemmi/Pinterest-Crawler/actions/workflows/python-app.yml/badge.svg)](https://github.com/SajjadAemmi/Pinterest-Crawler/actions/workflows/python-app.yml)

<img src="https://raw.githubusercontent.com/SajjadAemmi/Pinterest-Crawler/main/Pinterest-Logo.png" width="400px">

Downloads HD images from pinterest by your favorite keywords. A useful tool to create a dataset for machine learning projects.

## Install
Install the package with pip in a Python>=3.8 environment:
```
pip install pinterest-crawler
```

## Usage

### CLI
Pinterest Crawler may be used directly in the Command Line Interface (CLI):

```bash
pinterest-crawler --keywords lion tiger bear
```

Also you can write your favorite keywords in a file for example `my_keywords.txt` and set path of file in `--keywords` argument:
```bash
pinterest-crawler --keywords my_keywords.txt
```

### Python 
Coming soon...
<!-- Due to some limitations of Pinterest, you can download 100 images per keyword. If you want to download more images, you can run following command for infinite execution:

```
python loop.py
``` -->

## TODO
- [ ] download images in a loop
- [ ] download images in a specific size
- [ ] download images in a specific format
