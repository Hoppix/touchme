# 🖥️ touchme 🖥️ 

A simple python util for creating code templates        

Just a simple project for me to play around with setup tools while getting some nifty QoL utility.

## 🔧 Install 🔧

``sh
curl https://raw.githubusercontent.com/Hoppix/touchme/main/install.sh | bash
``

### ❗️ Prerequisites ❗️
* python >= 3.9.10

## 🚀 Usage 🚀
Type: touchme followed by a filename, example - touchme test.sh or via flag touchme -f test.sh      
```sh
touchme test.sh     
touchme test.py
```
Or with file flag:      
```sh
touchme -f test.sh     
touchme -f test.py
```

####
Currently the following languages are supported:        
* *python*
    * [py](resources/python_template.py)
* *shell*
    * [sh](resources/shell_template.sh)


#### 📦 Author 📦 
Discord: Hoppix#6723


#### Todo
* write tests .... for filechooser ;_;
