# NOTE
# Contents

- [x] This is a complete item

+ ### [GitHub](#GitHub)
	+ #### [Command Lines](#Command_Lines)
	+ #### [GitHub Pages](#GitHub_Pages)

+ ### [Swift](#Swift)

+ ### [Python3](#Python3)
	+ #### [註解](#Comment)
	+ #### [資料型態](#Data_Type)

+ ### [Jupyter Notebook](#Jupyter_Notebook)
	+ #### [Shortcuts](#Shortcuts)

+ ### [C#](#C#)

+ ### [Communication](#Communication)
	+ #### [Block Chain](#Block_Chain)

+ ### [Database & SQL](#Database_&_SQL)

+ ### [Web](#Web)
	+ #### [HTML](#HTML)
	+ #### [CSS](#CSS)
	+ #### [PHP](#PHP)
	+ #### [JS](#JS)
	+ #### [JSON](#JSON)

+ ### [Markdown](#Markdown)
	+ #### [Quote](#Quote)
	+ #### [Code](#Code)
	+ #### [Link](#Link)
		- ##### [URL](#URL)
		- ##### [In-Page](#In-Page)
	+ #### [Highlight](#Highlight)

+ ### [Terminal](#Terminal)

+ ### [Hacker](#Hacker)

<a name="GitHub" />

# GitHub

<a name="Command_Lines" />

### Command Lines
+   git
	> Get help of git command

+   git init
	> 

+   git clone `https`
	> 

+   git \s
	> get status

+   git add `file name`

+   git commit -m "`commit`"  
    git commit -am "`commit`"
    > give description / Comment to the file
  
+   git push  
	> Upload the file in Staging Area
    git push origin master  
    > 
    git push origin `branch name`  
    > 
    git push --set-upstream origin `branch name`  
    > 
    git push -f  
    > Force Push,  also as `$ git push --force`
    git push -u origin master  
    > 

+   git pull  
    pull = git fetch + git merge
    > Update local version from GitHub
    
+   git add .  
    > add all changed file to Staging Area,  also as `$ git add --all`
    
+   git log  
	> Show all the commits overtime
    git log -p -2  
    > 顯示每個更新之間差別的內容, 限制為只輸出最後兩個更新
    git log --stat  
    > 檢視每個更新的簡略統計資訊
    git log --oneline
    
+   git checkout -b `branch name`  
	> create a new branch and switch to it
    git checkout `branch name`
    > Change the branch to the other one

+   git branch  
	> Show the branches
    git branch `branch name`  
    git branch -D `branch name`  
    git branch --delete `branch name`  

+ 	git remote  
	git remote add origin  
    git remote rm origin  
    git remote -v  

+   git stash  
    git stash save  
    git stash apply  
    git stash drop

+   git config user.name  
	> Check user name
    git config user.email
    > Check user email

+   git config --global user.name `user name`  
    git config --global user.email `user email`  

<a name="GitHub_Pages" />

### GitHub Pages
+ static page like HTML as well
+ Dont support `PHP`, `ASP`, ` .htacess`, `FTP Server`
+ Can be UPLOADED by GIT ONLY
+ GitHub Pages will be PUBLIC

    ### Steps  
	+ set project name to `username.github.io`  
    + set up an empty REPO  
    + add a HTML file name `index.html`  

	```html
	<!DOCTYPE html>
		<html>
		   	<head>
				<meta charset="utf-8">
					<title>Hi, GitHub</title>
			</head>
			<body>
				<h1>...</h1>
			</body>
		</html>
	```
	+ git add index.html  
	+ git commit -m "add index"
	+ git push


### Reference
+ Git Push：https://gitbook.tw/chapters/github/push-to-github.html
+ Git 管控：https://gitbook.tw/chapters/using-git/add-to-git.html
+ Git Ignore：https://www.gitignore.io/

----

<a name="Swift" />

# Swift

----
<a name="Python3" />

# Python3

Using `UTF-8`,`Unicode Strings`


<a name="Comment" />

### 註解
+ 單行註解：`# 註解`
+ 多行註解：
	<pre><code>
	```
	註解 
	```
	</code></pre>

<a name="Data_Type" />

### 資料型態

----
<a name="Jupyter_Notebook" />

# Jupyter Notebook

<a name="Shortcuts" />

### Shortcuts

+ Shift - Enter
	> Run selected cell and turn to next cell as the code mode

+ Ctrl - Enter
	> Run selected cell

+ Double press "D"
	> Delete selected cell

+ Shift - M
	> Merge selected cells

----
<a name="C#" />

# C#

----
<a name="Communication" />

# Communication

<a name="Block_Chain" />

### Block Chain


----
<a name="Database_&_SQL" />

# Database & SQL


----
<a name="Web" />

# Web

----
<a name="HTTP" />

## - HTTP

<a name="PHP" />

## - PHP

<a name="CSS" />

## - CSS
- Cascading Style Sheets (串接樣式表)  
-用來替HTML增加`Style` ex. Color, Font Size, Font Type...

<a name="JS" />

## - JS

<a name="JSON" />

## - JSON

----
<a name="Markdown" />

# Markdown

<a name="Quote" />

+ Quote

<a name="Code" />

+ Code

<a name="Link" />

+ Link

	+ URL  
		- With Text  

	+ In-Page

<a name="Highlight" />

+ Highlight

### Reference

----
<a name="Terminal" />

# Terminal

+ ls
	> List all files in this path
+ cd
+ cd ..
+ mkdir
	> Create folder
+ touch
	> Create file
+ ping
+ traceroute
+ sudo spctl --master-disable
	> Allow Mac to install applications from any **Anywhere**
+ nslookup google.com 
+ nslookup - xx.xx.xx.xx
+ pip3 install matplotlib
+ ps -ax

----
<a name="Hacker" />

# Hacker