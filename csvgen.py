import csv
import random

# create an empty csv file in directory, update name here
filename = 'movies_csv_file.csv'
# change min/max lines to desired amount
min_lines, max_lines = 25, 100
# change years of movies to generate
movie_year_min, movie_year_max = 1900, 2021

# clear prior contents of csv file
f = open(filename, "w+")
f.close()

# populations for random field generation
word_file = 'safedict_full.txt'
word_list = open(word_file).read().splitlines()
language_file = 'language_list.txt'
language_list = open(language_file).read().splitlines()

with open(filename, 'w', newline='') as csvfile:
    fieldnames = ['Title', 'Year', 'Languages', 'Rating Value']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    csv_rows = random.randrange(min_lines, max_lines, 1)
    line_count = 0
    for i in range(csv_rows):
        n = random.randrange(1, 5, 1)
        m = random.randrange(1, 3, 1)

        title = ' '.join(random.sample(word_list, m)).title()
        year = random.randrange(movie_year_min, movie_year_max, 1)
        languages = '[' + ';'.join(random.sample(language_list, n)) + ']'
        rating = round(random.uniform(1, 10), 1)

        writer.writerow({'Title': title, 'Year': year, 'Languages': languages, 'Rating Value': rating})
        line_count += 1

print("{file} was successfully generated with {count} rows of data.".format(file=filename, count=line_count))
