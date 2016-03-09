Version control with Git
=============

What is version control?
-----------

Some ways in which you already have version control

  - http://www.phdcomics.com/comics/archive.php?comicid=1323
  - http://www.phdcomics.com/comics/archive.php?comicid=1531
  - Dropbox and its file version history 
  - "Track Changes" in Word
  
Today we will talk about the sort of version control that is used by programmers.
  
Getting started with Git
--------

Mac/Linux: open a Terminal window. Windows: run 'Git Bash'.

	$ git config --global user.name "Your Name"
	$ git config --global user.email "your.email@students.unibe.ch"
	$ git config --global push.default simple
	$ git config --global core.editor [YOUR EDITOR]
		TextMate: "mate -w"
		SublimeText Mac: "subl -n -w" 
		SublimeText Windows: "<DRAG EXE> -w"
		Notepad++: "<DRAG EXE> -multiInst -notabbar -nosession -noPlugin"
		Gedit: "gedit -s"
		
You shouldn't ever need to run these commands again - they tell Git who you are and which text editor you want to use to write your system messages.

Creating a repository
-----------

Git works in terms of *repositories*. To start using Git you make a directory (folder) into a repository, and Git keeps track of every change you ask it to track inside that folder. The folder can have files or other folders inside it. Usually a single repository corresponds to a single project - you might have one for your thesis, one for your class project in here, one for the files you have to keep track of for another class, etc.

So we'll set up our first repository. This means drawing on what we learned last time about our filesystem.

	$ pwd # see what directory (folder) you are in
	$ ls  # show what is in this directory (folder).

A good strategy is to decide now where on your computer you will keep the projects you track with Git. I personally keep mine in a folder in my home directory called 'Projects', but you are free to choose.

	$ mkdir ~/Projects
	$ cd ~/Projects
	
This `Projects` folder is *not* a Git repository! Never put one repository inside of another - Git will become quite confused that way. 

Now it is time to create our first repository. Remember that a repository starts life as a plain old directory. Go ahead and make a directory inside `Projects`. Let's call it `learngit`. Then we are going to move into that directory with the `cd` command, and check we are in the right place with the `pwd` command.

	$ mkdir learngit
	$ cd learngit
	$ pwd
	
OK - here is now to make a new repository.

	$ git init
	
Easy, huh? If you look at this folder in the Finder / Explorer window, or look at it using `ls`, it doesn't look any different. But if you run ls with a special argument:

	$ ls -a
	
you will see that this thing called `.git` is now there. This is where Git will do all the work of keeping track of what changes you make in here. 

Tracking changes
-------

Now it's time to put some stuff in here so that Git can track it!

Open your text editor and make a new text file. Write something (anything) in there, and then save the file into your repository. Call it `README.txt`. Then go back to the shell and run the command

	$ git status
	On branch master

	Initial commit

	Untracked files:
	  (use "git add <file>..." to include in what will be committed)

		README.txt

	nothing added to commit but untracked files present (use "git add" to track)


You will see a message that tells you a few things:

- Something something branch. That will come in handy later.
- Initial commit. You'll find out soon what a 'commit' is.
- Something about untracked files, including this file you just made.
- Another message that reiterates "use 'git add' to track". 

What that last bit is telling us is that we have to tell Git when we want it to start tracking something in the repository. We do this with the `git add` command. Then we can run `git status` again and see what has changed.

	$ git add README.txt
	$ git status
	On branch master

	Initial commit

	Changes to be committed:
	  (use "git rm --cached <file>..." to unstage)

		new file:   README.txt

You don't have to start a Git repository with an empty folder! If, after working with Git for a little while, you decide you want to use it to track some files you already have, you can also run `git init` in that directory and things will work just the same. All the files and folders that are already there will be listed as 'untracked' until you add them to be tracked.

Storing changes in commits
-----------

If you are used to something like Word, you know that once you turn on 'Track Changes' then that's all you have to do. Everything gets notices as you type it, and later you can go through and accept or reject them. The point there is to come to a final version of the document, and for the tracked changes ultimately to be included or discarded.

