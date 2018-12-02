import io

import flickrapi
import json
import random

import tempfile
import os.path
import flickrapi
import requests
from io import BytesIO
import logging
from PIL import Image
import numpy as np


logging.basicConfig()


class Match(object):
    def __str__(self):
        return self.tile

    def __repr__(self):
        return self.__str__()
def get_flickr_image_by_keyword(keyword):

    logging.info("Getting {} from Flickr".format(keyword))
    flickr = flickrapi.FlickrAPI("6e939a9f2350e5edf34b14f2ccc9652d", "54d3b1560b1fb598", format='etree')
    result = flickr.photos.search(per_page=10000,
                                  text=keyword,
                                  tag_mode='all',
                                  content_type=1000,
                                  tags=keyword,
                                  extras='url_o,url_l',
                                  sort='relevance')
    # Randomize the result set
    img_url = None
    photos = [p for p in result[0]]
    while img_url is None and len(photos) > 0:
        photo = photos[0]
        img_url = photo.get('url_o') or photo.get('url_l')
        photos.pop()

    logging.info(img_url)

    if img_url is not None:
     img_file = requests.get(img_url, stream=True)
     return BytesIO(img_file.content)


if __name__ == '__main__':


    # input_image = sys.argv[1]
    for i in range(0,1000):
      keyword = random.choice(json.load(open('objects.json'))['objects'])
      input_image = get_flickr_image_by_keyword(keyword)
      if input_image is not None:
        image = Image.open(input_image)
        path="image"+"/"+str(i)+".bmp"

        image.save(path)


