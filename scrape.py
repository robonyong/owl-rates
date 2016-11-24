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

app = create_app('config.py')

sizes = {
	'1024': (1024, 1024),
	'600': (600, 600),
	'250': (250, 250)
}

page = requests.get('http://www.audubon.org/birds-of-america?query=owl&sort_by=field_boa_plate_value&sort_order=ASC')
tree = html.fromstring(page.content)

owl_links = tree.xpath('//h4[@class="common-name"]/a/@href')

owl_names = tree.xpath('//h4[@class="common-name"]/a/text()')

owl_images = tree.xpath('//img[@class="lazy" and not(contains(@src, "image_placeholder"))]/@src')

owls = []

for idx, owl_name in enumerate(owl_names):
	owl_link = 'http://www.audubon.org' + owl_links[idx]
	new_owl = Owl(name=owl_name, slug=slugify(owl_name, max_length=24), nas_link=owl_links[idx])
	db.session.add(new_owl)
	owls.append(new_owl)

for idx, img in enumerate(owl_images):
	img_arr = img.split("/")
	img_plate = img_arr[len(img_arr) - 1].split("?")[0]
	img_link = 'http://df0bd6h5ujoev.cloudfront.net/' + img_plate

	slug = slugify(owl_names[idx], max_length=24)
	outfile = 'tmp/' + slug + '.jpg'

	try:
		file = io.BytesIO(urllib.request.urlopen(img_link).read())
		im = Image.open(file)

		for key in sizes:
			filename = slug + '_' + key + '.jpg'
			tmp_file = ''.join(('tmp/', filename))
			tmp_im = im.copy()
			tmp_im.thumbnail(sizes[key], Image.ANTIALIAS)
			tmp_im.save(tmp_file)

			aws_key = ''.join(('owls/', filename))
			s3.Object('owl-rates', aws_key).put(Body=open(tmp_file, 'rb'))
			os.remove(tmp_file)
			aws_link = ''.join(('https://s3-us-west-1.amazonaws.com/owl-rates/', aws_key))
			prop = 'image'
			if key == '600':
				prop = 'image_web'
			elif key == '250':
				prop = 'image_thumbnail'
			owl = owls[idx]
			setattr(owl, prop, aws_link)

	except IOError: 
		print("cannot create files for", img_link)

for idx, link in enumerate(owl_links):
	owl_link = 'http://www.audubon.org' + link
	owl_page = requests.get(owl_link)
	owl_tree = html.fromstring(owl_page.content)
	owl_description = owl_tree.xpath('//section[contains(@class, "bird-guide-section") and contains(@class, "text-container")]')[0]
	owl_description = owl_description.text_content().replace('\r', '').replace('\t', '').replace('\xa0', '').split('\n')

	for index, block in enumerate(owl_description):
		block = block.strip()
		if (block == '' or block[:9] == 'Read more'):
			pass
		else:
			owl_id = idx + 1
			new_description = OwlDescription(description=block, idx=index, owl_id=owl_id)
			db.session.add(new_description)

db.session.commit()
