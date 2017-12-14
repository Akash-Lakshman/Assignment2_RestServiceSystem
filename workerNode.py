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
    
    while True:
        cyclo = requests.get(cyclomaticURL)
        print("Got Cyclomatic",cyclo)
        json_data = json.loads(cyclo.text)
        print(json_data)
        print("Received: ",json_data['sha'])
        if json_data['sha'] == -2:       # Polling for manager to give commits
            print("Polling")
        else:
            if json_data['sha'] == -1:
                print("END, Nothing Remaining")
                break
            subprocess.call(["bash", "getCommit.sh", json_data['sha']])
    
if __name__ == "__main__":
    exec()
