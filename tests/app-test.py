import unittest
import requests
from ConfigParser import SafeConfigParser
import json


def load_properties(env, pproperty):
    try:
        parser = SafeConfigParser()
        parser.read('../conf/environ.properties')
        vproperty = parser.get(str(env), str(pproperty))
        return vproperty
    except Exception as ex_prop:
        print "Error______: " + str(ex_prop)

def load_data4tests(api_version):
    try:
        with open('data4tests.json', 'r') as f:
            data = json.load(f)
            try:
                data4tests = data['requests'][api_version -1]['data']
                return data4tests  
            except Exception as ex:
                print str(ex)
    except Exception as e:
            print str(e)



#data_respon = {u'OP2': u'Dublin', u'QT': u'The capital of Bulgaria is?', u'OP1': u'Sofia', u'CRT': u'op1', u'OP3': u'Kiev'}
url = load_properties('local','url')

class TestStringMethods(unittest.TestCase):
    def test_url(self):
    	param = '1'
    	response = requests.get(url + param) 	
     	self.assertEqual(response.status_code, 200)

    def test_url_response_content(self):
        param = '2'
        response = requests.get(url + param)
        self.assertEqual(response.json(), eval(load_data4tests(2)))

    def test_badparam(self):
    	param = 'string'
        response = requests.get(url + param)
        self.assertEqual(response.status_code, 400)

    def test_outofbound(self):
    	param = '100'
        response = requests.get(url + param)
    	self.assertEqual(response.status_code, 500)


if __name__ == '__main__':
    unittest.main()
		