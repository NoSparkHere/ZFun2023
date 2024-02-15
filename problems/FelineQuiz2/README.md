---
enabled: true
name: 菲林问答 Season 2
category: basic
url_orig: 
prompt: ZFun{...}
index: 0
flags:
- name: Flag 1
  score: 50
  type: text
  flag: f"ZFun{{{sha256(token+'cd02e3d2aff3e8db')[:16]}}}"
- name: Flag 2
  score: 100
  type: expr
  flag: f"ZFun{{{sha256(token+'21ba1d1cb7db907c')[:16]}}}"
- name: Flag 3
  score: 50
  type: expr
  flag: f"ZFun{{{sha256(token+'36eb4ce3a2872f03')[:16]}}}"
---

善用搜索引擎很重要哦！
