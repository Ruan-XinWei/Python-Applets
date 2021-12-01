# Python-Applets
Python实现的一些实用小程序

## 本仓库说明

该仓库用来存放主要用Python实现的实用小程序，简化日常繁琐的工作，也能够作为Python的练手小项目。  
为了能够更好地适配各个小程序，建议使用[Anaconda](https://www.anaconda.com/)，避免过多耗时在安装包上。  
对于不想要直接`git clone`整个项目的小伙伴，推荐使用[Git Zip](https://gitzip.org/)。  
本人目前对于Python并不是很熟练，也想借助这个想法，锻炼自己的Python水平。仓库中的Python代码可能并不是很好的解决方法，后期也会慢慢进行完善。  
如果你也是刚接触Python，或者是Python不是很熟练的同学，欢迎一起讨论，一起进步。  
如果在使用过程中发现任何问题，或者有更好的意见，欢迎提出[Issue](https://github.com/Ruan-XinWei/Python-Applets/issues)。

## 小程序介绍

### 前言

对于每一个小程序，尽量结构一致：  

1. config：配置文件
2. <span>xxx.cmd</span>：批处理文件
3. <span>xxx.py</span>：主要Python文件
4. <span>README.md</span>：程序说明，包括使用方法

### Windows磁盘剩余空间定时记录（[check_disk_free_space](https://github.com/Ruan-XinWei/Python-Applets/tree/main/check_disk_free_space)）

主要解决问题：在使用Windows的过程中，如果没有定期主动查看磁盘剩余空间，很容易出现”突然”的爆红，出现原因包括并不限于更新Windows、无意间下载了大体积文件……  
简化之处：定期自动记录磁盘剩余空间，记录下了时间、各磁盘剩余空间以及磁盘每个时间段变化的空间，以便能够在后期查看的时候，初步定位出现问题的时间。