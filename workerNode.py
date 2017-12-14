import os,sys,requests,json,subprocess  
 
def exec(): 
 
    ip = input('Enter IP of Manager Node : ')
    port = input('Enter port number : ')
    link = 'http://'+ip+':'+port
    rURL = link + '/repo'
    cyclomaticURL = link + '/cyclomatic'
    commits=0
    
    req = requests.get(link,json = {'pullState' : False})
    
    jsonData = json.loads(req.text)

    print(jsonData)

    URL = jsonData['repo']
    
    subprocess.call(["bash","pullScript.sh",URL])
    print(" end of segment!!! ")
    req = requests.get(link,json = {'pullState' : True})
    
    
if __name__ == "__main__":
    exec()
