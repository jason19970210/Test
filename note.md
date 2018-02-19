# Python3

# GitHub

>> Working direction   > git add >   Staging Area   > git commit >   Repository
								<<  git checkout  <<  


	> git 							// get help of git command
	> git init						// create a new repository (repo)
	> git clone						//
	> git \s 						// get status
	> git add <file name>			//
	> git commit -m "..."			// give description to the file
	> git push						// 
	> git push origin master
	> git push origin branch_name 	// 上傳分支到 origin node
	> git push --set-upstream origin branch_name
	> git push -f 					// or call git push --force
	> git pull						// update local version from github     >>> git pull = git fetch + git merge
	> git add .						// add all the files without a commit
	> git add --all 				//
	> git commit -am "..." 			// add everything and give the commit
	> git log 						// show all the commits overtime
		> git log -p -2 			// 顯示每個更新之間差別的內容, 限制為只輸出最後兩個更新
		> git log --stat 			// 檢視每個更新的簡略統計資訊
		> git log --oneline 		//
	> git checkout -b branch_name 	// create a new branch and switch to it
	> git branch 					// show the branches
		> git branch branch_name
		> git branch -D branch_name
	> git branch --delete branch_name // delete the branch
	> git checkout branch_name 		// change the branch to the other one
	> git push -u origin master
	
	> git remote add origin			// 新增遠端節點
		> git remote rm origin		// 刪除遠端節點
	> git remote -v 				// 檢視遠端節點
	> git push origin :branch_name 	// 刪除遠端分支

	> git stash save 				// 將目前狀況存下來
	> git stash apply				// 把最後一次的 stash拿出來用
	> git stash drop 				// 刪除最後一次的 stash


	> git config user.name 	// check user name
	> git config user.email // check user email


	> 	echo "# Note" >> README.md 	// echo "..." >> file_name    >> create a new file and add text in
		git init
		git add README.md
		git commit -m "first commit"
		git remote add origin git@github.com:jason19970210/Note.git
		git push -u origin master
		// Create a new repository on the command line


  > Readme
  	> #, ##, ... , ###### set Heading  >> The number of # you use will determine the size of the heading.
  	> quote text with a >
  	> quoting code with `...`
  		> quoting few lines of code with ```...```
  	> links by [Showing Name](URL)
  	> make lists by -
  		> put in order wth 1. 2. 3.
  	> make task list with [ ], and check the task with [x]

  > GitHub Pages
  	> static page >> HTML as well (NOT FOR PHP OR ASP)
  	> Do NOT support " .htaccess ", FTP server
  	> Can be upload by ONLY Git
  	> GitHub Pages will be PUBLIC

  	Steps
  	> set project name to " (\username).github.io "
  	> set up an empty REPO
  	> add a HTML file name "index.html"

  		> <!DOCTYPE html>
			<html>
  				<head>
    				<meta charset="utf-8">
    					<title>你好，GitHub</title>
  				</head>

  				<body>
    				<h1>覺得厲害</h1>
  				</body>
			</html>

	> git add index.html
	> git commit -m "add index"
	> 

  . First use termianl to cd where you want to put the file
  . Use 'git clone URL' then it will be downloaded to the direction

  . mkdir file_name
  . cd file_name
  . git init			// Initialize 初始

  Setting for beginning use
  *** git config --global user.name "..."
  *** git config --global user.email email@example.com


  Reference
  	> Git Push：https://gitbook.tw/chapters/github/push-to-github.html
  	> Git 管控：https://gitbook.tw/chapters/using-git/add-to-git.html
  	> Git Ignore：https://www.gitignore.io/


# Jupyter-Notebook
	>

# Swift
	>

# C+
	> 

# C#
	>

# SQL
	> select 	// take data
	> insert	// put data in
	> update	// update data
	> drop		// delete data

## WEB
>>> Html & CSS 排版 / Javascript 邏輯

# HTML
	> <HTML> </HTML>	// 文件宣告
	> <Head> </Head>
	> <BODY> </BODY>
		> backgroung : ;


> Fun Example
	> https://www.codecademy.com/courses/animate-your-name/0/1
		> Include main.js amd index.html

	> Note
		> https://www.facebook.com/noootownnotes/

# Javascript
	> 
	
  Reference
	> http://larry850806.github.io/2016/07/16/JS-tips/

# CSS

# PHP

# Markdown
  Reference
	> http://markdown.tw
		> https://github.com/othree/markdown-syntax-zhtw/blob/master/syntax.md


# Terminal
	> ls
	> cd
	> cd .. // go back the former direction
	> mkdir // create folder
	> touch // 新增檔案
	> ping
	> traceroute
	> sudo spctl --master-disable // allow the Mac to install from anywhere
	> atom . // open atom and cd to the file
