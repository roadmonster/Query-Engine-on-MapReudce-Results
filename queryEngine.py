#!/usr/bin/env python
import csv
import operator

def load():

	data = {}
	with open("tfidf.csv", "r") as infile:
		reader = csv.reader(infile)
		for row in reader:
			data[row[0]] = {}
			data[row[0]][row[1]] = row[2]
	return data


def getScore(doc, query, data):

	score = 0

	for word in query:
		lowered = word.lower()
		term = filter(lambda c: 97 <= ord(c) <= 122, lowered)
		if len(term) > 0:
			try:
				score += data[doc][word]
			except KeyError:
				score += 0

	return score/len(query)


def main():

	data = load()
	again = True
	print "Query: "
	while again:
		results= {}
		query = raw_input().strip().split()

		for key in data:
			score = getScore(key, query,data)
			results[key] = score

		sorted_result = dict( sorted(results.items(), key=operator.itemgetter(1),reverse=True))

		new_result = {}
		
		keys = sorted_result.keys()[:5]
		print sorted_result[keys[0]]
		print sorted_result[keys[1]]
		print sorted_result[keys[2]]
		print sorted_result[keys[3]]
		print sorted_result[keys[4]]		


		again = False

		print "Query:"
		query = raw_input().strip().split()
		if(len(query) > 0):
			again = True


if __name__ == "__main__":
	main()
