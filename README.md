# WebScraper

1) Run the shell script ./install for the first use and then run the python file solution.py using python solution.py

Please ensure that you have root access 

2) The code was developed in Ubuntu 12.04 having python 2.7 and firefox browser; minor changes have to be made to scale it to other systems

3) Please ensure that you have a steady internet connection; and you may have to run the code multiple times in case a connection error\ results

Method:

1) Extracting from a given webpage

The TRAI website had a lot of hidden urls, so I used urllib to open a website and to find links using beautlful soup
But then, I came across javascripts. Here the url remained same, but the content changed; which was again a dilemna

2) Parsing Javascripts

I used selenium to parse javascripts, then I crawled for pdfs in the new links too.
Selenium opens browser to parse script, so I found out a method to hide all the browsers which were opened and to 
close it after I was done with my task

3) Downloading files

I had saved pdf urls in a list, I ran a for loop to download pdfs one by one using urlretrieve, Here new directories will be 
created as per details mentioned on the url

 
#References:

Stack overflow!
