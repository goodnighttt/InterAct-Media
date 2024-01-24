import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# 读取评论数据
with open('reasons-write.txt', 'r', encoding='utf-8') as file:
    comments = file.read()

# 使用jieba进行分词
seg_list = jieba.cut(comments)

# 要删除的词语列表
stop_words = ['的', '了', '是', '我', '你', '他', '她', '们','有','字',
              '很','写','比较','像','看起来','感觉','一','个','着','在','看上去','因为','一个','小人']

# 过滤分词结果，删除停用词
seg_filtered = [word for word in seg_list if word not in stop_words]

# 将分词结果转换为字符串
seg_str = " ".join(seg_filtered)

# 创建词云对象，并指定字体文件路径
font_path = '鸿雷拙书简体.otf'  # 替换为你自己的字体文件路径
wordcloud = WordCloud(width=800, height=400, background_color='white', font_path=font_path).generate(seg_str)

# 显示词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
