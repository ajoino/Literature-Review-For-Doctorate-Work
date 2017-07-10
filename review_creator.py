from os import listdir
from os.path import isfile, join
filenames = [f for f in listdir('reviews/') if isfile(join('reviews/', f))]

"""
with open('reviews/Turney2006Similarity.tex') as file:
	data = file.read()
"""	

all_data = ""

for filename in filenames:
	with open('reviews/' + filename) as file:
		all_data = all_data + file.read()
		
with open('all_reviews.tex','w') as write_file:
	write_file.write(all_data)