This is not how Git works. Instead, it thinks in terms of versions. You add what you want to track, and then when you're ready to make a version you commit. Every version—that is, every commit—has a message associated with it. This helps you keep track of what it was. Let's commit what we have now.

	$ git commit
	
Your text editor should have popped open, with some text in it - up at the top there, write a phrase or a sentence that describes what you changed. When you're done, save and close the editor. Back in your shell you should now see a message like this:

	[master (root-commit) 09be4b3] Hey it worked!
	warning: LF will be replaced by CRLF in README.md.
	The file will have its original line endings in your working directory.
	 1 file changed, 1 insertion(+)
	 create mode 100644 README.md
	
You will probably only see that 'warning' line if you are on Windows; don't worry too much about that. It's just telling you that Windows uses a different code when you press 'enter' in a text file than Mac and Linux does.

It takes some practice to get used to the cycle of `add` and `commit` that makes Git work. Mostly, think of `add` as "Whatever I just did in this file, I want that to be part of the next version" and `commit` as "OK, time to make the new version." When you are getting started it can seem weird and cumbersome to need two commands, but when you get the hang of it it can be useful, since it lets you make changes to files and directories even when you aren't yet ready to save them into a version.

We can see how this works by making changes to multiple files. Open your README and write something new in it somewhere. Save it, and then put a new file in the same directory. You can make another text file, or copy an image somewhere, or whatever you like. When you have done **both** these things, see what happens when you add only one!

	$ git add mynewfile
	$ git status	
	On branch master
	Changes to be committed:
	  (use "git reset HEAD <file>..." to unstage)

		new file:   unibern_logo_txp.png

	Changes not staged for commit:
	  (use "git add <file>..." to update what will be committed)
	  (use "git checkout -- <file>..." to discard changes in working directory)

		modified:   README

You see that your new file is listed as "to be committed" and the other is not. Go ahead and see what happens when you commit your changes. You can give the commit a message right on the command line, instead of waiting for the editor to open, by using the `-m` argument like so.

	$ git commit -m "Adding a new picture"
	$ git status
	[master d975ba1] made a change
	 1 file changed, 0 insertions(+), 0 deletions(-)
	 create mode 100644 unibern_logo_txp.png
	gs2-kps-pc247:learngit tla$ git status
	On branch master
	Changes not staged for commit:
	  (use "git add <file>..." to update what will be committed)
	  (use "git checkout -- <file>..." to discard changes in working directory)

		modified:   README

	no changes added to commit (use "git add" and/or "git commit -a")
	
Now we have two commits—two version—in our repository, but the changes to our README still haven't been saved!

This brings me to another point: **Git does not think in terms of files.** Rather, it thinks in terms of changes and commits. A *change* is a place in a file where something has changed. A *commit* is a snapshot of the entire repository. So in Git you make changes, you add those changes (usually by adding the file that contains the changes, though it is possible to add only selected changes within a file!), and then you commit a whole set of changes.

When you think you understand what you have seen, go ahead and commit those changes to your README.

	$ git add README
	$ git commit -m "Changed the README"
	

Back to the future: Seeing past commits
------------

Now that we have made several commits, how can we go back to a version we have saved before? 

You can use the `git log` command to see all the commits, that have got you to the point where you are now. It looks something like this:

	$ git log
	commit 42e925de226079e2bc7132bc04d03b3fad8b6766
	Author: tla <tla@mit.edu>
	Date:   Wed Mar 2 19:10:07 2016 +0100

	    changed the README

	commit d975ba1ea8764732fb216180e978f79662a20c0f
	Author: tla <tla@mit.edu>
	Date:   Wed Mar 2 19:07:21 2016 +0100

	    made a change

	commit 76304f50e8ff141ec308a6575ba09521062390b1
	Author: tla <tla@mit.edu>
	Date:   Wed Mar 2 19:05:08 2016 +0100

	    first post
		
