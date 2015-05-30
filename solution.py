# Here my task is to scrape all pdf files from the given url - http://trai.gov.in/Content/PressReleases.aspx and to download it to a user intended location.

# Usage: python solution.py || sudo python solution.py
# Expected output: Pdf's will be downloaded to the mentionied location

from BeautifulSoup import *
import urllib2
import urllib
import re
from selenium import webdriver
import time
from pyvirtualdisplay import Display
import os

# This function will hide all selenium browsers that will open 
display = Display(visible=0, size=(800, 600))
display.start()

# List of all pdf's
pdf_list=[]

# List of all Java Script's
script_id=[]	

# All links to crawl!
all_links=[]

# Count of pdf files
count_pdf=0

######################################################################################################
######################################################################################################

# Aim: To crawl pdf's inside a particular link

def find_pdf(new_link):

	global count_pdf

	try:
		#Opening link after testing beautiful soup
       		new_soup=BeautifulSoup(urllib2.urlopen(new_link))

       	# Not a valid link
	except:
		#Move on if the link is not valid
       		pass
	else:
		#Find all html links from the source code
       		temp_links=new_soup.findAll("a",href=True)

		#print(temp_links)

		#Finding pdf's from those links, since pdf's are linked 
			
		for pdf in temp_links:

			#print(new_links['href'])
			
			#Finding pdf from source code

			if('.pdf' in pdf['href']):
				
				#In some cases complete http link is not given

				if('http' not in pdf['href']):

					#Adding base url to extract complete link
					new_pdf= base+pdf['href']
				else:
					new_pdf=pdf['href']

				#Adding pdf to the pdf list and incrementing count
				if(new_pdf not in pdf_list):
					#print(new_pdf)
					#outputfile.write(new_pdf)
					#outputfile.write("\n")

					pdf_list.append(new_pdf)
					count_pdf=count_pdf+1

###########################################################################################################

#Executing Java Script

def script_execute(link):
	
#	print("\n"+link['href']+"\n")
	
	#Here in the TRAI website, all the pages were linked through paging hence extract all javascripts

	if("Paging" in link['id']):
		#print("\n"+link['id']+"\n")

		#Checking if script was already visited or not

		if(link['id'] not in script_id):
			
			#print("\n"+link['id']+"\n")
	
			#Clicking script through selenium

			driver.find_element_by_id(link['id']).click()

			#Sleeping to allow page to load, this can be modified according to the internet connecting
			time.sleep(1)

			#Extractign source code and editing it
			html=driver.page_source
			test_soup=BeautifulSoup(html)
			#outputfile1.write(str(test_soup))
			#find_pdf(baseurl)

			#Adding script to script list
			script_id.append(link['id'])
			
			#Finding new links in the newly opened page
			test_links=test_soup.findAll("a",href=True)

			for test_link in test_links:

				#If link was not visited before
				if(test_link not in all_links):

					#Adding new links to the link list
					all_links.append(test_link)


					#We do not wish to visit external urls or control url or new scripts
					if('http' in test_link['href'] or '#' in test_link['href'] or 'script' in test_link['href']):
						#print("\nFlag\n")
						pass
	
					else:	
										
						#If the complete url was not mentoned here
						new_test_link=base+test_link['href']

						#print(new_test_link)
		
						#Calling function to find pdf's
						find_pdf(new_test_link)


######################################################################################################
######################################################################################################

#outputfile=open("temp1.txt",'w')
#outputfile1=open("temp_soup.txt",'w')

#Url you wish to crawl
baseurl="http://trai.gov.in/Content/PressReleases.aspx"

#Main website link
base="http://trai.gov.in"
soup = BeautifulSoup(urllib2.urlopen(baseurl))

#Finding all links from source code
links=soup.findAll("a",href=True)

print("\n\t Crawling PDF's! \n")

#Selenium browser, please change accordingly in case you do not have Firefox installed
driver = webdriver.Firefox()
driver.get(baseurl)

#Crawling through all the links
for link in links:

	#If link was not visited before
	if(link not in all_links):
		
		#Adding link to link list	
		all_links.append(link)		

		#We do not wish to visit external urls or internal navigations
		if('http' in link['href'] or '#' in link['href']):
			#print("\nFlag\n")
			pass
	
		else:	

			#Executing scripts seperately
			if('script' in link['href']):
				script_execute(link)
				#json.loads(link['href'])
				#print("\nFlag\n")

			else:		
				#If complete url was not mentioned here
				new_link=base+link['href']
	
			#Calling function to extract pdf's
			find_pdf(new_link)

#Closing selenium browsers
display.stop()
driver.quit()


#please replace raw_input with input, if using python 3.x 
choice = raw_input("\n\tTotal "+str(count_pdf)+" pdf's found, do you wish to download all the files? (Y/N): ")

#Downloading files

def download(pdf_list):

	#current_path=os.system('pwd')		

	#please replace raw_input with input, if using python 3.x, make sure to enter the complete final name start from the root here

	directory=raw_input("\n\tPlease enter the complete path (pwd), where you wish to download all the files: ")
	original_directory=directory
	
	#directory=raw_input("\nPlease enter the directory name, where you wish to download all the files: ")
	#directory=current_path+"/"+directory

	

	#if not os.path.exists(directory):
    	#		os.makedirs(directory)

	#os.chdir(directory)

	#please replace raw_input with input, if using python 3.x, here users can download files in the same directory or as stated on the website

	same_dir=raw_input("\n\tDownload all files in the same directory? (Y/N): ")
	
	if(same_dir=='Y' or same_dir=='y'):
		
		print("\n\tDownloading!!\n")

		#Creating the directory, where the user wishes to save files

		if not os.path.exists(directory):
		    os.makedirs(directory)

		#Changing directory

		os.chdir(directory)

		#Downloading files one by one from the pdf list

		for pdf in pdf_list:
			split_url=pdf.split('/')
			urllib.urlretrieve(pdf,split_url[len(split_url)-1])				
	
	#In case the user wishes to download files as it is

	else: 
		print("\n\tDownloading!!\n")

		#Downloading files one by one

		for pdf in pdf_list:
			url=pdf

			#Here individual folders will be created as stated in the url seperated by /			
	
			temp=url.replace('://','_') #http://
			split_url=temp.split('/')
		
			i=1

			while(i<len(split_url)):
				#print(temp1[i])

				if(i<len(split_url)-1):	
		
					directory=directory+"/"+split_url[i]

					#Create sub directories as mentioned in url

					if not os.path.exists(directory):
					    os.makedirs(directory)

				os.chdir(directory)
				i=i+1

			filename=split_url[i-1]
			urllib.urlretrieve (url,filename)
			directory=original_directory

if(choice=='Y' or choice=='y'):
	#print("\n\tDownloading!!\n")
	download(pdf_list)
else:
	print("\n\n\tThank you!")

print("\n\n\tThank you!")
