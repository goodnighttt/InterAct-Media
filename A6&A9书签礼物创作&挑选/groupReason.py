import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# 读取评论数据
with open('整合结果2.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 创建词云对象，并指定字体文件路径
font_path = '鸿雷拙书简体.otf'  # 替换为你自己的字体文件路径
wordcloud = WordCloud(width=800, height=400, background_color='white', font_path=font_path)

# 根据选择的编号生成词云图
selected_code = 'EB'  # 替换为您选择的编号
selected_comments = ''
for line in lines:
    code, comments = line.strip().split(':')
    if code == selected_code:
        selected_comments = comments.strip()
        break

# 使用jieba进行分词
seg_list = jieba.cut(selected_comments)

# 要删除的词语列表
stop_words = ['的', '了', '是', '我', '你', '他', '她', '们','有','字',
              '很','写','比较','像','看起来','感觉','一','个','着','在',
              '看上去','因为','一个','小人','跟']

# 过滤分词结果，删除停用词
seg_filtered = [word for word in seg_list if word not in stop_words]

# 将分词结果转换为字符串
seg_str = " ".join(seg_filtered)

# 生成词云图
wordcloud.generate(seg_str)

# 显示词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
