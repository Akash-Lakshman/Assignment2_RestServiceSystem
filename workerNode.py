import os,sys,requests,json
 
def exec(): 
 
    ip = input('Enter IP of Manager Node : ')
    port = input('Enter port number : ')
    link = 'http://'+ip+'/'+port+'/repo'
    req = requests.get(link,json = {'pullState' : False})
    jsonData = json.loads(requests.text)
    print(jsonData)

    reposURL = jsonData['repo']
    req = requests.get(link,json = {'pullState' : True})
    
    
if __name__ == "__main__":
    exec()
