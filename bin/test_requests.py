import requests
from xml.etree import ElementTree
URL = 'https://beacon.nist.gov/rest/record/last'
class RandomnessBeacon():
    def __init__(self,url):
        self.url = url
        self.r = requests.get(self.url)
        self.tag_output_value = None

    def get_output_value_tag(self):
        if self.r.status_code == 200:
            self.tree = ElementTree.fromstring(self.r.content)
            self.tag_output_value = self.tree[6].text

    def get_result(self):
        if not self.tag_output_value is None:
            self.unique_letters = set(list(self.tag_output_value))
            for i in self.unique_letters:
                print "{0:s},{1:d}".format(i,self.tag_output_value.count(i))

if __name__=='__main__':
    random_beacon = RandomnessBeacon(URL)
    random_beacon.get_output_value_tag()
    random_beacon.get_result()