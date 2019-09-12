# NOTE
# Contents
	

+ ### [Jupyter Notebook](#Jupyter_Notebook)
	+ #### [Shortcuts](#Shortcuts)

+ ### [C#](#C#)

+ ### [Machine Learning](#Machine_Learning)
	+ #### [Install](#Tensorflow_Install)
		+ #### [MacOS](#Tensorflow_Install_MacOS)
		+ #### [Ubuntu](#Tensorflow_Install_Ubuntu)

+ ### [Network & Communication](#Network_&_Communication)
	+ #### [Ethernet](#Ethernet)
	+ #### [Internet](#Internet)
	+ #### [Block Chain](#Block_Chain)

+ ### [Database & SQL](#Database_&_SQL)
	+ #### [Database](#Database)
	+ #### [SQL](#SQL)
		+ #### [AppServ](#Appserv)
			+ #### [Install](#Appserv_Install)
		+ #### [XAMPP](#XAMPP)
			+ #### [Install](#XAMPP_Install)
		+ #### [Create](#SQL_Create)
			+ #### [Create Database](#SQL_Create_Database)
			+ #### [Create Table](#SQL_Create_Table)


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
	+ #### [Subscript & Superscript (上標 & 下標)](#Subscript&Superscript)
	+ #### [Code](#Code)
	+ #### [Table](#Table)
	+ #### [Link](#Link)
	+ #### [Picture](#Picture)
	+ #### [Highlight Text in diff](#diff_highlight)
	+ #### [Folding](#Folding)

+ ### [Terminal](#Terminal)

+ ### [Hacker](#Hacker)
	+ #### [Network Panatration](#Network_Panatration)


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

<a name="Machine_Learning">

# Machine Learning

<a name="Tensorflow_Install" />

## Install Tensorflow

<a name="Tensorflow_Install_MacOS">

### MacOS

#### Use `Virtualenv`
- Recommened
1. Start a Terminal ( shell )
2. install `pip` and Virtualenv
```shell
$ sudo easy_install pip
$ install --upgrade virtualenv
```
3. Create a Virtualenv environment
```
$ virtualenv --system-site-packages targetDirectory # for Python 2.7
$ virtualenv --system-site-packages -p python3 targetDirectory # for Python 3.n
```
Note: where targetDirectory identifies the top of the Virtualenv tree. Our instructions assume that targetDirectory is ~/tensorflow, but you may choose any directory.

4. Activate Virtualenv environment
```
$ cd targetDirectory
$ source ./bin/activate      # If using bash, sh, ksh, or zsh
$ source ./bin/activate.csh  # If using csh or tcsh 
```

The preceding `source` command should change your prompt to the following:
```
(targetDirectory)$ 
```

5. Ensure pip ≥8.1 is installed
```
(targetDirectory)$ easy_install -U pip
```

6. Issue one of the following commands to install TensorFlow and all the packages that TensorFlow requires into the active Virtualenv environment
```
(targetDirectory)$ pip install --upgrade tensorflow      # for Python 2.7  
(targetDirectory)$ pip3 install --upgrade tensorflow     # for Python 3.n
```

7. Optional.  
If Step 6 failed, install TensorFlow in the active Virtualenv environment by issuing a command
```
pip install --upgrade tfBinaryURL   # Python 2.7
 $ pip3 install --upgrade tfBinaryURL  # Python 3.n
```

