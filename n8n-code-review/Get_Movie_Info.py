import requests
from bs4 import BeautifulSoup as bs

# movie_title = 'AttilaMarcel'


def make_movie_name(movie_title):
    movie_sub_title = ''
    basic_url = 'https://search.naver.com/search.naver?query='

    movie_url = basic_url + movie_title
    response = requests.get(movie_url)

    if response.status_code == 200:
        sub_title_temp = ''

        html = response.text
        soup = bs(html, 'html.parser')
        movie_title = soup.find_all('span', 'area_text_title')
        movie_sub_info = soup.find_all('div', 'sub_title')

        # 영화 메인 타이틀
        for title in movie_title:
            movie_title = title.text

        # print(movie_title)

        # 영화 sub info
        for sub_info in movie_sub_info:
             sub_title_temp = sub_info.text.split()

        movie_sub_title = ' '.join([word for word in sub_title_temp[0:-1] if word != '영화'])

        print(movie_title + ' (' + movie_sub_title + ', ' + sub_title_temp[-1] + ') (FHD)')

    else:
        print('error' + response.status_code)


if __name__ == '__main__':
    text_file_info = []

    # 텍스트 파일에서 링크와 제목 아티스트 get (구분자는 |)
    try:
        with open('Test_movie_name.txt', 'r', encoding='UTF8') as f:
            lines = f.readlines()  # 모든 줄을 읽어옴
            text_file_info = [line.strip() for line in lines]
    except Exception as e:
        print('텍스트 파일 읽어오기 실패: ', e)

    for movie in text_file_info:
        make_movie_name(movie)