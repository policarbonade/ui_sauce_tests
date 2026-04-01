from pages.google_page import GooglePage


def test_sauce_search(page):
    google = GooglePage(page)

    google.open()