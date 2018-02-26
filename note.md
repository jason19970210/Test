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
	> git stash apply				// 把最後一次的 stash 拿出來用
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
    				<h1>  ...  </h1>
  				</body>
			</html>

	> git add index.html
	> git commit -m "add index"
	> 

  . First use termianl to "cd" where you want to put the file
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
	> ShortCuts
		> Shift - Enter			// run selected cell and turn to next cell as the code mode
		>  Ctrl - Enter			// run selected cell 
		> Double press "D"		// delete selected cell
		> shift - M 			// Merge selected cells


# Python3 >> using "UTF-8", unicode strings
	> 註解 :	單行註解 : #
			多行註解 : '''	 	  	"""
					  text 	  or
					  '''			"""
	> 多行語句 : total = a + \
						b + \
						c

				total = ['a','b',
						 'c']
	
	> 標準數據類型 : Number, String, List, Tuple(元組), Sets(集合), Dictionary(字典)

		檢視Type use	 >> print(type(x))	>> type class
					 >> isinstance		>> bool(True/False)
				ex. a = 111
					print(type(a))			<class 'int'>
					isinstance(a, int)		True

		> Number : int, float, bool, complex(複數)

			>> 類型轉換
				> int(x)			// 
				> float(x)			// 
				> complex(x)		// 
				> complex(x, y)		// 將 x 和 y 轉換到一個複數，時數部分為 x, 虛數部分為 y,  x 和 y 是數字表達式

			>> functions for Number
				> Math
					> abs(x)	取絕對值				
					> fabs(x) 	取絕對值 (float)		math.fabs(-10) = 10.0
					> ceil(x)	(無條件進位)			math.ceil(4.1) = 5
					> floor(x)	取高斯 (無條件捨去)	math.floor(4.9) = 5
					> log(x)	取對數值				math.log(math.e) = 1, math.log(100,10) = 2.0   (e, pi(π) are available in python)
					> log10(x)  得以10為底的對數值		
					> sqrt(x)	得平方根
				> Random
					> choice(seq)						从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
					> random()							随机生成下一个实数，它在[0,1)范围内。
					> shuffle(lst)						将序列的所有元素随机排序
					> uniform(x, y)						随机生成下一个实数，它在[x,y]范围内。
					> random.randint(x,y)				随机生一个整数int类型，可以指定这个整数的范围
					> random.sample(sequence,length)	可以从指定的序列中，随机的截取指定长度的片断，不修改原序列
							ex.
							>>> lst = random.sample('abcd1234',4)
							>>> strs = ''.join(lst)
							>>> strs
							'a432'
							
				> Trigonometric function(三角函數)

		> String : 	word = '字符串'
					sentence = "这是一个句子。"
					paragraph = """这是一个段落，
								可以由多行组成"""

			>> 字符串格式化
				ex.
				print ("我叫 %s 今年 %d 岁!" % ('小明', 10))				我叫 小明 今年 10 岁!

				> %s
				> %d
				> ...
			>> functions for String
				> capitalize()	将字符串的第一个字符转换为大写
				> isalnum()		如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
				> isalpha()		如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
				> isdigit()		如果字符串只包含数字则返回 True 否则返回 False
				> islower()		如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
				> isnumeric()	如果字符串中只包含数字字符，则返回 True，否则返回 False
				> isspace()		如果字符串中只包含空白，则返回 True，否则返回 False.
				> len(string)	返回字符串长度
				> lower()		转换字符串中所有大写字符为小写
				> lstrip()		截掉字符串左边的空格或指定字符

		> List : 	>>>a = [1, 2, 3, 4, 5, 6]
					>>> a[0] = 9
					>>> a[2:5] = [13, 14, 15]
					>>> a
					[9, 2, 13, 14, 15, 6]
					>>> a[2:5] = []   # 将对应的元素值设置为 [] 
					>>> a
					[9, 2, 6]

				>> append(), pop()

		> Tuple

		> Set : 無序, 不重複元素的序列
			創建空集合：only use  set()    DO NOT use { } <- this is use for creating dictionary

					ex.
					student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
					print(student)   # 输出集合，重复的元素被自动去掉					return {'Mary', 'Jim', 'Rose', 'Jack', 'Tom'}
					 
					# 成员测试
					if('Rose' in student) :
					    print('Rose 在集合中')
					else :
					    print('Rose 不在集合中')										return Rose 在集合中
					 
					 
					# set可以进行集合运算
					a = set('abracadabra')
					b = set('alacazam')
					 
					print(a)														return {'b', 'a', 'c', 'r', 'd'}
					print(a - b)     # a和b的差集 									return {'b', 'd', 'r'}
					print(a | b)     # a和b的并集										return {'l', 'r', 'a', 'c', 'z', 'm', 'b', 'd'}
					print(a & b)     # a和b的交集										return {'a', 'c'}
					print(a ^ b)     # a和b中不同时存在的元素							return {'l', 'r', 'z', 'm', 'b', 'd'}

		> Dictionary : 映射類型	>> key:value

					ex.
					dict = {}
					dict['one'] = "1"
					dict[2]     = "two"
					 
					tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
					 
					 
					print (dict['one'])       # 输出键为 'one' 的值			return 1
					print (dict[2])           # 输出键为 2 的值				return two
					print (tinydict)          # 输出完整的字典				return {'name': 'runoob', 'site': 'www.runoob.com', 'code': 1}
					print (tinydict.keys())   # 输出所有键					return dict_keys(['name', 'site', 'code'])
					print (tinydict.values()) # 输出所有值					return dict_values(['runoob', 'www.runoob.com', 1])
	

	> Print : 
				# 換行輸出
				print(x)
				print(y)

				# 不換行輸出
				print(x, end = "")
				print(y, end = "")

					>> String Print 字串擷取
						str = 'Runoob'

						print (str)          # 输出字符串
						print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
						print (str[0])       # 输出字符串第一个字符
						print (str[2:5])     # 输出从第三个开始到第五个的字符
						print (str[2:])      # 输出从第三个开始的后的所有字符
						print (str * 2)      # 输出字符串两次
						print (str + "TEST") # 连接字符串

	> 運算子
		> 算數邏輯
			> + - * /
			> % 取餘數, // 取商數
			> a ** b   a的b次方
		> 比較邏輯
			> == != > < >= <=
		
		> 賦值邏輯
			> c = a + b 			將a + b 的運算结果赋值為 c
			> c += a 				c = c + a
			> c -= a 				c = c - a
			> c *= a 				c = c * a
			> c /= a 				c = c / a
			> c %= a 				c = c % a
			> c //= a 				c = c // a
			> c **= a 				c = c ** a

		> 二進位邏輯
			ex.
			a = 0011 1100
			b = 0000 1101
			- - -
			> & (And Gate) 			a & b = 0000 1100		//
			> | (Or Gate)			a | b = 0011 1101		//
			> ^ (NOR Gate)			a ^ b = 0011 0001		//兩對應的二進位相異時，結果為1
			> ~ 					  ~a  = 1100 0011		//
			> >>n 					a >> 2	= 1111 0000		// 將二進位右移 n 位
			> <<n 					a << 2	= 0000 1111		// 將二進位左移 n 位
		
		> 邏輯
			> and
			> or
			> not

		> 成員
			> in
			> not in


	> Import
				> import module								// import whole module
				> from module import function 				// import function from module
				> from module import 1st_function, 	2nd...	// import few functions from module
				> from module import *						// import all functions from module
	


	> func : BeautifulSoap >> 解析HTML
	> 正則表達式 : Regular Expression : 
	> Use 	request
			pandas
			sklearn
			jieba
			wordcloud

	> Source Base : Numpy, Pandas, SciPy, Matplotlib, Seaborn, ggplot
		Scikit : Preprocessing, Dimentionality reduction, Model selection, Mining/Learning, Experiment

	> for 迴圈
	> 

# Swift
	> make webView support URL with "http"    	>>  right click on info.plist
													> open as -> Source Code
													copy & paste
													"<key>NSAppTransportSecurity</key>
													 <dict>
    												 	<key>NSAllowsArbitraryLoads</key>
    													<true/>
													 </dict>"

												>>  select info.plist on the right under project folder
													right click choose "Add Row"
													selcet "App Transport Security Settings"
													click on the arrow to make it down as a Dictionary
													press the + and choose "Allow Arbitary Loads"
													the default value is boolean: NO , turn it to "YES"

	> Web View (deprecated) 	>> work with iOS 9 and above
									>> use the standard import which is UIKit

	> WebKit View 				>> support iOS 11 and newer
									>> must import WebKit in ViewController

# C+
	> 

# Arduino
	> int pin;

	> void setup() {				// Do once when launch
		Serial.begin(9600);
	}

	> void loop() {					// Reapeat

	}

# SQL
	> select 	// take data
	> insert	// put data in
	> update	// update data
	> drop		// delete data

# Internet
	> Ethernet
	> Wifi
	> Mobile Network
		> 3G
		> LTE
		> 4G
		> LAA: http://www.ttc.org.tw/userfiles/file/20151104/20151104090423_39805.pdf
		> LTE-U

# Machine Learning
	> http://www.r2d3.us/圖解機器學習第一章/

# C#
	> 

## WEB
>>> Html & CSS 排版 / Javascript 邏輯
	> https://developer.mozilla.org/zh-TW/docs/Learn/Getting_started_with_the_web/Installing_basic_software
# HTTP

# HTML
	-> Structure : DOM (Document Object Model)
		> Tags	
			> <h1> - <h6>		標題
			> <p>				段落
			> <a>				超連結				<a herf="https://www.google.com/"> Google Website </a>
			> <table>			表格
				> <tr>			表格內的 row
				> <td>			表格內的 cell
			> <br/>				換行(無結束標籤)

		> Attributes 屬性
			> class				標籤的類別(可重複)
			> id 				標籤的id (不可重複)
			> title 			標籤的顯示資訊
			> style 			標籤樣式
			> data-*			自定義新屬性
		>> 一個標籤可以同時存在多種屬性


> Fun Example
	> https://www.codecademy.com/courses/animate-your-name/0/1
		> Include main.js amd index.html

	> Note
		> https://www.facebook.com/noootownnotes/

# Javascript
	> 
	
  Reference
	> http://larry850806.github.io/2016/07/16/JS-tips/

# CSS  > Cascading Style Sheets (串接樣式表)
			> 用來替 HTML 增加 Style     ex. color, font size, font type ...
	> 

# PHP  > PHP: Hypetext Preprocessor (PHP: 超文字預處理器) (Personal Home Page)
		> 註解：/* */, //, #
		> 資料型態 -- 變數：整數(integer), 浮點數(float), 布林值(boolean), 字串(string)
				  |- 複合類型：陣列(Array), 物件(object)
				  |- 特殊類型：NULL, 資源(resource)

	>	<?php
           	.....
		?>				// PHP 剖析引擎只針對 <?php ?> 其他內容則會被送出

	>	<?php
			-PHP-
		?>

		HTML

		<?php
			-php-
		?>				// 將 PHP 嵌入 HTML 中

# JSON

# Markdown
  Reference
	> http://markdown.tw
		> https://github.com/othree/markdown-syntax-zhtw/blob/master/syntax.md


# Terminal
	> ls
	> cd
	> cd .. 							// go back the former direction
	> mkdir 							// create folder
	> touch 							// 新增檔案
	> ping
	> traceroute
	> sudo spctl --master-disable 		// allow the Mac to install from anywhere
	> atom . 							// open atom, then open the files in the folder
	> nslookup google.com 				// check the DNS server
	> nslookup - xx.xx.xx.xx 			// use xx.xx.xx.xx as the DNS server
	> pip3 install matplotlib 			// use pip3 command to install matplotlib
	
# Hacker