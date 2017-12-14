#!/bin/bash

echo "URL $1"
cd repoData # A directory created in the same folder as the code for getting the repository to this location and doing init
rm -rf .git/ 
echo "Old Stuff Removed"
git init
git remote add origin $1
git pull
