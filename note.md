# NOTE
# Contents

+ ### [GitHub](#GitHub)
	+ #### [Command Lines](#Command_Lines)
	+ #### [GitHub Pages](#GitHub_Pages)

+ ### [Swift](#Swift)
	+ #### [UIWebView](#UIWebView)

+ ### [Python3](#Python3)
	+ #### [註解](#Comment)
	+ #### [資料型態](#Data_Type)
		+ #### [Number](#Number)
		+ #### [String](#String)
		+ #### [List](#List)
		+ #### [Tuple](#Tuple)
		+ #### [Set](#Set)
		+ #### [Dictionary](#Dictionary)

+ ### [Jupyter Notebook](#Jupyter_Notebook)
	+ #### [Shortcuts](#Shortcuts)

+ ### [C#](#C#)

+ ### [Communication](#Communication)
	+ #### [Internet](#Internet)
	+ #### [Block Chain](#Block_Chain)

+ ### [Database & SQL](#Database_&_SQL)
	+ #### [Database](#Database)
	+ #### [SQL](#SQL)

+ ### [Web](#Web)
	+ #### [HTML](#HTML)
	+ #### [HTTP](#HTTP)
	+ #### [CSS](#CSS)
	+ #### [PHP](#PHP)
	+ #### [JS](#JS)
	+ #### [JSON](#JSON)

+ ### [Markdown](#Markdown)
	+ #### [Font](#Font)
	+ #### [Quote](#Quote)
	+ #### [Code](#Code)
	+ #### [Link](#Link)
	+ #### [Picture](#Picture)

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
    > 
    
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

<a name="UIWebView" />

### UIWebView
#### Make UIWebView support `http`

+ Method 1
	- Right Click on `info.plist`
	- Select `Open As` > `Source Code`
	- Copy & Paste

		```Swift
		<key>NSAppTransportSecurity</key>
		<dict>
    		<key>NSAllowsArbitraryLoads</key>
    		<true/>
    	</dict>
		```

+ Method 2
	- Select `info.plist`
	- Right Click & Choose `Add Row`
	- Select `App Transport Sercurity Settings`
	- Click the arrow to make it down as a Dictionary
	- Press `+` & Choose `Allow Arbitary Loads`
	- Set the boolean value from default NO to `YES`
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
+ 標準資料型態：`Number`, `String`, `List`, `Tuple`(元組), `Sets`(集合), `Dictionary`
+ 檢視資料型態
	- print(type(a))
	- isinstance(a,int)

	```
	a = 111
	print(type(a))
	isinstance(a,int)

	Output:
	Line[1]: <class 'int'>
	Line[2]: True
	```
<a name="Number" />

+ Number : `int`, `float`, `bool`, `complex`(複數)
	+ 類別宣告
		- int(x)
		- float(x)
		- complex(x)
		- complex(x,y)
			> 將 x 和 y 轉換到一個複數，實數部分為 x, 虛數部分為 y,  x 和 y 是數字表達式

	+ Functions For Number
		+ Math
			- abs(x)
				> 取絕對值
			- fabs(x)
				> 取絕對值(float)
			- ceil(x)
				> 無條件進位
			- floor(x)
				> 無條件捨去, 高斯
			- log(x)
				> 取對數值
			- log10(x)
				> 取以10為底的對數值
			- sqrt(x)
				> 取平方根
		+ Random
			- choice(seq)
				> 從序列的元素中隨機挑選一個元素

				```python
				random.choice(range(10))
				// 從 0～9 之間挑一個整數
				```
			- random()
				> 隨機生成一個實數, 介在[0,1)
			- shuffle(lst)
				> 將序列的所有元素隨機排序
			- uniform(x,y)
				> 隨機生成一個實數, 介在[x,y]
			- random.randint(x,y)
				> 隨機生成一個int整數, 介在[x,y]
			- random.sample(sequence,length)
				> 可以從指定的序列中，隨機的截取指定長度的片段，不修改原序列
				```
				>>> lst = random.sample('abcd1234',4)
				>>> strs = ''.join(lst)
				>>> strs
				'a432'
				```
		+ Trigonometric function (三角函數)

<a name="String" />

+ String
	+ Word
		```
		word = ' 字符串 '
		```
	+ Sentence
		```
		" This is sentence. "
		```
	+ Paragraph
		```
		"""这是一个段落，
		可以由多行组成"""
		```
	+ 字符串格式化
		```
		print ("我叫 %s 今年 %d 岁!" % ('小明', 10))

		Output:
		我叫 小明 今年 10 岁!
		```
	+ Functions For String
		+ capitalize()
			> 將字符串的第一個字符轉換為大寫
		+ isalnum()
			> 如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
		+ isalpha()
			> 如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
		+ isdigit()
			> 如果字符串只包含数字则返回 True 否则返回 False
		+ islower()
			> 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
		+ isnumeric()
			> 如果字符串中只包含数字字符，则返回 True，否则返回 False
		+ isspace()
			> 如果字符串中只包含空白，则返回 True，否则返回 False
		+ len(string)
			> 返回字符串长度
		+ lower()
			> 转换字符串中所有大写字符为小写
		+ lstrip()
			> 截掉字符串左边的空格或指定字符

<a name="List" />

+ List

<a name="Tuple" />

+ Tuple

<a name="Set" />

+ Set

<a name="Dictionary" />

+ Dictionary

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

<a name="Internet" />

## Internet

<a name="Block_Chain" />

## Block Chain


----
<a name="Database_&_SQL" />

# Database & SQL

<a name="Database" />

## Database

<a name="SQL" />

## SQL


----
<a name="Web" />

# Web

----
<a name="HTTP" />

## - HTTP

<a name="HTML">

<a name="PHP" />

## - PHP

<a name="CSS" />

## - CSS
- Cascading Style Sheets (串接樣式表)  
- 用來替HTML增加`Style` ex. Color, Font Size, Font Type...

<a name="JS" />

## - JS

<a name="JSON" />

## - JSON

----
<a name="Markdown" />

# Markdown

<a name="Font" />

## Font

<a name="Quote" />

## Quote

<a name="Code" />

## Code

<a name="Link" />

## Link

<a name="Picture">

## Picture



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