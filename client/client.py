import sys
import requests
from requests.auth import HTTPDigestAuth
import json
from ConfigParser import SafeConfigParser


#load properties
def load_properties(env, pproperty):
	try:
		parser = SafeConfigParser()
		parser.read('../conf/environ.properties')
		vproperty = parser.get(str(env), str(pproperty))
		return vproperty
	except Exception as ex_prop:
		print "Error______: " + str(ex_prop)

#call to trivifree_api
def get_question(question_id):

	try:
		url = load_properties('local','url')
		response = requests.get(url + str(question_id))
		if response.status_code == 200:
			jData = response.json()
			return jData
		else:
			return None
	except Exception as ex:
		print "Error_____________________: " + str(ex)

#show data to user
def main():
	qid = 1
	answers_ok = 0
	Opts = load_properties('local','Opts')
	while True:
	    qData = get_question(qid)
	    if qData is not None:
	    	print (40*'-')
	    	print ('|' + 15*' ' + "TriviFree" + 14*' ' + '|')
	    	print (40*'-')
	    	a = raw_input(qData['QT'] + '\n' + Opts + '\n' + "1: " + qData['OP1'] + '\n' + "2: " + qData['OP2'] + '\n' + "3: " + qData['OP3'] + '\n')
	    	qid +=  1
	    	try:
	        	number = int(a)
	        	if number == 0:
	        		print 'Bye'
	        		break
	        	else: 
	        		if (0 < number <= 3):
						correct_answer = qData['CRT']
						correct_answer = int(correct_answer[-1:])
						print correct_answer
						print number
						print type(correct_answer)
						print type(number)
						if number == correct_answer:
							answers_ok += 1
							print str(answers_ok) + "***"
	        		else:
						print "Between 1 and 3 please"
	    	except Exception as e: 
	    		print str(e)
	        	print "Im sorry, please enter a number between 1 and 3"
	    else:
	    	print "End"
	    	print "Score: " + str(answers_ok)
	    	break

if __name__ == "__main__":
    main()