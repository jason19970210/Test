# NOTE
# Contents

+ ### [GitHub](#GitHub)
	+ #### [Command Lines](#Command_Lines)
	+ #### [GitHub Pages](#GitHub_Pages)

+ ### [Swift](#Swift)
	+ #### [Data Type](#Swift_Data_Type)
	+ #### [UIWebView](#UIWebView)

+ ### [Python3](#Python3)
	+ #### [Comment](#Comment)
	+ #### [Data Type](#Python_Data_Type)
		+ #### [Number](#Number)
			+ ##### [類別宣告](#類別宣告)
			+ ##### [Functions For Number](#Functions_For_Number)
				+ [Math](#Python_Math)
				+ [Random](#Python_Random)
				+ [Trigonometric Function](#Python_Trigonometric_Function)
		+ #### [String](#String)
		+ #### [List](#List)
		+ #### [Tuple](#Tuple)
		+ #### [Set](#Set)
		+ #### [Dictionary](#Dictionary)
			+ ##### [利用 Value 反查 Key](#value_key)
			+ ##### [檢查 Dict 中有無包含特定的 Key](#dict_key)
		+ #### [運算子](#cal)
			+ ##### [算數邏輯](#calculate)
			+ ##### [比較邏輯](#compare)
			+ ##### [賦值邏輯](#give_value)
			+ ##### [二進位邏輯](#binary_logic)
			+ ##### [邏輯閘](#logic_gate)
			+ ##### [成員](#member)
		+ #### [Input](#input)
	+ #### [爬蟲](#)

+ ### [Jupyter Notebook](#Jupyter_Notebook)
	+ #### [Shortcuts](#Shortcuts)

+ ### [C#](#C#)

+ ### [Network & Communication](#Network_&_Communication)
	+ #### [Ethernet](#Ethernet)
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
	+ #### [Table](#Table)
	+ #### [Link](#Link)
	+ #### [Picture](#Picture)

+ ### [Terminal](#Terminal)

+ ### [Hacker](#Hacker)

----
----


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

<a name='Swift_Data_Type' />

### Data Type

<a name="UIWebView" />

### UIWebView
#### Make UIWebView support `http`

+ Method 1
	- Right Click on `info.plist`
	- Select `Open As` > `Source Code`
	- Copy & Paste

		```swift
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

### Comment
+ 單行註解：`# 註解`
+ 多行註解：
	<pre><code>
	```
	註解 
	```
	</code></pre>

<a name="Python_Data_Type" />

### Data Type
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

	<a name='類別宣告' />

	+ 類別宣告
		- int(x)
		- float(x)
		- complex(x)
		- complex(x,y)
			> 將 x 和 y 轉換到一個複數，實數部分為 x, 虛數部分為 y,  x 和 y 是數字表達式

	<a name='Functions_For_Number'>

	+ Functions For Number

		<a name='Python_Math' />

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
			- max(a,b)
				> a, b 的最大值
			- min(a,b)
				> a, b 的最小值

		<a name='Python_Random' />

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

		<a name='Python_Trigonometric_Function' />

		+ Trigonometric Function (三角函數)

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
	無序, 不重複元素的序列  
	+ 創建空集合：set()


<a name="Dictionary" />

+ Dictionary
	+ 映射類型：key:value, 鍵值:變數
	+ dict = {}
		> 建立空的dict
	+ del dict[key]
		> 刪除特定的 key-value pair
	+ dict[key]=value
		> 若key不存在 則增加這組pair  若key已存在 則更新這組pair

	```python
	dict = {}
	dict['one'] = "1"
	dict['2'] = "two"

	tinydict = {'name':'runnob','code':1,'site':'www.runnob.com'}

	print(dict['one'])
	print(dict['2'])
	print(tinydict)
	print(tinydict.keys())
	print(tinydict.values())

	## Output
	1
	two
	{'name': 'runoob', 'site': 'www.runoob.com', 'code': 1}
	dict_keys(['name', 'site', 'code'])
	dict_values(['runoob', 'www.runoob.com', 1])

	- - - -

	table = {}
	
	for inputTimes in range(0,5)
		k = input('輸入字串：')
		v = int(input('輸入整數：'))
		
		table[k] = v
		print(end='\n')
	print(table)
	

	## Output
	輸入字串：eat
	輸入整數：24

	輸入字串：3
	輸入整數：17

	輸入字串：Lynn
	輸入整數：19

	輸入字串：hello_world
	輸入整數：265

	輸入字串：5578
	輸入整數：201

	{'3':17, 'Lynn':19, '5578':201, 'hello_world':265, 'eat':24}
	```
	<a name='value_key' />

	+ 利用 Value 反查 Key
	```python
	d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
	target = 2
	for key in d:
		if d[key] == traget:
			print('key = ', key)
			break
		else:
			print('404 NOT FOUND!')
	
	## Output
	key = two
	```
	<a name='dict_key' />

	+ 檢查 Dict 中有無包含特定的 Key

	```python
	d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
	print('one' in d)
	print(1 in d)

	## Output
	True
	False

	- - - -
	# 若想拿到一個由所有key組成的list、或一個由所有value組成的list，可以使用dict.keys()或是dict.values()。結合反查的方法，可以檢查一個特定的key或value在這個dict中存不存在。

	d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
	print(0 in d.keys())
	print(1 in d.values())
	print('one' in d.keys())
	print(9 in d.values())

	## Output
	False
	True
	True
	False

	- - - -
	# d.get(key, default_value): 是比較安全的作法，如果key不存在的話就會回傳 default_value (下面例子中的deafult_value就是’找不到耶’)。

	d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
	print(d['one'])
	print(d.get('two','NOT FOUND'))
	print(d.get(2,'NOT FOUND'))


	## Output
	1
	2
	NOT FOUND
	```

<a name='cal' />

+ #### 運算子

	<a name='calculate' />

	+ 算數邏輯
		+ \+ - * /
		+ % 取餘數
		+ // 取商數
		+ a ** b  a的b次方

	<a name='compare' />

	+ 比較邏輯
		+ `==` `!=` `>` `<` `>=` `<=`

	
	<a name='=give_value' />

	+ 賦值邏輯
		+ c = a + b
			> 將a + b 的運算结果赋值為 c
		+ c += a
			> c = c + a
		+ c -= a
			> c = c - a
		+ c *= a
			> c = c * a
		+ c /= a
			> c = c / a
		+ c %= a
			> c = c % a
		+ c //= a
			> c = c // a
		+ c **= a
			> c = c ** a

	<a name='binary_logic' />

	+ 二進位邏輯
		+ &
			> And Gate
		+ |
			> Or Gate
		+ ^
			> NOR Gate  
			> 兩對應二進位相異時, 輸出1
		+ ~
			> 補數
		+ \>>n
			> 右移n單位
		+ <<n
			> 左移n單位

		#### Example
		```
		a = 0011 1100
		b = 0000 1101

		a & b = 0000 1100
		a | b = 0011 1101
		a ^ b = 0011 0001
		~a = 1100 0011
		a >>2 = 1111 0000
		a <<2 = 0000 1111
		```

	<a name='logic_gate' />
	
	+ 邏輯閘
		+ And
		+ Or
		+ NOT

	<a name='member' />

	+ 成員
		+ in
		+ not in

<a name='input' />
 
+ ### Input
	+ For `Python3`
		+ Use `raw_input` in `Python2`
		+ There is another function for `input` in `Python2`

		### Example
		```python
		a = input()
		print('a= ',a)

		b = input('Your Name: ')
		print('Your Name: ',b)


		## Output
		289
		a = 289
		Your Name: aaa
		Your Name: aaa

		- - - -

		a = int(input('整數1 = '))
		b = int(input('整數2 = '))
		print(a+b)
		print(a-b)
		print(a*b)
		print(a/b)


		## Output
		整數1 = 10
		整數2 = 101
		111
		-91
		1010
		0.099.....

		```
+ ### If-Else Function
	```python
	if 條件:
		do `1st`
		do 2nd
	else: #else 不接條件
		do 3rd



	if 條件1:
		do 1st
	elif 條件2:
		do 2nd
	else
		do 3rd
	```
+ ### For Loop Function
	```python
	for i in range(0,10):
		print(i)


	## Output
	0
	1
	2
	3
	...
	9
	```
	range(n) = range(0,n)  
	資料只取到`n-1`  
	range 結構: range(起點,終點,間距)

	```python
	for i in range(1,10):
		for j in range(1,10):
			print(i*j,end='')
		print(end='\n')
	
	# end=' '  不希望print出來的結果換行且要有空格
	# end='\n'  若要再換行可使用end='\n'

	## Output
	99 乘法表


	for i in range(1,10,2):
		print(i)

	## Output
	1
	3
	5
	7
	9

	for i in range(10,1,-3):
		print(i)

	## Output
	10
	7
	4
	```
+ ### Import
	+ import `module`
		> import whole module
	+ from `module` import *
		> import all functions from module
	+ from `module` import `function`
		> import the function from module
	+ from `module` import `1st_function`, `2nd_function`...
		> import few functions from module
+ ### Function
	+ ### 自定義函數
		- 以 `def` 開頭 後接函數名稱和 `()`
		- 任何傳入參數和自變量必須置於 `()` 中間 `()`可用於定義參數
		- 函數的第一行可選擇性使用文檔字符 用於存放函數說明
		- 函數內容以 `:` 起始 且需縮排
		- `return[express(表達式)]` 結束函數並選擇性返回一個值給調用方
		- 不帶表達式的return則返回 `NONE`

			Example:
			```python
			def function_name(parameters):
				"函數_文檔字符串"
				function_suite
				return[express]

			- - - -
			def printme(str):
				"print 傳入的字符串到 console上 "
				print(str)
				return
			```
	+ ### 調用函數
		```python
		def printme(str):
				"print 傳入的字符串到 console上 "
				print(str)
				return

		# 調用函數
		printme("調用自定義函數")
		printme("再次調用函數")


		## Output
		調用自定義函數
		再次調用函數



		```

	+ ### BeautifulSoup
		+ 解析 HTML
	+ ### 


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
<a name="Network_&_Communication" />

# Network & Communication

<a name="Ethernet" />

## Ethernet

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

#### 是一種創建動態交互站點的服務器端腳本語言
Example
```html
<!DOCTYPE html>
	<html>
		<body>

			<?php
			echo "Hello World!";
			?>

		</body>
	</html>
```

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

<a name="Table" />

## Table

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