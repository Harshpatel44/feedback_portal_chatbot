__author__ = 'Harsh Patel'
from textblob import TextBlob

testimonial = TextBlob("yes the problem here is different")
print(testimonial.sentiment)
def function(*argv):
    for arg in argv[1:]:
        print(arg[0])


#function(['harsh',1],['annu',2])