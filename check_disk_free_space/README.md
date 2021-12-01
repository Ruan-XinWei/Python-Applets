# 程序文件说明：
1. config配置文件，以[start]和[end]结尾，并且都是独占一行，每一行都是...=...的形式，等号左边为属性名，等号右边为属性值
2. diskinfo.cmd是批处理文件，用于定时执行<span>diskinfo.py</span>
3. diskinfo.py是python文件，用于输出此时的磁盘空闲信息
4. diskinfo.txt的内容是磁盘空闲信息，格式为一行时间，接下来的是每个盘符的空间
5. README.txt说明文件
6. Windows设置定时任务：控制面板\系统和安全\管理工具\任务计划程序 -> 创建基本任务

# 基本条件：
1. python
2. Windows