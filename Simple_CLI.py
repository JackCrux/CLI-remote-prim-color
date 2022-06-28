import urllib.parse

import urllib.request

def submitInformation(url,parameters):
    encodedParams = urllib.parse.urlencode(parameters).encode("utf-8")
    req = urllib.request.Request(url)
    net = urllib.request.urlopen(req,encodedParams)
    print(net.read())
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

     parameters = {'color':'red'}
     info = submitInformation(enter_url,parameters)

if (user == "2"):

     parameters = {'color':'blue'}
     info = submitInformation(enter_url,parameters)

if (user == "3"):

     parameters = {'color':'green'}
     info = submitInformation(enter_url,parameters)

else:

     exit()
