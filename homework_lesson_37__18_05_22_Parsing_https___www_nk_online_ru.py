import requests
from bs4 import BeautifulSoup
import csv


### Single Term of Lesson 37 ###
def get_page_layout(url):
    page_layout = requests.get(url)
    return page_layout.text


def write_csv(data2):
    with open("homework_lesson_37__18_05_22_Parsing_https___www_nk_online_ru.csv", 'a') as fh_hw_37:
        writer = csv.writer(fh_hw_37, delimiter=';', lineterminator='\r')
        writer.writerow((data2['rubric_news'], data2['date_news'])) #, data2['news']))


def get_news_data1(html):
    soup = BeautifulSoup(html, 'lxml')
    date_l_z = soup.find('div', class_="col-md-9"). \
        find('div', id="comp_1b86e738b9feb52cfaf6497334579ee3"). \
        find_all('div', class_="news-item")[5].find('div', class_="cell info").find('div', class_='date').text
    lesoparkovuyu_zonu = soup.find('div', class_="col-md-9"). \
        find('div', id="comp_1b86e738b9feb52cfaf6497334579ee3"). \
        find_all('div', class_="news-item")[5].find('div', class_="cell info"). \
        find('h3').text
    date_k_p_o_n = soup.find('div', class_="col-md-9"). \
        find('div', id="comp_1b86e738b9feb52cfaf6497334579ee3"). \
        find_all('div', class_="news-item")[4].find('div', class_="cell info").find('div', class_='date').text

    kino_pod_otkrytym_nebom = soup.find('div', class_="col-md-9"). \
        find('div', id="comp_1b86e738b9feb52cfaf6497334579ee3"). \
        find_all('div', class_="news-item")[4].find('div', class_="cell info"). \
        find('h3').find('a').text
    print(f"  {date_l_z} {lesoparkovuyu_zonu} \n\n  {date_k_p_o_n} {kino_pod_otkrytym_nebom}")


def get_news_data2(html):
    soup = BeautifulSoup(html, 'lxml')

    this_week_news = soup.find('div', class_="col-md-9"). \
        find('div', id="comp_1b86e738b9feb52cfaf6497334579ee3"). \
        find_all('div', class_="news-item")

    for i in this_week_news:
        print(f'{i.find("div", class_="cell info").find("div", class_="date").text} : '
              f'{i.find("div", class_="cell info").find("h3").find("a").text}')

    for save_data in this_week_news:
        try:
            rubric_news2 = save_data.find("div", class_="cell info").find('div', class_="rubric").text
        except ValueError:
            rubric_news2 = ""
        try:
            date_news2 = save_data.find("div", class_="cell info").find("div", class_="date").text
        except ValueError:
            date_news2 = ""
        try:
            news2 = save_data.find("div", class_="cell info").find("h3").find("a").text
        except ValueError:
            news2 = ""
        data2 = {"rubric_news": rubric_news2, "date_news": date_news2, 'news': news2}
        # print(data2)
        write_csv(data2)


def main():

    url = "https://www.nk-online.ru/"
    get_news_data2(get_page_layout(url))

    get_news_data1(get_page_layout(url))
    print()




if __name__ == '__main__':
    main()
