# json structure
# http://api.yandex.ru/maps/doc/geocoder/desc/concepts/response_structure.xml#json_response
# example http://geocode-maps.yandex.ru/1.x/?format=json&geocode=37.611,55.758&kind=house&results=1&lang=ru-RU
# http://jsonlint.com/
# example "37.611,55.758"
# "47.14,39.43"
# use in AppEngine

import pycurl
import cStringIO
import json

buf = cStringIO.StringIO()
coord="37.611,55.758"
acc="house"
resn="1"
c = pycurl.Curl()
c.setopt(c.URL, 'http://geocode-maps.yandex.ru/1.x/?format=json&geocode='+coord+'&kind='+acc+'&results='+resn+'lang=ru-RU')
c.setopt(c.WRITEFUNCTION, buf.write)
c.perform()
a = json.loads(buf.getvalue())
buf.close()

if a['response']['GeoObjectCollection']['metaDataProperty']['GeocoderResponseMetaData']['found']==0 : print "Found objects"

print a['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']


# b = json.loads(a)
# print b;
# for key, value in b.items():
# print key, value

