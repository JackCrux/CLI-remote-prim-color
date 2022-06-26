import urllib.parse

import urllib.request

def submitInformation(url,parameters):
    encodedParams = urllib.parse.urlencode(parameters).encode("utf-8")
    req = urllib.request.Request(url)
    net = urllib.request.urlopen(req,encodedParams)
    return(net.read())

print("""

select your color

[1] red
[2] blue
[3] green

""")

enter_url = input("enter url : ")

user = input("enter value : ")

if (user == "1"):

     print("Prim remotely changed colors to Red.")
     parameters = {'color':'red'}
     info = submitInformation(enter_url,parameters)

if (user == "2"):

     print('Prim remotely changed colors to Blue.')
     parameters = {'color':'blue'}
     info = submitInformation(enter_url,parameters)

if (user == "3"):

     print("Prim remotely changed colors to Green.")
     parameters = {'color':'green'}
     info = submitInformation(enter_url,parameters)

else:

     exit()
