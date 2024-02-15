---
enabled: true
name: 一键日卫星（ver.PHP）
category: security
url_orig: 
prompt: ZFun{...}
index: 0
flags:
- name: 
  score: 500
  type: expr
  flag: f"ZFun{{W0w_yQu_7nD3r5Tand_P0p_N0w_1a0_Da_1s_8acK_{sha256(token+'80b7fd7c3b9c1ddb')[:10]}}}"
---


在 PHP 中有个叫做反序列化的东西，还有一个叫做 POP 链的东西

现在你已经知道它们是什么了，来试试一键日卫星吧

flag 在当前文件目录下（cat ./flag）

注：你的电脑里必须要有 php 环境，这题需要一定的 php 知识

---

### 提示 #1

[php反序列化之pop链](https://blog.csdn.net/weixin_45785288/article/details/109877324) | [PHP魔术方法](https://www.php.net/manual/zh/language.oop5.magic.php)

愿意仔细看第一篇文章的话，一定可以做出来的

### 提示 #2

- __destruct 是反序列化的入口
- echo 可以触发 __toString
- 给一个不存在的属性或对象赋值会触发 __set
- unset 这个函数（注意前面没有__），如果传入的参数是不存在的，则会触发 __unset
- 当尝试以调用函数的方式调用一个对象时，__invoke 会被调用
- system 命令可以执行 cat ./flag
- POP链：Z→u→F→n→HACKER

---

本题使用了 [ctf-docker-template/web-nginx-php73](https://github.com/CTF-Archives/ctf-docker-template/tree/main/web-nginx-php73) 的模板，并针对 [web-docker-manager](https://github.com/NoSparkHere/web-docker-manager) 进行了修改。
