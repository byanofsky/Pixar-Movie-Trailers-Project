#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Creates instances of the Movie class and launches web page."""

import fresh_tomatoes
import media

# Create instances of Movie class
finding_dory = media.Movie(
    "Finding Dory",
    "Dory tries to find her parents.",
    "https://upload.wikimedia.org/wikipedia/en/3/3e/Finding_Dory.jpg",
    "https://www.youtube.com/watch?v=NQu-153MnGQ",
    2016)

the_good_dinosaur = media.Movie(
    "The Good Dinosaur",
    "A dinosaur tries to get back to his family.",
    "https://upload.wikimedia.org/wikipedia/en/8/80/The_Good_Dinosaur_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=daFnEiLEx70",
    2015)

inside_out = media.Movie(
    "Inside Out",
    "Two feelings get lost and have to get back to the others.",
    "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=_MC3XuMvsDI",
    2015)

monsters_university = media.Movie(
    "Monsters University",
    "A movie about monsters meeting in college.",
    "https://upload.wikimedia.org/wikipedia/en/2/2a/Monsters_University_poster_3.jpg",  # NOQA
    "https://www.youtube.com/watch?v=xBzPioph8CI",
    2013)

brave = media.Movie(
    "Brave",
    "A Scottish princess must save her mother.",
    "https://upload.wikimedia.org/wikipedia/en/9/96/Brave_Poster.jpg",
    "https://www.youtube.com/watch?v=TEHWDA_6e3M",
    2012)

cars_2 = media.Movie(
    "Cars 2",
    "The second movie about cars.",
    "https://upload.wikimedia.org/wikipedia/en/7/7f/Cars_2_Poster.jpg",
    "https://www.youtube.com/watch?v=oFTfAdauCOo",
    2011)

toy_story_3 = media.Movie(
    "Toy Story 3",
    "The third movie about toys.",
    "https://upload.wikimedia.org/wikipedia/en/6/69/Toy_Story_3_poster.jpg",
    "https://www.youtube.com/watch?v=JcpWXaA2qeg",
    2010)

up = media.Movie(
    "Up",
    "A movie about an old man who goes on an adventure.",
    "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
    "https://www.youtube.com/watch?v=pkqzFUhGPJg",
    2009)

wall_e = media.Movie(
    "Wall•E",
    "A robot tries to save his friend, and the human race.",
    "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
    "https://www.youtube.com/watch?v=ZisWjdjs-gM",
    2008)

ratatouille = media.Movie(
    "Ratatouille",
    "A rat helps a chef learn to cook.",
    "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk",
    2007)

cars = media.Movie(
    "Cars",
    "A movie about cars",
    "https://upload.wikimedia.org/wikipedia/en/3/34/Cars_2006.jpg",
    "https://www.youtube.com/watch?v=WGByijP0Leo",
    2006)

the_incredibles = media.Movie(
    "The Incredibles",
    "A superhero family must save the day.",
    "https://upload.wikimedia.org/wikipedia/en/e/ec/The_Incredibles.jpg",
    "https://www.youtube.com/watch?v=eZbzbC9285I",
    2004)

finding_nemo = media.Movie(
    "Finding Nemo",
    "A dad fish needs to find his son.",
    "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
    "https://www.youtube.com/watch?v=wZdpNglLbt8",
    2003)

monsters_inc = media.Movie(
    "Monsters, Inc.",
    "Monsters must work together to get a girl back to her world.",
    "https://upload.wikimedia.org/wikipedia/en/6/63/Monsters_Inc.JPG",
    "https://www.youtube.com/watch?v=cvOQeozL4S0",
    2001)

toy_story_2 = media.Movie(
    "Toy Story 2",
    "The second movie about toys.",
    "https://upload.wikimedia.org/wikipedia/en/c/c0/Toy_Story_2.jpg",
    "https://www.youtube.com/watch?v=Lu0sotERXhI",
    1999)

a_bugs_life = media.Movie(
    "A Bug's Life",
    "A movie about bugs.",
    "https://upload.wikimedia.org/wikipedia/en/c/cc/A_Bug%27s_Life.jpg",
    "https://www.youtube.com/watch?v=vhGlMv3UCXA",
    1998)

toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life.",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc",
    1995)

# Store all Movie instances into "movies" list
movies = [finding_dory, the_good_dinosaur, inside_out, monsters_university,
          brave, cars_2, toy_story_3, up, wall_e, ratatouille, cars,
          the_incredibles, finding_nemo, monsters_inc, toy_story_2,
          a_bugs_life, toy_story]

# Open web page with movies
fresh_tomatoes.open_movies_page(movies)
