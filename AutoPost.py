# Importing the modules used
from instabot import Bot 
from PIL import Image
import urllib.request
import random

# Defining the variables
file_name = 'Image1'
hashtags = ''
url = ''
quote = ''
uername = ''
password = ''
number = 0
quoteList = []
urlList = []
hashtagList =[]
bot = Bot()

# Creating the lists based off the .txt files 
with open('hashtags.txt', 'r') as f:
	hashtag1 = f.readlines()
	hashtagList = eval(hashtag1[0])
	hashtaglList = list(dict.fromkeys(hashtagList))

with open('image.txt', 'r') as f:
	url1 = f.readlines()
	urlList = eval(url1[0]) 
	urlList = list(dict.fromkeys(urlList))

with open('quote.txt', 'r') as f:
	quote1 = f.readlines()
	quoteList = eval(quote1[0]) 
	quoteList = list(dict.fromkeys(quoteList))

# Defining the variables based off random items from lists
number = random.randint(0, len(hashtagList) - 1)
hashtags = hashtagList[number]

number = random.randint(0, len(urlList) - 1)
url = urlList[number]

number = random.randint(0, len(quoteList) - 1)
quote = quoteList[number]

# Downloading the image into the 'images' folder
def dl_jpeg(url, file_path, file_name):
	full_path = file_path + file_name + '.jpg'
	urllib.request.urlretrieve(url, full_path)

dl_jpeg(url, 'images/', file_name)

# Cropping the image to its always under a square and 1080p or under
img = Image.open('images/Image1.jpg')

if img.width > 1080:
	if img.height > 1080:
		if img.height > img.width:
			baseHeight = 1080
			hpercent = (baseHeight/float(img.size[1]))
			hsize = int((float(img.size[0])*float(hpercent)))
			img = img.resize((hsize,baseHeight), Image.ANTIALIAS)
			img.save('images/Image1.jpg')
		else:
			basewidth = 1080
			wpercent = (basewidth/float(img.size[0]))
			hsize = int((float(img.size[1])*float(wpercent)))
			img = img.resize((basewidth,hsize), Image.ANTIALIAS)
			img.save('images/Image1.jpg')

if img.width != img.height:
	if img.width > img.height:
		new_width = img.height
		new_height = img.height
		left = (img.width - new_width)/2
		top = (img.height - new_height)/2
		right = (img.width + new_width)/2
		bottom = (img.height + new_height)/2
		img = img.crop((left, top, right, bottom))
		img.save('images/Image1.jpg')
	else:
		new_width = img.width
		new_height = img.width
		left = (img.width - new_width)/2
		top = (img.height - new_height)/2
		right = (img.width + new_width)/2
		bottom = (img.height + new_height)/2
		img = img.crop((left, top, right, bottom))
		img.save('images/Image1.jpg')

# Asking the user for their login
username = input('What is your username?\n-')
password = input('\nWhat is your password?\n-')

# Logging into page and uploading 
bot.login(username = username, password = password)
bot.upload_photo(photo = "images/Image1.jpg",  caption = str(quote) + ' -- ' + str(hashtags))

