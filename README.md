![Untitled](https://github.com/goodnighttt/InterAct-Media/assets/85438203/1ef012a3-5430-4dd9-b89f-dd4d05690c3b)



## 📊主题**：图临成新变，传物揭迷因**

       使用工具：python，D3.js，PS

### **小组成员：**

👍🏻**邢文彦**
💫**陈嘉欣**
👺**张景润**

## 一、交互展示：

[最终版演示.mp4](%E6%9C%80%E7%BB%88%E7%89%88%E6%BC%94%E7%A4%BA.mp4)

## 二、主题阐释

<aside>
💡 **图临成新变，传物揭迷因** 
图临，即一种对图形进行临摹的操作。在临摹的过程中，由于人力所不可操控的原因而导致发生的各种突变，会留下变异的基因。当这种基因（或者说微小误差的积累）被选择后，就会产生全新的字体与样式。这样，即使在刻意的模仿过程中，依然产生了新的变化。
传物，对于物品的传递，在本次实验中可以有多种解释。既可以指遗传物质、被临摹物的传递，也可以指信号或信息在主体之间的传播。通过对于传递过程中发生的种种差异与变化的研究，我们揭露了“临摹-创新”的一层潜在关系。

</aside>

## 四、简介

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
    

## 五、实验过程详情

### A1&A5——“爱”字临摹/点赞

<aside>
💡 本部分实验主要探究临摹的**相似度与喜爱度的联系**。
将喜爱度根据实际书写时的卷面排布，将其可视化为**热度图**，并且鼠标悬浮在每个方块上时，会出现弹出框并绘制**雷达图**。
· 其中弹出框中会显示该方块的具体点赞数以及该块的实际字样。
· 而雷达图一共会显示五个差异度属性——像素差异、重心差异、梯度差异、粗细差异、总加权差异，这五个属性都是将该块的文字与临摹的原素材文字进行比较后的结果。

![Untitled](项目/图临成新变，传物揭迷因/Untitled.png)

</aside>

数据处理

1. **图像分割**
    
    第一步需要将原文件图中的所有文字进行分割，本次我使用到的是PS的切片工具。但是由于我是将其通过切片数进行平均切分的，因此拍照时因为透视产生的形变会对数据处理产生一定的偏差。
    
    ![Untitled](项目/图临成新变，传物揭迷因/Untitled%201.png)
    
    python批量处理
    
    1）在将所有切片后的图片导出后，需要将其所有文件名进行一个整理，将其全部改为“1.jpg、2.jpg…”的形式，这样在后续的获取图片数据的阶段就可以直接利用其名字的序号作为索引进行绑定。
    
    - 更多代码
        
        ```jsx
        for file_name in file_names:
            # 去掉前缀"S0_"
            if file_name.startswith("1_"):
                new_file_name = file_name.replace("1_", "", 1)
            else:
                new_file_name = file_name
        ```
        
    
    ![Untitled](项目/图临成新变，传物揭迷因/Untitled%202.png)
    
    2）但是由于给出的喜爱数据与实际写的时候的方向是相反的，所以要先将数据转置，但是不能直接转置，因为转置结果的方向与我想要的方向是相反的。
    
    ```jsx
    # 顺时针旋转90度
    rotated_data = list(zip(*data[::-1]))
    ```
    
2. **图像处理`【详情可看A7&A8部分】`**
    
    首先对图像进行二值化处理，获得明显的字符。
    
    ![Untitled](项目/图临成新变，传物揭迷因/Untitled%203.png)
    
    二值化之后，对图像的边缘进行切割，并统一加黑边，得到统一的图像。
    
    ![Untitled](项目/图临成新变，传物揭迷因/Untitled%204.png)
    
    1）准确度
    
    准确度的计算是通过临摹图与样本图每个位置像素之差的绝对值之和：
    
    ```python
    img1_float = img_as_float(img1)
    img2_float = img_as_float(img2)
    pixel_diff = np.sum(np.abs(img1_float - img2_float))
    ```
    
    2）方正度
    
    方正度由重心来衡量，我们认为，一个字越方正，重心越会接近于画布中间的位置，而一个字越飘逸，重心则会偏离中心。
    
    图像的重心由物理公式来决定，即：
    
    ![Untitled](项目/图临成新变，传物揭迷因/Untitled%205.png)
    
    ![Untitled](Untitled%206.png)
    
    ```python
    # 计算图像的重心
    def calculate_centroid(img):
        y, x = np.where(img > 0)
        return np.mean(x), np.mean(y)
    ```
    
    3）粗细
    
    粗细由一个图像中白色像素点占图像总像素的比例决定：
    
    ```python
    # 计算字体粗细
    def calculate_thickness(img):
        white_pixels = np.sum(img > 0)
        total_pixels = img.size
        return white_pixels / total_pixels
    ```
    
    4）梯度
    
    在这里，梯度选用了Sobel算子进行计算：
    
    ```python
    # 计算图像的梯度方向
    def calculate_gradient_direction(img):
        sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
        sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
        gradient_direction = np.arctan2(sobely, sobelx)
        return gradient_direction
    ```
    

可视化

1. 热度图绘制
    
    这一步是将喜爱度作为数据，其范围映射成颜色的深浅。
    
    ```jsx
    // 创建颜色比例尺
              var colorScale = d3.scaleLinear()
                .domain([d3.min(data, function(d) { return d3.min(d); }), d3.max(data, function(d) { return d3.max(d); })])
                .range(["#fbe5eb", "#f0255e"]);
    ```
    
2. 方块绑定数据
    
    这里是要将每个方格的相关数据都绑定到每个方块上，首先是图片以及喜爱度。图片就像是上面在数据处理时说的一样，通过其名字作为索引绑定。
    
    ```jsx
    // 获取所有的图片路径
    		var imagePaths = [];
    		for (var i = 1; i <= 160; i++) {
    		  imagePaths.push("image/images/" + i + ".jpg");
    		}
    ```
    
    - 更多代码
        
        ```jsx
        // 创建矩形
              var rects = heatMap.selectAll("rect")
                .data(function(d, i) { 
                  return d.map(function(value, j) { 
                    var cellIndex = i * data[0].length + j; // 按行展开的一维索引
                    return {
                      value: value,
                      rowIndex: i,
                      columnIndex: j,
                      cellIndex: cellIndex
                    };
                  });
                })
        ```
        
    
    ![Untitled](Untitled%207.png)
    
3. 弹出框
    
    这里要做的主要是针对鼠标悬浮事件，在里面加入弹出框的设置，将每个方块绑定好的数据显示出来。
    
    鼠标悬浮时出现弹出框，鼠标移出时要及时将这个div销毁，当然，也可以使用修改透明度的方式。
    
    - 更多代码
        
        ```jsx
        .on("mouseover", function(d) {
                  var rectX = +d3.select(this).attr("x");
                  var rectY = +d3.select(this).attr("y");
                  var likes = d.value;
                  var index = d.cellIndex;
                  var rowIndex = d.rowIndex;
                  var columnIndex = d.columnIndex;
              
                  var tooltip = d3.select("body")
                    .append("div")
                    .attr("class", "tooltip")
                    .style("left", (rectX + rectWidth + rectPadding) + "px")
                    .style("top", rectY + rectHeight + rectPadding + "px");
              
                  tooltip.append("p")
                    .text("Likes: " + likes);
              
                  tooltip.append("p")
                    .text("Index: " + index);
        
        		  // 显示图片
        			var imagePath = imagePaths[index]; // 获取对应索引的图片路径
        			tooltip.append("img")
        			  .attr("src", imagePath)
        			  .style("max-width", "100px")
        			  .style("max-height", "100px");
                })
                .on("mouseout", function() {
                  d3.select(".tooltip").remove();
                });
        ```
        
    
    ![Untitled](Untitled%208.png)
    
4. 雷达图
    
    1）基本雷达图
    
    首先我先做出了基础的雷达图的绘制代码，然后将其包装成一个函数放入鼠标悬浮事件上调用。
    
    而基础的雷达图的绘制我主要分为3个步骤，绘制正五边形参考背景、绘制数据的五边形、绘制标签。
    
    - 更多代码
        
        ```jsx
        function drawRadar(radarData){
        				  var svglast = d3.select("#last")
        				  svglast.remove();
        				  
        				  
        				  // 设置雷达图参数
        				  var width = 300;
        				  var height = 300;
        				  var radius = Math.min(width, height) / 3;
        				  var angle = (Math.PI * 2) / radarData.length;
        				  
        				  
        				  // 创建SVG容器
        				  var svg = d3.select("#radarChart")
        				      .append("svg")
        					  .attr("id","last")
        				      .attr("width", width)
        				      .attr("height", height);
        				  
        				  // 创建雷达图
        				  var g = svg.append("g")
        				      // .attr("transform", "translate(" + (width / 3) + "," + (height / 3) + ")")
        				  	.attr("transform", "translate(130, 150)"); // 添加偏移量来移动雷达图;
        				  
        				  // 创建雷达图的坐标轴
        				  var axis = g.selectAll(".axis")
        				      .data(radarData)
        				      .enter()
        				      .append("g")
        				      .attr("class", "axis");
        				  								 
        				  								 
        				  // 创建雷达图的轴线和标签
        				  axis.append("line")
        				      .attr("x1", 0)
        				      .attr("y1", 0)
        				      .attr("x2", function (d, i) { return radius * Math.cos(angle * i); })
        				      .attr("y2", function (d, i) { return radius * Math.sin(angle * i); });
        				  
        				  axis.append("text")
        				      .attr("x", function (d, i) { 
        				          var angleOffset = Math.PI / 2;  // 角度偏移量，使标签位置与顶点对应
        				          var angle = (Math.PI * 2 / 5) * i - angleOffset;
        				          var x = (radius + 20) * Math.cos(angle)-10;  // 标签离顶点的距离为半径+10
        				          return x;
        				      })
        				      .attr("y", function (d, i) { 
        				          var angleOffset = Math.PI / 2;  // 角度偏移量，使标签位置与顶点对应
        				          var angle = (Math.PI * 2 / 5) * i - angleOffset;
        				          var y = (radius + 10) * Math.sin(angle)+5;  // 标签离顶点的距离为半径+10
        				          return y;
        				      })
        				      .text(function (d) { return d.name; });
        				  								 
        				  
        				  			 
        				  			 // 创建雷达图的数据区域
        				  			 var area = d3.areaRadial()
        				  				 .angle(function (d, i) { return angle * i; })
        				  				 .innerRadius(0)
        				  				 .outerRadius(function (d) { return d.value * radius; });
        				  			 
        				  			 // 添加一个起始数据点到数据数组末尾，以闭合路径
        				  			 radarData.push(radarData[0]);
        				  			 
        				  			 g.append("path")
        				  				 .datum(radarData)
        				  				 .attr("class", "area")
        				  				 .attr("d", area)
        				  					  .attr("fill", "lightpink");
        				  										  
        				  										  
        				   // 创建正五边形背景
        				   var pentagon = g.append("polygon")
        				       .attr("class", "pentagon")
        				       .attr("points", function () {
        				           var points = [];
        				           for (var i = 0; i < 5; i++) {
        				               var angle = (Math.PI * 2 / 5) * i - Math.PI / 2;
        				               var x = radius * Math.cos(angle);
        				               var y = radius * Math.sin(angle);
        				               points.push(x + "," + y);
        				           }
        				           return points.join(" ");
        				       });
        
        				   // 设置正五边形背景样式
        				   pentagon.attr("fill", "none")
        				       .attr("stroke", "lightpink")
        				       .attr("stroke-width", 1);
        			  }
        ```
        
    
    2）方块绑定雷达的差异数据
    首先是将csv中的每一行数据绑到每一个对应的方块中去。
    
    ![Untitled](Untitled%209.png)
    
    ```jsx
    d3.csv("diff.csv").then(function(diffData) {
              // 创建图像编号与数据的映射对象
              var imageNumberMap = {};
              diffData.forEach(function(d) {
                var imageNumber = +d.image_number; // 将图像编号转换为数值
                imageNumberMap[imageNumber] = {
                  pixel_diff: +d.pixel_diff,
                  centroid_diff: +d.centroid_diff,
                  gradient_diff: +d.gradient_diff,
                  thickness_diff: +d.thickness_diff,
                  total_diff: +d.total_diff
                };
              });
    ```
    
    ![Untitled](Untitled%2010.png)
    
    绑定后就用前面提到的函数进行调用，但是会发现，按照原本的代码逻辑，每次悬浮后的雷达图数据不是在原图上修改的，而是重新绘制铺满页面。
    
    因此如果要解决这个问题，我选择了在每次调用绘制函数时，在绘制前先将上一次绘制的雷达图销毁的操作。
    

### A7&A8——图形传递临摹

#### 实验方法说明

<aside>
💡 每一个圆盖对应一个汉字的样本。对每一个汉字，都通过图像处理进行分割`（技术：图像二值化、图像分割）` ，然后，将每一个汉字图像都映射到同样大小的画布中（如1024*1024像素）。
寻找一种图像间差异度的度量方法，如每个像素位置处的像素值差异矩阵，然后输出成数值，将每一代与父代之间的差异通过时间序列进行可视化。
**预测：**

![Untitled](Untitled%2011.png)

**工具**：`Python、D3.js`

</aside>

#### 数据/图像预处理

![三组皆为临摹所得数据](Untitled%2012.png)

三组皆为临摹所得数据

![Untitled](Untitled%2013.png)

![Untitled](Untitled%2014.png)

首先，对**A7_2**组临摹的实验所得的图像数据进行**图像二值化**处理，将背景置为**0**，而字符的形体置为**1**。

```python
binary = np.where(gray < threshold, 255, 0).astype('uint8')
```

![二值化后的对应图像](Untitled%2015.png)

二值化后的对应图像

![Untitled](Untitled%2016.png)

![Untitled](Untitled%2017.png)

在实验中，一个实验者进行了两次临摹，并且有一个透明盖会经过选择操作被下一位实验者作为临摹对象，因此，我们选取更具有代表性的被临摹一组（**也即打了√的一组**）作为可视化对象。

截取图片并保存，图片名称为对应编号：

![分割后的汉字字符](Untitled%2018.png)

分割后的汉字字符

对汉字字符进行字形结构差异度的量化判断，在本次实验中，引入了多种字形结构的差异度判别标准，分别是：

- **形状上下文描述（即轮廓比对）**
    
    *形状上下文特征多用于形状匹配，目标识别。 它采用一种基于形状轮廓的特征描述方法,其在对数极坐标系下利用直方图描述形状特征能够很好地反映轮廓上采样点的分布情况。 形状上下文指的是像素点邻域内的其它像素点的分布情况。*
    
- **骨架提取**
- **重心、梯度和像素值差异加权**

先读取父本图`“0.png”`，通过Opencv提取其主要轮廓，然后循环读取剩下的临摹图，提取轮廓，通过形状上下文描述算子计算轮廓差异度，绘制成曲线图。

![提取的主要轮廓](Untitled%2019.png)

提取的主要轮廓

![Untitled](Untitled%2020.png)

```python
img0 = cv2.imread("0.ong")
img0_contours = cv2.findContours(img0) #提取轮廓
ref_cnt = max(ref_contours, key=cv2.contourArea) #选择最大轮廓	
```

首先，我们先读入父本图片，提取轮廓并选择其最大轮廓，之后每一张图片都按照同样的逻辑进行处理；

在这里，我对数据的处理和输出采用了两种方式，以得到不同可视化形式所需要的数据。第一种是形如下面的**json**数组，该**json**表示的是1-39幅临摹图与父本图0的差异度：

```json
{"image": 1, "difference": x1}, {"image": 2, "difference": x2},……
```

第二种是一个40*40的矩阵，也同样输出为**json**，该文件代表的同样是1-39临摹图与0的差异度。

```python
matrix = [] #在这里初始化差异矩阵
differences = [] #差异度数组
for i in range(1, 40):
    img = cv2.imread(f'{i}_no_borders.png', cv2.IMREAD_GRAYSCALE)
    _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = max(contours, key=cv2.contourArea)

    match = sd.computeDistance(ref_cnt, cnt)
    matrix[0][i] = match
    matrix[i][0] = match
		differences.append({"image": i, "difference": match})

with open('matrix.json', 'w') as f:
    json.dump(matrix, f)
		# json.dump(differences, f)
```

在循环开始前，我声明了差异值列表，用来存储每一幅图与父本图片的差异度。在循环中，提取每一幅临摹图的轮廓，并计算与父本图0之间的差异值。由于最终要使用D3.js作为数据可视化的工具，而D3接收的数据格式为json，因此需要将差异度矩阵转换为json格式。
    

#### 可视化处理

在可视化的过程中，我选用了D3.js作为工具来呈现最终的结果。可视化形式选用了两种，第一种是面积图，第二种是和弦图（环状桑基图）。

面积图实际上就是填充后的平滑折线图，通过面积图的高低起伏和走向，我们能够看出每一代临摹图与父代之间的差异趋势变化；

和弦图能够展现两两之间的数值关系和对比差异，方便我们直接显示数据和对比。

在这里，对D3的代码作简要说明：

- **面积图**

```jsx
d3.json("differences.json").then(function(data) {
        x.domain(d3.extent(data, function(d) { return d.image; }));
        y.domain([0, d3.max(data, function(d) { return d.difference; })]);
				
				var area = d3.area()
        .x(function(d) { return x(d.image); })
        .y1(function(d) { return y(d.difference); })
        .curve(d3.curveCatmullRom.alpha(0.2)); // 添加平滑曲线
}
```

绘制面积图由**d3.area()方法进行绘制**，其中X轴对应图片序号，而Y轴对应该序号图与父代图之间的差异度。

- **和弦图**

```jsx
var ribbons = chordSvg .append("g")
            .attr("class", "ribbons")
            .selectAll("path")
            .data(chordData)
            .enter().append("path")
            .attr("d", ribbon)
            .style("fill", function(d) { return color(d.target.index); })
            .style("stroke", function(d) { return d3.rgb(color(d.target.index)).darker(); })
            .style("opacity", 0.3)
            .on("mouseover", function(d) {
                var current_diff = current_diff_matrix[d.source.index][d.target.index];  // 使用当前的差异矩阵
                tooltip.style("visibility", "visible")
                    .html("差异度: " + current_diff);
                tooltipImg.style("visibility", "visible")
                    .attr("src", "A7/" + (d.target.index + 1) + "__no_borders.png")
                    .style("top", (height/2)+"px")
                    .style("left",(width/4*3-240)+"px");
                tooltipImg1.style("visibility", "visible")
                    .attr("src", "A7/1__no_borders.png")
                    .style("top", (height/2)+"px")
                    .style("left",(width/4*3+50)+"px");
                d3.select(this).style("opacity", 0.95);
            })
            .on("mousemove", function() {
                tooltip.style("top", (d3.event.pageY-10)+"px")
                    .style("left",(d3.event.pageX+10)+"px");
            })
            .on("mouseout", function() {
                tooltipImg.style("visibility", "hidden");
                tooltipImg1.style("visibility", "hidden");
                tooltip.style("visibility", "hidden");
                d3.select(this).style("opacity", 0.5);
            });
```

该段代码主要负责鼠标悬浮显示弦和差异度数值的功能。

#### 优化处理

除了对汉字轮廓进行形状上下文分析外，还有其他的方法可以度量两个汉字之间的形体差异。如对应位置的像素之差，能够看出字形**是否位置匹配**；汉字的像素重心分布，能够看出形体结构的**纵横飘逸**情况；像素的梯度，能够看出字形的**”弯折“**情况。

通过对手动截取的图像进行观察，能够发现由于采集数据时的不规范，有些字体并不一样大，并且放置的角度也不正确，因此需要进行图像处理，来使所有的字符标准化。

![**原本的数据，角度、位置并不统一，如果直接处理，存在较大误差**](Untitled%2021.png)

**原本的数据，角度、位置并不统一，如果直接处理，存在较大误差**

使用Opencv的`Rotate()`方法对图像进行旋转，旋转过程中产生的缺失填充为黑色。

![滑动条实时控制旋转角度](Untitled%2022.png)

滑动条实时控制旋转角度

![矫正角度后得到的数据](Untitled%2023.png)

矫正角度后得到的数据

矫正角度后，我们需要对图片进行黑边切割。原本的图片数据中，字符分布的位置并不统一，如果直接进行差异度比较，存在较大误差。因此，先遍历所有像素，找到有白色像素（即文字所在）的最大区域，切割出来，统一加黑边，并缩放至相同像素，便实现了字符的统一化（位置、角度）。

![去除黑边后统一加边框并缩放到相同像素](Untitled%2024.png)

去除黑边后统一加边框并缩放到相同像素

重新对差异度进行衡量，在这里，除了轮廓的形状上下文差异外，我还采用了梯度、像素值差异作为衡量的标准。像素值差异即两张图片对应位置上像素的差值取绝对值，最后求和，而梯度则为梯度矩阵和值的差。

$$
pixel_-diff = sum(abs(img1 - img2))

$$

$$
gradient_-diff = sum(abs(gradient(img1))) - sum(abs(gradient(img2)))
$$

```python
# 计算图像的梯度方向
def calculate_gradient_direction(img):
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
    gradient_direction = np.arctan2(sobely, sobelx)
    return gradient_direction

# 计算各个差异
def calculate_difference(img1, img2):
    img1_float = img_as_float(img1)
    img2_float = img_as_float(img2)
    pixel_diff = np.sum(np.abs(img1_float - img2_float))

    # 梯度
    gradient_direction_diff = np.sum(np.abs(calculate_gradient_direction(img1))) - np.sum(np.abs(calculate_gradient_direction(img2)))

    return pixel_diff,  gradient_direction_diff

最后一共输出四种差异度：像素差异度、梯度差异度、轮廓差异度以及三者相加形成的加权差异度
```

#### 可视化结果&分析

[Untitled](Untitled.mp4)

面积图呈现了汉字字符差异度与临摹代数的关系。在本幅图中，我们能够发现，在一开始，临摹次数小于**20**时，差异度平稳变化，并在第10代和第15代出现了一定的起伏。这符合我们的认知，即前几次的临摹并不会发生特别大的改变。

到了20代后，在22、23代左右，发生了一次**突变**，这次突变导致差异度迅速上升，出现了峰值。在此之后，差异度整体水平大于前20代水平，表示突变之后差异的***基因***保留了下来。

通过点击不同颜色的按钮，我们可以观察不同差异度决定的面积图，可以看到四条面积曲线所呈现的趋势基本一致，这表明字体的差异度确实是在逐代增加。

[和弦图演示（初代）](Untitled%201.mp4)

和弦图演示（初代）

[添加了选择按钮的和弦图](Untitled%202.mp4)

添加了选择按钮的和弦图

为了更清晰地展现这种规律，我们采用和弦图的形式对差异度数值直接进行量化展现，和弦线条的粗细即代表差异度大小，为了方便感受字体之间的差异，我还将临摹字与父代同时排列显示。

由和弦图，我们能够更清晰地看出，在20代左右发生了突变。由字形的对比，也能感受到字形、轮廓似乎与父代字形有着较大的差异。

在39代，由数据(`梯度差异度`）和对比图能够看出，字符的倾斜与弯曲与初代相比也发生了很大变化，几乎看不出来是一个方正的汉字了。

基于以上的数据可视化结果，我们可以看出一层潜在的隐藏规律：**刻意的模仿也能导致潜在的创新。**

由`生物进化理论`，我们可以得知，生物的遗传实际上是遗传物质的遗传，而遗传物质是直接复制父本母本。每一代复制和模仿实际上都产生了一定的变异，而当变异积累到一定的量级时，就会在表现型上凸显出来。表现型经过自然选择，就可以将这种突变基因保留下来，由此完成生物进化。我们可以将”图临游戏“的临摹视作一种复制，而每一次临摹上一幅图的行为看作遗传。

从信号学/信息学的角度来看，每一次临摹实际上也可以看作上一代向下一代的信息传输。在此处，信源即是上一代被临摹的样本，信道就是人眼由光学路径观察到的情况。上一代样本在临摹结束后，图片的摆放就以及经过了编码过程，而下一位临摹者接收到图片信息后，则会由大脑进行解码。
而由信道限制、噪声等因素影响，信息的传输并不是无损的，这也可以解释为何每一代临摹中不可能存在完全的复制情况。

当然，临摹也能被视作一种“`运算法则`”，但临摹并不是单纯的复制，这其中存在着一定的误差因素，如临摹时手的力度、观察力等等。因此，**经过多代的临摹后，才能带来创新。**

### A6&A9——书签创作/挑选

<aside>
💡 该实验使用了同学两次挑选数据创作/收入囊中时的选择原因数据，目的是对比从**创作者以及欣赏者的两个角度**挑选书签时的感受差异。
将所有原始数据列举出来作为按钮，点击即可看到两次选择的原因绘制出的词云图，即可进行对比。

![Untitled](Untitled%2025.png)

</aside>

数据处理

1. 同类书签分组
    
    1）整理数据
    
    首先从数据文件中整理出同学拍的32个原数据样本。
    
    ![Untitled](Untitled%2026.png)
    
    2）将原文本数据进行分组操作，根据编号，将编号相同的评论分到一组，并将评论通过逗号分隔拼接到一起。
    
    ![Untitled](Untitled%2027.png)
    
    ```jsx
    # 整合相同编号的内容
    result = {}
    for line in lines:
        line = line.strip()
        if line:
            parts = line.split(',')
            if len(parts) == 2:
                code, content = parts
                if code in result:
                    result[code].append(content)
                else:
                    result[code] = [content]
            else:
                print(f"无法解析的数据行: {line}")
    ```
    
2. 词频处理
    
    这里我主要用了jieba库进行分词，但是仅仅使用库进行分词的话，我从结果中看到很多没有用的词，我希望显示的词中**尽量只保留能代表主观想法的词汇**，如形容词。
    
    因此我根据多次测试整理出了一系列停用词，在数据中将其删去。
    
    ![Untitled](Untitled%2028.png)
    

可视化

1. 词云图绘制
    
    主要就是`seg_list = jieba.cut(selected_comments)`以及`ordcloud.generate(seg_str)`的操作，主要是要多以不将上述分组好的数据再根据编号进行一个提取，这样才能获得单个编号的评价。
    
    ```
    #根据选择的编号生成词云图
    selected_code ='EB'#替换为您选择的编号
    selected_comments =''
    forlineinlines:
        code, comments = line.strip().split(':')
    ifcode == selected_code:
            selected_comments = comments.strip()
    break
    ```
    

### A11——简笔抽象画摹写

数据处理

<aside>
💡 这一部分是想将**整个传递的过程**在一个窗口呈现出来，主要参考了morphing技术，目的是利用中间插值的方法实现每每两张图片之间的过渡，以便更直观地看到每次传递后的变化。

</aside>

1. 图像切片
    
    图像切片与上面同理，将图片切割好。
    
    ![Untitled](Untitled%2029.png)
    
2. 中间插值渐变过渡
    
    原本是向利用检测出的轮廓来进行一个根据边缘绘制中间变化可能的插入帧，但是时间有限一直没有做出来，因此最后退而求其次，通过两者直接修改透明度实现过渡。
    
    ```
    #图像间的平滑过渡
    foralphainnp.linspace(0, 1, 10):
    #通过线性插值创建中间图像
    interpolated_image = cv2.addWeighted(base_image, 1 - alpha, current_image, alpha, 0)
    
    #在视频中写入中间图像
    output_video.write(interpolated_image)
    
    #显示中间图像
    cv2.imshow('Morphing', interpolated_image)
        cv2.waitKey(1)
    ```
    
3. **一些有点失败但是很有意思的尝试**
    
    1）手动打点定位
    
    morphing主要分为两个步骤，一为检测对应的控制点，二为通过控制点在中间进行插值。本次采用了手动添加监测点的方式。
    
    2）找出轮廓
    
    后来又有了通过检测到轮廓后，识别检测出哪些是对应的的边缘，然后直接根据撑开或者缩小边缘来实现渐变，会更真实一点，有点像是live2d里的那种操作。
    
    3）找到特征点比对
    
    在找对应的部位时用到的，但是最后呈现的结果发现实在差太多，所以舍掉了。
    
    ![手动添加控制点](Untitled%2030.png)
    
    手动添加控制点
    
    ![边缘检测](Untitled%2031.png)
    
    边缘检测
    
    [通过控制点中间插值](test1.mp4)
    
    通过控制点中间插值
    
    ![特征点检测](Untitled%2032.png)
    
    特征点检测
    
    - 更多代码
        
        ```python
        def select_feature_points(image, num_points):
            """
            手动选择特征点
            """
            points = []
            win_name = 'Select Feature Points'
        
            def mouse_callback(event, x, y, flags, param):
                if event == cv2.EVENT_LBUTTONDOWN:
                    points.append((x, y))
                    cv2.circle(image, (x, y), 3, (0, 0, 255), -1)
                    cv2.imshow(win_name, image)
        
            cv2.namedWindow(win_name)
            cv2.setMouseCallback(win_name, mouse_callback)
        
            while len(points) < num_points:
                cv2.imshow(win_name, image)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    break
        
            cv2.destroyWindow(win_name)
        
            return points
        ```
        
        ```python
        # 应用边缘检测算法
        edges = cv2.Canny(gray, 50, 150)  # 设置阈值参数为50和150
        
        # 轮廓检测
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        ```
        
        ```
        defextract_features(image):
        #使用SIFT算法提取特征点和描述符
        sift = cv2.xfeatures2d.SIFT_create()
            keypoints, descriptors = sift.detectAndCompute(image,None)
        returnkeypoints, descriptors
        
        defmatch_features(descriptors1, descriptors2):
        #使用FLANN匹配器进行特征匹配
        FLANN_INDEX_KDTREE = 0
            index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
            search_params = dict(checks=50)
            flann = cv2.FlannBasedMatcher(index_params, search_params)
            matches = flann.knnMatch(descriptors1, descriptors2, k=2)
        
        ```
        
    

### A3——章法排序

统计了同学们在认为的对排序有影响的因素，并按照每个因素出现次数的多少制作了词云。

![词云.png](%E8%AF%8D%E4%BA%91.png)

排序因素饼状图：

![饼状图.jpg](%E9%A5%BC%E7%8A%B6%E5%9B%BE.jpg)
