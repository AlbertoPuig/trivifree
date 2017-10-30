import sys
import requests
from requests.auth import HTTPDigestAuth
import json


Opts = 'Options'
url = "http://127.0.0.1:5000/trivifree/api/v1/quest/"
'''qid = 1'''

def get_question(question_id):

	try:
		response = requests.get(url + str(question_id))
		if response.status_code == 200:
			jData = response.json()
			'''print "_________________"
			print jData['OP1']
			print "_________________"'''
			'''return jData['OP1']'''
			return jData
		else:
			return None
	except Exception as ex:
		print "Error_____________________: " + str(ex)


def main():
	qid = 1
	answers_ok = 0
	while True:
	    '''a = raw_input("Enter a number between 1 and 3 or 0 to exit: ")'''
	    '''a = raw_input(question + '\n' + Opts + '\n' + get_question(2) + '\n' + Op2 + '\n' + Op3 + '\n')'''
	    qData = get_question(qid)
	    if qData is not None:
	    	a = raw_input(qData['QT'] + '\n' + Opts + '\n' + "1: " + qData['OP1'] + '\n' + "2: " + qData['OP2'] + '\n' + "3: " + qData['OP3'] + '\n')
	    	qid +=  1
	    	try:
	        	number = int(a)
	        	if number == 0:
	        		print 'bye'
	        		break
	        	else: 
	        		if (0 < number <= 3):
						print 'Its a correct answer'
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