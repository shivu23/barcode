# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 13:33:47 2019

@author: Shivu
"""

import imdb
hr=imdb.IMDb()
movie_name=input("enter your movie name")
movies=hr.search_movie(str(movie_name))
index=movies[0].getID()
movie=hr.get_movie(index)
title=movie['title']
year=movie['year']
cast=movie['cast']
list_of_cast=','.join(map(str,cast))
print("title",title)
print("year",year)
print("cast",list_of_cast)