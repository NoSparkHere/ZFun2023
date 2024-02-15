---
enabled: true
name: “静态”文件服务
category: security
url_orig: 
prompt: ZFun{...}
index: 0
flags:
- name: 
  score: 250
  type: expr
  flag: f"ZFun{{p4th_trav3rsa1_is_vuln3rb1e_{sha256(token+'2a9b8b5d4eb33a42')[:10]}}}"
---

有一天 RX 要给 ZeroAurora 传一个文件，于是他随便写了一小段代码开了一个文件服务器，根路径下只放了几个要传输的文件，但殊不知大黑客 ZeroAurora 已经可以访问他电脑上的任意文件了。注：你要寻找 flag.txt ，并查看提交这个文件的内容。

访问方式：`题目地址/?file_path=<路径>`

---

提示：在操作系统中开一个 shell，如何进入上一级目录呢？

---

本题在 [web-docker-manager](https://github.com/NoSparkHere/web-docker-manager) 环境下部署。
