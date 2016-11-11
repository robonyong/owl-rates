from lxml import html
import requests
from models import Owl
# from pymongo import MongoClient

page = requests.get('http://www.audubon.org/birds-of-america?query=owl&sort_by=field_boa_plate_value&sort_order=ASC')
tree = html.fromstring(page.content)

owl_links = tree.xpath('//h4[@class="common-name"]/a/@href')

owl_names = tree.xpath('//h4[@class="common-name"]/a/text()')

print(owl_names)

# owl_images = tree.xpath('//img[@class="lazy" and not(contains(@src, "image_placeholder"))]/@src')

# for img in owl_images:
# 	img_arr = img.split("/")
# 	img_plate = img_arr[len(img_arr) - 1].split("?")[0]
# 	img_link = 'http://df0bd6h5ujoev.cloudfront.net/' + img_plate

for link in owl_links:
	owl_link = 'http://www.audubon.org' + link
	owl_page = requests.get(owl_link)
	owl_tree = html.fromstring(owl_page.content)
	owl_description = owl_tree.xpath('//section[contains(@class, "bird-guide-section") and contains(@class, "text-container")]')[0]
	owl_description = owl_description.text_content().replace('\r', '').replace('\t', '').replace('\xa0', '').split('\n')
	owl_description_arr = []
	for block in owl_description:
		block = block.strip()
		if (block == '' or block[:9] == 'Read more'):
			x = block
		else:
			owl_description_arr.append(block)

# print(owl_images)