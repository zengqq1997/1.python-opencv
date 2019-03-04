# win10 python+opencv 环境配置

## python安装

安装python，这里安装的是python3.6.7的版本，可以在Python的官网 www.python.org 中找到最新版本的Python安装包，点击进行下载，请注意，当你的电脑是32位的机器，请选择32位的安装包，如果是64位的，请选择64位的安装包。

在使用安装包安装过程，将pip的工具包勾选上

## opencv 安装

当下载好并安装好python之后，以管理员身份运行cmd或者powershell。一次输入以下命令：

> ```
> pip install --upgrade setuptools
> pip install numpy Matplotlib
> pip install opencv-python
> ```

opencv环境已经配置完成，就是这么简单。只需要numpy、Matplotlib、opencv-python三个包，都不大很快就可以下好，如果下载中间出现error或wrong，重新输入命令即可。

## 测试

### 测试代码

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

### 测试结果

![avatar](https://github.com/zengqq1997/python-opencv-/blob/master/测试结果.jpg)

