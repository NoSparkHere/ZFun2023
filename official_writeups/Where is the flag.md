# Where is the flag
### 出题人：墨染琴弦
## 题目描述
这个程序会把 flag 输出到一个文件里……但是，where？
## 文件内容
[见此](https://github.com/NoSparkHere/ZFun2023/blob/main/problems/where_is_the_flag/files/where_is_the_flag.zip)
## 解法
### 解法一
需要一个能够监测程序行为的软件

比如：[Process Monitor](https://learn.microsoft.com/en-us/sysinternals/downloads/procmon#download)、火绒剑（已下线）

然后检测这个exe即可

最后在%TEMP%中找到flag文件
### 解法二
~~有笨比把flag明文放在程序里了，我不说是谁~~

这是个C++程序文件，反编译即可拿到flag
## flag
ZFun{yOn_F1nd_Me_iN_the_TEMP!}