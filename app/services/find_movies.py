# -*- encoding=utf-8 -*-
import requests
from bs4 import BeautifulSoup
from app.models import db
from app.models import Movie, Comment


def find_movies():
    r_movies = requests.get('https://movie.douban.com/cinema/nowplaying/shanghai/').text

    movies_soup = BeautifulSoup(r_movies, "html.parser")

    movies = movies_soup.find_all('li', 'list-item')
    print(type(movies))
    for movie in movies:
    # movie = movies[0]
        if 'id' in movie.attrs.keys():
            movie_id = movie.attrs['id']
        if 'data-title' in movie.attrs.keys():
            movie_title = movie.attrs['data-title']
        if 'data-actors' in movie.attrs.keys():
            movie_actors = movie.attrs['data-actors']
        if 'data-director' in movie.attrs.keys():
            movie_director = movie.attrs['data-director']
        if 'data-score' in movie.attrs.keys():
            movie_score = movie.attrs['data-score']
        print(movie_id, movie_title, movie_actors, movie_director, movie_score)
        poster = movie.find('li', 'poster')
        comments = []
        if poster is not None:
            print(poster)
            print(4, poster.img)
            print(5, poster.a)
            if 'src' in poster.attrs.keys():
                movie_img = poster.img.attrs['src']

            if poster.a is not None and 'href' in poster.a.attrs.keys():
                print('href')
                movie_href = poster.a.attrs['href']
                movie_detail = requests.get(movie_href).text
                movie_soup = BeautifulSoup(movie_detail, 'html.parser')
                review_list = movie_soup.find('div', 'review-list')
                if review_list is not None:
                    print(6)
                    review_item = review_list.find_all('div', 'main review-item')
                    if review_item is not None:
                        print(review_item)
                        for i in range(0, 2):
                            print(7)
                            if i < len(review_item) and 'id' in review_item[i].attrs.keys():
                                comment_id = review_item[i].attrs['id']
                                comment = requests.get(r'https://movie.douban.com/j/review/' + comment_id + r'/full').text
                                comments.append(comment)
                                # print(comment)
                                print(i)
        print(7.5, len(comments))
        test_movie = Movie(id=movie_id, chinese_name=movie_title,
                           director=movie_director, actor=movie_actors)
        for comment in comments:
            print(8)
            test_comment = Comment(score='3.4', content=comment, movie=test_movie)
            print(test_comment.content)

        db.session.add(test_movie)
        db.session.commit()


if __name__ == '__main__':
    find_movies()