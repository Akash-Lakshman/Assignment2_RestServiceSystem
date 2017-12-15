import os, sys, json, requests, time, getpass
from flask import Flask 
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class getRepos(Resource):
    def __init__(self):
        super(getRepos,self).__init__()
        global managerServer
        self.reqparser = reqparse.RequestParser()
        self.server = managerServer
        self.reqparser.add_argument('pullState', type=int, location = 'json')
        self.reqparser.add_argument('complexity', type=float, location='json')
    
    def get(self):
        args = self.reqparser.parse_args()
        if args['pullState'] == False:
           # print("hahaha")
            return {'repo': "https://github.com/Akash-Lakshman/Assignment_SC"}
        if args['pullState'] == True:
            self.server.currWorkerCount += 1
            if self.server.currWorkerCount == self.server.workerCount:
                self.server.start = time.time()  # Starting timer
            print("Work :",self.server.currWorkerCount)

api.add_resource(getRepos, "/repo", endpoint="repo")
        
#  API for obtaining commits and posting the cyclomatic results
class apiCyclomatic(Resource):
    def __init__(self):  # Upon initialisation of the class
        global managerServer  # Init the global server
        self.server = managerServer  # Init the global server
        super(apiCyclomatic, self).__init__()  # Initialising the Resource class
        self.reqparser = reqparse.RequestParser()

        self.reqparser.add_argument('commitSha', type=str, location = 'json')  # Repeat for multiple variables
        self.reqparser.add_argument('complexity', type=float, location='json')

    def get(self):
        if self.server.currWorkerCount < self.server.workerCount: # waiting for workers
            time.sleep(0.1)
            return {'sha': -2}
        if len(self.server.commitList) == 0:  # No more commits to give
            return {'sha': -1}
        X = self.server.commitList[0]  # commit val to give next commit in list
        del self.server.commitList[0]  
        print("Sent: {}".format(X))
        return {'sha':X}


    def post(self):
        args = self.reqparser.parse_args()  # parse the arguments from the POST
        print("Received sha {}".format(args['commitSha']))
        print("Received complexity {}".format(args['complexity']))
        self.server.CCList.append({'sha':args['commitSha'], 'complexity':args['complexity']})
        print(self.server.CCList)
        print(self.server.commitList)
        if len(self.server.CCList) == self.server.totalNumberOfCommits:
            endTime = time.time() - self.server.startingTime
            print(" Amount of time taken in seconds",(endTime))
            
            print(len(self.server.CCList))
            AvgCC = 0
            for x in self.server.CCList:
                if x['complexity'] > 0:
                    AvgCC += x['complexity']
                else:
                    print("Commit {} doesn't have a computable files".format(x['sha']))
            AvgCC = AvgCC / len(self.server.CCList)
            print(" CYCLOMATIC COMPLEXITY FOR THE REPOSITORY: ",AvgCC)
        return {'success':True}

api.add_resource(apiCyclomatic, "/cyclomatic", endpoint="cyclomatic")


class managerNode():
    def __init__(self):
        self.workerCount = input("Enter the number of worker nodes : ")
        self.workerCount = int(self.workerCount)
        self.currWorkerCount = 0    #Number connected to the managerNode
        #request repository info using the github API
        self.startingTime = 0.0
        self.CCList = [] 
        self.commitList = []  # List containing all commit sha values

        r = requests.get("https://api.github.com/repos/Akash-Lakshman/Assignment_SC/commits?page={}&per_page=100")
        jsonData = json.loads(r.text)

        for x in jsonData:
            self.commitList.append(x['sha'])
            print("Commits : {}".format(x['sha']))
        print("\n")
        self.totalNumberOfCommits = len(self.commitList)  # Total number of commits in repo
        
        print("Number of commits: {}".format(self.totalNumberOfCommits))


if __name__ == "__main__":
    managerServer = managerNode()  # initializing an instance of managerNode()
    app.run()
