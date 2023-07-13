import unittest


class TestPinterestCrawler(unittest.TestCase):
    """
    high level support for doing this and that.
    """
    def test_import(self):
        import pinterest_crawler

    def test_version(self):
        import pinterest_crawler
        print(pinterest_crawler.__version__)

    def test_download(self):
        return True


if __name__ == '__main__':
    unittest.main()