where tfBinaryURL identifies the URL of the TensorFlow Python package. The appropriate value of tfBinaryURL depends on the operating system and Python version. Find the appropriate value for tfBinaryURL for your system [here](https://www.tensorflow.org/install/install_mac#the_url_of_the_tensorflow_python_package). For example, if you are installing TensorFlow for macOS, Python 2.7, the command to install TensorFlow in the active Virtualenv is as follows
```
$ pip3 install --upgrade \
 https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.6.0-py3-none-any.whl
```

#### Use `native pip`
#### Use `Docker`
#### Use `Conda`

<a name="Tensorflow_Install_Ubuntu" />

### Ubuntu
### Windwos
### From Source

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
SQL , Structured Query Language  
不同 `資料庫管理系統` 在執行資料庫工作時 所使用的語言

<a name="Appserv" />

### AppServ

<a name="Appserv_Install" />

#### Install
> Windows  
`AppServ`官網 點擊 [AppServ v2.5.9 & 2.4.9 with Zend Optimizer AddOns Released !](http://www.appservnetwork.com/modules.php?name=News&file=article&sid=38)

+ When Installing, following the steps of the wizard.  
+ Type "localhost" & your email address, let the Apache HTTP Port as 80 as default  
+ Enter Root Password and confirm again, The `Character Sets and Collations` should be the option `UTF-8 Unicode`
+ Then the install will be finish.

#### Starting Apache
+ Using the broswer and point to `http://localhost/`  
+ If the web shows fail to connect with the localhost,
> Windows >> Program >> AppServ >> Control Server by Service >> `Apache Start`

#### Stop Apache
> Windows >> Program >> AppServ >> Control Server by Service >> `Apache Stop`

<a name="XAMPP" />

### XAMPP

<a name="XAMPP_Install" />

#### Install
> MacOS
[`XAMPP` Website](https://www.apachefriends.org/zh_tw/download.html) choose the OS-Version  
Here I choose `XAMPP 7.2.2 / PHP 7.2.2`  
+ Open the `manager` run the three services
+ If the `Apache Server` cannot be runing, type the command line in `Terminal`
```shell
sudo launchctl unload -w /System/Library/LaunchDaemons/org.apache.httpd.plist
```

> Disable OSX's built-in Apache server

reference from [here](https://superuser.com/questions/908111/xampp-wont-start-apache-on-mac-os-x-10-10-3-yosemite)

+ Now we need to change the default password  
1. Go to http://localhost/dashboard/ in Safari
2. Choose `HOW-TO Guides` then select `Reset the MySQL/MariaDB Root Password`, it will show you how to change the password.
3. Or you can open a terminal
```shell
$ /Applications/XAMPP/bin/mysqladmin --user=root password "NEW_PASSWORD"
```

### 語法
- SELECT "欄位" FROM "表格名";
- SELECT DISTINCT "欄位"  
	FROM "表格名";
- 


##### Error
```
New XAMPP security concept:

Access to the requested directory is only available from the local network.

This setting can be configured in the file "httpd-xampp.conf".
```


##### Under Mac
1. sudo gedit /opt/lampp/etc/extra/httpd-xampp.conf
2. As below: Search "phpmyadmin"
```
<Directory "/opt/lampp/phpmyadmin">
    AllowOverride AuthConfig
    Allow from all
    Require all granted
</Directory>
```

##### Under Windows
1. Search "httpd-xampp.conf", it should be under C://xampp/
2. Find "phpmyadmin"
3. As below: 
```
<Directory "/opt/lampp/phpmyadmin">
    AllowOverride AuthConfig
    Allow from all
    Require all granted
</Directory>
```

<a name="Start_phpMyAdmin">

### Start phpMyAdmin
+ Ativate Apache and go to http://localhost/phpmyadmin/
> User: `root`  
> Password: `0800080128`

#### Create Database in phpMyAdmin
+ Type the name of the database, select the second colume to `utf-8_unicode_ci`
+ You will see there is some SQL Command
```SQL
CREATE DATABASE `(Your_database_name)`DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
```
+ Then we need to create a table in this database
+ Type the name of the table, and type how many columes we need in this table

<a name="SQL_Create" />

## Create

<a name="SQL_Create_Database">

### Create Database
```sql
CREATE DATABASE `Database_Name` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
```

註：`COLLATE` 語系校正

<a name="SQL_Create_Table">

### Create Table
```sql
CREATE TABLE Table_Name (
	1st_Column 1st_Column_Data_Type
	2nd_Column 1st_Column_Data_Type
)
```

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

<a name="Subscript&Superscript" />

## Subscript & Superscript (上標 & 下標)

- 上標 Superscript : `<sup> </sup>`
```
a<sup>2</sup>
```
a<sup>2</sup>
- 下標 Subscript : `<sub> </sub>`

<a name="Code" />

## Code

<a name="Table" />

## Table

aaa | bbb | ccc
--- | --- | ---
123 | 121 | 122

```markdown
aaa | bbb | ccc
--- | --- | ---
123 | 121 | 122
```


<a name="Link" />

## Link

<a name ="link_with_title">

- With Title

<a name = "link_without_title">

- Without Title


<a name="Picture">

## Picture

### Steps
1. New a Repo and it will be like a server to save photos
2. Just use `git clone http` ... `git push` to upload the photos
3. Go to Repo and click download in the photo
4. Copy the path
5. The format will be like this
	```markdown
	![1](https://raw.githubusercontent.com/jason19970210/MarkdownPhotos/master/1.png)
	```

<a name = "diff_highlight">

## Highlight Text in diff
```
\```diff
+ this will be highlighted in green
- this will be highlighted in red
\```
```
Then it will goes like

```diff
+ this will be highlighted in green
- this will be highlighted in red
```

<a name = "Folding">

## Folding


```
#### 问答

<details>
  <summary>什么是iuap design</summary>
  iuap design 是用友网络FED团队开发的企业级应用前端集成解决方案。
</details>

<details>
  <summary>什么是tinper</summary>

`tinper`是开源前端技术平台。
</details>

```
## 預覽效果


#### 问答
<details>
  <summary>什么是iuap design</summary>
  iuap design 是用友网络FED团队开发的企业级应用前端集成解决方案。
</details>

<details>
  <summary>什么是tinper</summary>

`tinper`是开源前端技术平台。
</details>




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
+ sudo su -
	> set authority to `root`
+ pwpolicy -clearaccountpolicies
	> decline all password security checking for global  
	> for me to set short password as well  
	> after enter this command, type the password then go to `Setting` to change the password for our own

+ apachectl start
	> Start Apache
+ sudo purge
	> Cleaning the memory of MacOS
+ scp -r username@ipaddress:path/on/remote/server path/to/localhost
	> copy the folder with `-r` option to the localhost, without `-r` can only transfer the file
+ scp -r localhost/path/folder username@ipaddress:path
	> copy the folder from local to remote server


<<<<<<< HEAD


# Raspberry Pi (Linux)
+ Change Update Mirror
	- $ sudo nano /etc/apt/sources.list
	- lines like this
		```
		deb http://xxxxxxx.com/raspbain/raspbian buster main contrib non-free rpi
		# Uncomment ....
		```
	- change http website from list of mirrors around the world  
	( https://www.raspbian.org/RaspbianMirrors )
+ Check OS Version & info
	- $ cat /etc/os-release
+ Install Go Lang & Check install version
	- ref : https://www.admfactory.com/how-to-install-golang-on-raspberry-pi/
	- $ sudo apt-get install golang
	- $ go version
=======
+ Linux Error : sudo: unable to resolve host xxx
	> $ sudo vim /etc/hosts  
	> #change origin hostname to current hostname
>>>>>>> 2544fff5d6c05ff5fa27fa3c5f1293123633cf2f
