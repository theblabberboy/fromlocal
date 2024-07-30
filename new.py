print("New things to learn")

print("Topic: add local repo to github")

#git init: to initalize new repository in git (go in the repo and type "git init")

#now we can add files in the folder

#after adding the files, to push this local repo to github, we have to create a repository in Github.
#(Don't add README.md or you have to sync it local system too)

#Before pushing we have to do:
#git remote add origin <-link->
#explanation: add in the remote repo. the name of the repo is "origin". we can give any other names (whatever) if we want, but we have
# to then be careful about the pushing command "git push origin main" to "git push whatever main"

#to check the remote: git remote -v

#to check branch: git branch (in which branch are we in)

#the concept of branch comes in, when multiple teams work on a same project. from the point where the team gets
#seperated the new branches are created!

#main is the parent branch in which the work intialises

#to rename a branch: git branch -M <new name>
#eg. git branch -M main

#after creation of al these we can use "git pupsh origin main"

#we can add a flag of "-u"
#"-u" mean: set upstream
#if we are working on a long project then we don't want to write "git push origin main" again and again
#so using the "-u" flag for the first time, will make "git push" work as "git push origin main"
#so for the first time instead of "git push origin main", we can use "git push -u origin main"