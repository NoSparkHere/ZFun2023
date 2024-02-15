---
enabled: true
name: 盒打击已就绪 2
category: security
url_orig: files/osint.zip
prompt: ZFun{...}
index: 0
flags:
- name: 
  score: 300
  type: text
  flag: "ZFun{G1506_NND_SHHQ}"
---

也许你并不知道，生活中随手拍下的照片也能成为别人追踪你的线索……

不信？来试试吧！

请找出图片中 4 站台上的高铁列车车次号、始发站和终到站（用车站首字母拼音表示）。

Flag 格式：`ZFun{车次号_始发站_终到站}`

例如：G6519（长沙南 → 长沙）对应的 Flag 为 `ZFun{G6519_CSN_CS}`
