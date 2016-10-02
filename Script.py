#!/usr/bin/env python
import json
products = []
result = {}
#Create the List of Listings
with open ('products.txt') as productsFile:
	for line in productsFile:
		products.append(line)
		entry = json.loads(line)
		result[entry['product_name']] = []
with open ('listings.txt') as listingsFile:
	for line in listingsFile:
		listing = json.loads(line)
		#print "%s" %listing["manufacturer"]
		for product in products:
			entry = json.loads(product)
			if(listing["manufacturer"].lower() == entry["manufacturer"].lower()):
				if ("for" not in listing["title"] and entry["model"] in listing["title"] ):
					#print "%s & %s" % (listing["title"].encode('utf-8'), entry["product_name"].encode('utf-8'))
					result[entry['product_name']].append(line)
					continue
				else:
					newTitle = listing["title"].split("for",1)[0]
					if(entry["model"] in newTitle):
						result[entry['product_name']].append(line)
						#print "%s & %s" % (listing["title"].encode('utf-8'), entry["product_name"].encode('utf-8'))
						
					continue	
for i in result:
	print '{"product_name": %s "listings": %s}' %(i,result[i])

			



	#print "Data: %s" %data
#listings = open("listings.txt", 'r')
#products = open("products.txt", 'r')
