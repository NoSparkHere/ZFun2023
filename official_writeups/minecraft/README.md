# Welcome to Minecraft
### 出题人：墨染琴弦
## 题目描述
做题之余，放松一下吧。

不过……生存模式下需要指令吗？

再给你送点提示：1.20.1
## 文件内容
[见此](https://github.com/NoSparkHere/ZFun2023/blob/main/problems/minecraft/files/minecraft.zip)
## 解法
Minecraft，启动！
阅读jar文件中的`mods.toml`可知，这是一个1.20.1的模组

再反编译，发现`minecraftforge`字样，确认这是个forge模组

### 解法一
在1.20.1 forge的MC中安装此mod，然后使用指令`/flag`

不知道指令也没关系，mc的命令系统会显示所有可用的指令，和原版对照一下即可
### 解法二
你都反编译了还进游戏干啥？

在`mod.jar:net/mcreator/zfun/procedures/SendflagProcedure.class`中即可看到flag
## flag
ZFun{he1l0_miNecraFt}
## 题外话
本来是没有版本提示的，不知道谁给我加上了，大大降低了难度

不过本来就没啥难度（