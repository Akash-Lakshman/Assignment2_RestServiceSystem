# Assignment2_RestServiceSystem
Computation of Cyclomatic complexity for a given repository via a Rest Service System.


# Software Dependencies

>>  Python, requests, Flask, Flask-RESTful, radon, Python terminal to execute the code

>> GIT repository used is https://github.com/Akash-Lakshman/Assignment_SC

# CONFIG and EXECUTION

>> Download the Repository, There needs to be an empty folder RepoData as per the repository, Navigate to ~/Assignment2_RestServiceSystem

>> Run the managerNode.py code in a terminal. using python managerNode.py and the default localhost will run the code on PORT 5000. Once started it will request number of nodes. Put respective input

>> Depending number of Nodes put run those many worker nodes in seperate terminals by running the file workerNode.py in each of ther terminal. For eg if the number of nodes is 2 then two workerNodes in 2 terminals must be opened. 

>> Provide the same IP & Port as the one that is running the managerNode. That will pick up the respective repository and execute the code to find the Cyclomatic Complexity using RESTFul services.

>> The worker Code polls the manager till required Worker Nodes are matched. once its done a timer is started and the workers request for commits, compute the average cyclomatic complexity for that poarticular commit and respond to the manager node with the results. Once commits are completed, timer is stopped to calculate the total time and the Average complexity.

# Note
If you want to use a different repository change the same in the manager Node
