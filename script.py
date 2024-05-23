# import urllib
# use urllib.request to get data from the url.
# write a function that takes a url
# return a response.

import urllib.request as urllib


def main(url):
    print("Checking Connectivity ...")
    response = urllib.urlopen(url)
    print("connected to ", url, " Successfully!")
    print("The response code was: ",response.getcode())

print("This is a site connectivity checker programme!!")
input_url = input("Input the url of the site you want to check: ")
main(input_url)