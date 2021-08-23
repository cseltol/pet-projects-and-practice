import requests
from bs4 import BeautifulSoup


def main():
    page = 0
    while True:
        if page == 0:
            url = "https://news.ycombinator.com/newest"
        else:
            url = "https://news.ycombinator.com/newest" + next_link

        request = requests.get(url)
        soup = BeautifulSoup(request.text, "html.parser")
        themes = soup.find_all("td", class_="title")

        for theme in themes:
            theme = theme.find("a", {"class": "storylink"})

            if theme is not None and "github.com" in str(theme):
                sub_link = theme.get("href")
                print("=" * len(str(theme.text)))
                print(str(theme.text) + "\n\t" + str(sub_link))
        nt = soup.find(class_="morelink")
        link = nt.get("href")
        next_link = link[6:]
        page = page + 1


if __name__ == "__main__":
    main()