I have made three commits; each one is listed out for me with a long ID, the author who made the commit (me), the date it was made, and the message that was written for it. With that information I can go back to any version I like by using these ID tag. (In fact, I only need to use the first 7-8 characters of the ID tag, and it will do what I want). Let's go back to the first commit we made, there at the bottom of the list:

	$ git checkout 76304f5
	Note: checking out '76304f5'.

	You are in 'detached HEAD' state. You can look around, make experimental
	changes and commit them, and you can discard any commits you make in this
	state without impacting any branches by performing another checkout.

	If you want to create a new branch to retain commits you create, you may
	do so (now or later) by using -b with the checkout command again. Example:

	  git checkout -b <new-branch-name>

	HEAD is now at 76304f5... first post
	
Okay that's a scary message. What it is saying is, you have gone back in the past, and it wouldn't be a good idea to commit anything new here until you know what you are doing. The `git status` command will remind you of this:

	$ git status
	HEAD detached at 76304f5
	nothing to commit, working directory clean
	
That `HEAD detached` thing means "be careful! You aren't looking at the present state of things." And indeed, if you look around:

	$ ls
	README
	
...that second file you added is now gone.

When you are ready to return to the present state of affairs, you use `checkout` again with the branch name. We haven't learned about branches yet, but for now you just need to remember that all repositories start with one branch, and that branch is called **master**. 

	$ git checkout master
	Previous HEAD position was 76304f5... first post
	Switched to branch 'master'
	$ ls
	README			unibern_logo_txp.png
	
Phew.

Remote repositories and Github
------------

The real reason people use Git, instead of just relying on Dropbox, to track changes in repositories is so that they can collaborate with others. Since you will all be working on a group project at the end of this term, this is relevant to you!

There are two well-known sites that host Git repositories; these are Github and Bitbucket. Github makes large-scale collaboration free and charges for private repositories; Bitbucket makes private repositories free and charges for repositories that want the collaboration of more than five people. In this class we will use Github, and you will all become members of the DHBern organization.

Once you have made a Github account and logged in, you can upload your 'learning Git' repository there. The first step is to create a repository on Github. Give it the same name as you gave the repository on your computer - in this case, `learngit`. Leave all the other options as they are. When it is created, you will get instructions for how to put things into it. In our case we have a *local* (meaning "on our own computer") repository already, and so this is how we sync it to Github (which, in Git parlance, is now the *remote*.) **IMPORTANT**: Make a note of the URL that Github has given you for this new repository.

	$ git remote add origin https://github.com/tla/learngit.git
	$ git push -u origin master

Now go look at your repository on Github (click its name there at the top of the page) and you will see your files there!

A Github repository is normally referred to in the wider world by a name like `tla/learngit` - essentially, the username of the owner and the name of the repository joined with a slash. This also serves as the Web address of a repository's page on Github, e.g. `https://github.com/tla/learngit`.

Once a repository is on Github, it means that if you lose the copy on your computer, you can get it back. Go ahead and delete your repository, like this

	$ cd ..
	$ pwd  # MAKE SURE you are in your Projects directory
	/Users/tla/Projects
	$ rm -rf learngit
	
Check in your Finder/Explorer window, if you like, to make sure that your repository folder is gone. Once you're sure, you can use that same URL you used in the `git remote add origin` command to get it back:

	$ git clone https://github.com/tla/learngit.git  # this is the same URL as above!

Now your repository, including the README and the other file you added, is in a folder inside `Projects` just like before. You can move into that folder and continue working however you like. Another point of terminology: the *origin* is the remote repository that holds the master copy of your work. In this case, that is the repository you just created on Github, and that you have now cloned back to your own computer.

You can also clone someone else's repository to your computer in the same way. For instance, the materials for this class are in Github in a repository known as `DHBern/TT2016` - that is, the repository named TT2016 and owned by the DHBern organization. Try it out:

	$ pwd    # You should still be in your Projects directory...
	/Users/tla/Projects
	$ git clone https://github.com/DHBern/TT2016.git
	
Now you have a README as well as a bunch of class lessons, including this one!
