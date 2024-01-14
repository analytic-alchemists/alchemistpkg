# How to contribute to the repository

## Steps

Click Fork to make your own copy of the repository.

![Screenshot 2024-01-11 125536](https://github.com/mschumak/alchemistpkg/assets/3884360/e9b35a0a-f7a5-4816-9b3a-d9b23a4dd459)

Go to your fork and click the Code button to get the clone link.

![Screenshot 2024-01-11 125658](https://github.com/mschumak/alchemistpkg/assets/3884360/5b7efbe5-568c-4583-96ec-288c2249aa39)

Open a terminal on your computer and change to a directory to work in.

Enter commands:

> git clone git@github.com:<your-account>/alchemistpkg.git

> cd alchemistpkg

> git checkout -b <your-working-branch-name, for example dir-struct-01-11>

Work on the code!

> git add <files to commit>

> git commit -m "commit message"

> git push origin <your-working-branch-name>

Go to the group's repository on Github. You will likely see a message that you have changes ready. Click the Compare & pull request button.

![Screenshot 2024-01-11 184642](https://github.com/mschumak/alchemistpkg/assets/3884360/98b30d3d-d683-4171-b263-f1a36f07217d)

Enter information about your pull request. Assign a reviewer. 
The main branch of the group's repository is set up so that at least one reviewer is required to merge any pull request.

![Screenshot 2024-01-11 185117](https://github.com/mschumak/alchemistpkg/assets/3884360/8bdf8737-b36f-44c1-85a2-681a58d232cd)

Your pull request doesn't have to fully resolve an Issue, but if it does, and the Issue should be closed after the pull request is merged, 
go to the list of Issues and select the Issue.

![Screenshot 2024-01-11 185545](https://github.com/mschumak/alchemistpkg/assets/3884360/fbb7e4b5-65b9-48c1-8c81-d32381077c06)

At the bottom right, click on Link a branch or pull request, and select the top item.

![Screenshot 2024-01-11 185731](https://github.com/mschumak/alchemistpkg/assets/3884360/b03b077f-8ea1-482e-8cea-4533852749f8)

Find your pull request and select it.

![Screenshot 2024-01-11 185839](https://github.com/mschumak/alchemistpkg/assets/3884360/a9d64d30-256a-4513-a360-67569c559bf4)

The main branch of the group repository requires at least one reviewer to merge the pull request. Discuss the changes with your reviewer.
You can make changes to your pull request by committing and pushing changes to the branch in your repository!

![Screenshot 2024-01-11 190916](https://github.com/mschumak/alchemistpkg/assets/3884360/400bc301-90b0-4dbf-b500-5b3be7bca612)

How do you update your fork after your or someone else's pull request has been merged?

Click "Sync fork" on your repository main branch.

On your terminal on your computer, enter commands:

> git checkout main

> git pull

If you have work in progress, checkout your working branch:

> git checkout <your-working-branch-name>

Then enter command:

> git pull origin main

This might result in having to merge code. 

# Testing Pull Requests

To test a pull request before merging it with the main branch, you can clone the repository
to a temporary location on your computer and switch to a local branch containing the pull request code.

## Steps

Go to a temporary directory in your terminal and clone the organization repository:

> git clone git@github.com:analytic-alchemists/alchemistpkg.git

Fetch the pull request code and put it in a local branch on your computer:

> cd alchemistpkg

> git fetch origin pull/<number>/head:<your chosen branch name>

> git checkout <your chosen branch name>

> cd ..

Make sure the package in uninstalled:

> pip uninstall alchemistpkg

Install the new code as a package:

> pip install ./alchemistpkg

Run your test file.

