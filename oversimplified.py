
import urllib.parse
import urllib.request

def submitInformation(url,parameters):
    encodedParams = urllib.parse.urlencode(parameters).encode("utf-8")
    req = urllib.request.Request(url)
    net = urllib.request.urlopen(req,encodedParams)
    return(net.read())

url =  "http://simhost-00d19634d4816ce28.agni.secondlife.io:12046/cap/7d1b564f-4630-1d60-23e3-5917bc3d9f75"

print("""

select your color

[1] red
[2] blue
[3] green

""")

user = input("enter value : ")

if (user == "1"):

     print("Prim remotely changed colors to Red.")
     parameters = {'color':'red'}
     info = submitInformation(url,parameters)

if (user == "2"):

     print('Prim remotely changed colors to Blue.')
     parameters = {'color':'blue'}
     info = submitInformation(url,parameters)

if (user == "3"):

     print("Prim remotely changed colors to Green.")
     parameters = {'color':'green'}
     info = submitInformation(url,parameters)

else:

     exit()




