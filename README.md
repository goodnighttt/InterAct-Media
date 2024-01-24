![Untitled](https://github.com/goodnighttt/InterAct-Media/assets/85438203/1ef012a3-5430-4dd9-b89f-dd4d05690c3b)



## 📊主题**：图临成新变，传物揭迷因**

       使用工具：python，D3.js，PS

### **小组成员：**

👍🏻**邢文彦**
💫**陈嘉欣**
👺**张景润**

## 一、交互展示：

[[[最终版演示.mp4](%E6%9C%80%E7%BB%88%E7%89%88%E6%BC%94%E7%A4%BA.mp4)](https://github.com/goodnighttt/InterAct-Media/issues/1#issue-2098598930)](https://private-user-images.githubusercontent.com/85438203/299378153-3122fa35-ea41-44e3-900f-2a8c6b4e5e66.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDYxMTI4NTEsIm5iZiI6MTcwNjExMjU1MSwicGF0aCI6Ii84NTQzODIwMy8yOTkzNzgxNTMtMzEyMmZhMzUtZWE0MS00NGUzLTkwMGYtMmE4YzZiNGU1ZTY2Lm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAxMjQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMTI0VDE2MDkxMVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWYxYzIxNTIzZjFhZmU4NzI4YjViYjA3Yjg5OTA1ZDJlNDAwMTk3YjlkN2I2NmNmYTUyOWVlNTIyOTAyMTczMjgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.dopT2qRA6B-1uXPWEyaJp8y58sjHDOpp53TSjifa5oA)

## 二、主题阐释


###💡 图临成新变，传物揭迷因
图临，即一种对图形进行临摹的操作。在临摹的过程中，由于人力所不可操控的原因而导致发生的各种突变，会留下变异的基因。当这种基因（或者说微小误差的积累）被选择后，就会产生全新的字体与样式。这样，即使在刻意的模仿过程中，依然产生了新的变化。
传物，对于物品的传递，在本次实验中可以有多种解释。既可以指遗传物质、被临摹物的传递，也可以指信号或信息在主体之间的传播。通过对于传递过程中发生的种种差异与变化的研究，我们揭露了“临摹-创新”的一层潜在关系。


## 三、简介

- A1&A5——“爱”字临摹/点赞
    
    本部分实验主要探究临摹的**相似度与喜爱度的联系**。
    将喜爱度根据实际书写时的卷面排布，将其可视化为**热度图**，并且鼠标悬浮在每个方块上时，会出现弹出框并绘制**雷达图**。
    · 其中弹出框中会显示该方块的具体点赞数以及该块的实际字样。
    · 而雷达图一共会显示五个差异度属性——像素差异、重心差异、梯度差异、粗细差异、总加权差异，这五个属性都是将该块的文字与临摹的原素材文字进行比较后的结果。
    
- A7&A8——图形传递临摹
    
    每一个圆盖对应一个汉字的样本。对每一个汉字，都通过图像处理进行分割`（技术：图像二值化、图像分割）` ，然后，将每一个汉字图像都映射到同样大小的画布中（如1024*1024像素）。
    **寻找一种图像间差异度**的度量方法，如每个像素位置处的像素值差异矩阵，然后输出成数值，将每一代与父代之间的差异通过时间序列进行可视化。
    
- A6&A9——书签创作/挑选
    
    该实验使用了同学两次挑选数据创作/收入囊中时的选择原因数据，目的是**对比从创作者以及欣赏者的两个角度**挑选书签时的感受差异。
    将所有原始数据列举出来作为按钮，点击即可看到两次选择的原因绘制出的词云图，即可进行对比。
    
- A11——简笔抽象画摹写
    
    这一部分是想将**整个传递的过程**在一个窗口呈现出来，主要参考了**morphing**技术，目的是利用中间插值的方法实现每每两张图片之间的过渡，以便更直观地看到每次传递过程中的变化。
    
- A3——章法排序
    
    为了探寻同学们在排序过程中对不同因素的重视程度，统计了不同排序因素的出现次数，制作了饼状图，使得不同因素的占比一目了然；同时制作词云，使得阅读者可以直观地看出不同因素以。
    
