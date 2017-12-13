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
            return {'repo': "https://github.com/Akash-Lakshman/Assignment_SC"}
        if args['pullState'] == True:
            self.server.currWorkerCount += 1
            if self.server.currWorkerCount == self.server.workerCount:
                self.server.start = time.time()  # Starting timer
            print("Work :",self.server.currWorkerCount)

api.add_resource(getRepos, "/repo", endpoint="repo")
        


class managerNode():
    def __init__(self):
        self.workerCount = input("Enter the number of worker nodes : ")
        self.workerCount = int(self.workerCount)
        self.currWorkerCount = 0    #Number connected to the managerNode
        #request repository info using the github API
        self.startingTime = 0.0
        self.commitTotal = []  # List containing all commit sha values

        r = requests.get("https://api.github.com/repos/Akash-Lakshman/Assignment_SC/commits?page={}&per_page=100")
        jsonData = json.loads(r.text)

        for x in jsonData:
            self.commitTotal.append(x['sha'])
            print("Commits : {}".format(x['sha']))
        print("\n")
        self.totalNumberOfCommits = len(self.commitTotal)  # Total number of commits in repo
        print("Number of commits: {}".format(self.totalNumberOfCommits))


if __name__ == "__main__":
    managerServer = managerNode()  # initializing an instance of managerNode()
    app.run()
