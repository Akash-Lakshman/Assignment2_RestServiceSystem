import os,sys,requests,json,subprocess  
 
if __name__ == '__main__':

    ip = input('Enter IP of Manager Node : ')
    port = input('Enter port number : ')
    link = 'http://'+ip+':'+port
    rURL = link + '/repo'
    cyclomaticURL = link + '/cyclomatic'
    commitsDone=0
    
    req = requests.get(rURL,json = {'pullState' : False})
    print(req.text)
    
    jsonData = json.loads(req.text)

    print(jsonData)

    URL = jsonData['repo']
    
    subprocess.call(["bash","pullScript.sh",URL])
    print(" end of segment!!! ")
    req = requests.get(rURL,json = {'pullState' : True})
    
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
            binaryCCVal = subprocess.check_call(["radon", "cc", "-s", "-a" , "repoData"])
            radonCCVal = CCVal.decode("utf-8")
            print(radonCCVal)
            avgCCStart = radonCCVal.rfind("(")

            if radonCCVal[avgCCStart+1:-2] == "":
                    
                print("No Files")
                r = requests.post(cycloURL, json={'commits': json_data['sha'], 'complexity': -1})
            else:
                avgCC = float(radonCCVal[avgCCStart+1:-2])  #Average cyclomatic complexity
                r = requests.post(cycloURL, json={'commits': json_data['sha'], 'complexity': avgCC})
            
            commitsDone += 1  #Commit count

    print("Commits Done: ", commitsDone)
