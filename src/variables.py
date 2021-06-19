import urllib

IMAGE_SEARCH_URL = "https://tr.pinterest.com/resource/BaseSearchResource/get/?"
IMAGE_DATA_QUERY = ""


def SOURCE_URL(url_query_string):
    return "/search/pins/?q=" + urllib.parse.quote(url_query_string)


def IMAGE_DATA(query, bookmark=""):
    DATA = '''{"options":{"isPrefetch":false,"query":"''' + query + '''","scope":"pins","no_fetch_context_on_resource":false},"context":{}}'''
    if bookmark == "":
        return DATA
    else:
        return '''{"options":{"page_size":25,"query":"''' + query + '''","scope":"pins","bookmarks":["''' + bookmark + '''"],"field_set_key":"unauth_react","no_fetch_context_on_resource":false},"context":{}}'''.strip()
