import http.client
import json
import termcolor
from Seq import Seq

PORT = 80
SERVER = 'rest.ensembl.org'

conn = http.client.HTTPConnection(SERVER, PORT)
conn.request("GET", "/homology/symbol/human/FRAT1?content-type=application/json")
r1 = conn.getresponse()
print('Response received: {}\n'.format(r1.status, r1.reason))
data1 = r1.read().decode('utf-8')
response = json.loads(data1)
id = response['data'][0]['id']

conn.request('GET', '/sequence/id/'+id+'?content-type=application/json')
r1 = conn.getresponse()
data1 = r1.read().decode('utf-8')
response = json.loads(data1)

DNAsequence = response['seq']


s1 = Seq(DNAsequence)
print('Bases in FRAT1: ', len(DNAsequence))
print("Number of T's in FRAT1 gen:", s1.count('T'))

if s1.count('A')> s1.count('C') and s1.count('A')>s1.count('T') and s1.count('A')>s1.count('G'):
    termcolor.cprint('The base most popular in FRAT1 is: A','green')
    print('The percentage of the most popular base is:'+str(s1.perc('A')),'green')

elif s1.count('C')> s1.count('A') and s1.count('C')>s1.count('T') and s1.count('C')>s1.count('G'):
    termcolor.cprint('The base most popular in FRAT1 is: C','green')
    print('The percentage of the most popular base is:'+str(s1.perc('C')),'green')

elif s1.count('T')> s1.count('C') and s1.count('T')>s1.count('A') and s1.count('T')>s1.count('G'):
    termcolor.cprint('The base most popular in FRAT1 is: T','green')
    termcolor.cprint('The percentage of the most popular base is:'+str(s1.perc('T')), 'green')

else:
    termcolor.cprint('The base most popular in FRAT1 is: G','green')
    termcolor.cprint('The percentage of the most popular base is:'+str(s1.perc('G')), 'green')

print('The percentage of the base A is:', s1.perc('A'))
print('The percentage of the base C is:', s1.perc('C'))
print('The percentage of the base T is:', s1.perc('T'))
print('The percentage of the base G is:', s1.perc('G'))

