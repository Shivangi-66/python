"""
collection- grouping of items in a collection
counter- a container which tracks frequency of values , it can hold anything
"""
import collections

co1=collections.Counter(['C','L','E','O','P','A','R','T'])
co2=collections.Counter('JULIUS CAESAR')

print(co1)
print(co2)

print("addititon in",co1 + co2)
print("subtraction",co1 -co2)
print("union n",co1 | co2)
print("intersection n",co1 & co2)