to_utf-8在使用时 
-f （--file）后加文件名（必须要有）
-k （--kind）后加编码方式（如果已知就写）
如果不是utf-8编码方式的，会新建一个文件并以utf-8来存储该文件，名称为new_源文件名称.txt
比如，如果原文件为test.txt，那么新文件就是new_test.txt