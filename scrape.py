from lxml import html
import requests
import boto3
from PIL import Image
from slugify import slugify
import os, sys, urllib, io

from database.schemas import *
from app import create_app, db

Image.MAX_IMAGE_PIXELS = 10000000000000
s3 = boto3.resource('s3')

app = create_app()

page = requests.get('http://www.audubon.org/birds-of-america?query=owl&sort_by=field_boa_plate_value&sort_order=ASC')
tree = html.fromstring(page.content)

owl_links = tree.xpath('//h4[@class="common-name"]/a/@href')

owl_names = tree.xpath('//h4[@class="common-name"]/a/text()')

owl_images = tree.xpath('//img[@class="lazy" and not(contains(@src, "image_placeholder"))]/@src')

owl_images_hq = list()

for idx, img in enumerate(owl_images):
	img_arr = img.split("/")
	img_plate = img_arr[len(img_arr) - 1].split("?")[0]
	img_link = 'http://df0bd6h5ujoev.cloudfront.net/' + img_plate



# link = owl_images_hq[0]

# size = (250, 250)

# outfile = "tmp/owl_250.jpg"
# if link != outfile:
#     # try:
#     file = io.BytesIO(urllib.request.urlopen(link).read())
#     im = Image.open(file)
#     im.thumbnail(size)
#     im.save(outfile, "JPEG")

#     key = 'owls/owl_250.jpg'

#     s3.Object('owl-rates', key).put(Body=open(outfile, 'rb'))
#     os.remove(outfile)

    # except IOError:
    #     print("cannot create thumbnail for", link)

# for link in owl_links:
# 	owl_link = 'http://www.audubon.org' + link
# 	owl_page = requests.get(owl_link)
# 	owl_tree = html.fromstring(owl_page.content)
# 	owl_description = owl_tree.xpath('//section[contains(@class, "bird-guide-section") and contains(@class, "text-container")]')[0]
# 	owl_description = owl_description.text_content().replace('\r', '').replace('\t', '').replace('\xa0', '').split('\n')
# 	owl_description_arr = []
# 	for block in owl_description:
# 		block = block.strip()
# 		if (block == '' or block[:9] == 'Read more'):
# 			x = block
# 		else:
# 			owl_description_arr.append(block)
