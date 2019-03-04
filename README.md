# win10 python+opencv 环境配置

## 一、opencv介绍

Open Source Computer Vision Library.OpenCV于1999年由Intel建立，如今由Willow Garage提供支持。OpenCV是一个基于BSD许可（开源）发行的跨平台计算机视觉库，可以运行在Linux、Windows、MacOS操作系统上。它轻量级而且高效——由一系列 C 函数和少量C++类构成，同时提供了Python、Ruby、MATLAB等语言的接口，实现了图像处理和计算机视觉方面的很多通用算法。最新版本是3.1 ，2016年1月29日发布。（引自[百度百科openCV](http://baike.baidu.com/link?url=48y7MuXtK9Rxobu15Z-PxxESNlthaIbVQvlC_AsSlNd56jgM2MuLKdlpI6bTqeZtHomJOZmqFqZkJEl5Tqzxea)）

## 二、python安装

安装python，可以在Python的官网 www.python.org 中找到最新版本的Python安装包，点击进行下载，请注意，当你的电脑是32位的机器，请选择32位的安装包，如果是64位的，请选择64位的安装包。这里安装的是python3.6.7的版本，因为可能新版本对于一些库的适配不那么齐全。

注意，在使用安装包安装过程，将pip的工具包勾选上

## 三、opencv 安装

当下载好并安装好python之后，以管理员身份运行cmd或者powershell。输入以下命令：

> ```
> pip install --upgrade setuptools
> pip install numpy Matplotlib
> pip install opencv-python
> ```

opencv环境已经配置完成，在这个工程中我们只需要下载numpy、Matplotlib、opencv-python三个包，都不大很快就可以下好，如果下载中间出现error或wrong，重新输入命令即可。

但是可能存在国内网络问题，网速非常慢，安装过程非常漫长，而且中间安装还有很大可能中断，因此可以用国内源安装方法来安装opencv

> python2版本的基本包安装
> pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python
> python2版本的额外包安装
> pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-contrib-python
> python3版本的基本包安装
> pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python
> python3版本的额外包安装
> pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-contrib-python

输入上面对应python版本的pip 语句就可以快速下载和安装了

## 四、测试

### 1.测试代码

```python
#导入cv模块
import cv2 as cv
#读取图像，支持 bmp、jpg、png、tiff 等常用格式
img = cv.imread("D:\python\test.jpg")
#创建窗口并显示图像
cv.namedWindow("Image")
cv.imshow("Image",img)
cv.waitKey(0)
#释放窗口
cv2.destroyAllWindows() 
```

### 2.测试结果

![avatar](https://github.com/zengqq1997/python-opencv-/blob/master/测试结果.jpg)

