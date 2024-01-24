import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import jieba
filename = "D:\\pythonProject\\pachong\\zongjie.txt"
with open(filename,encoding='utf-8') as f:
    mytext = f.read()
mytext = " ".join(jieba.cut(mytext))
backgroud_Image = plt.imread('D:\\pythonProject\\pachong\\lingxing.jpg')
wc = WordCloud( background_color = 'white',
                mask = backgroud_Image,
                max_words = 2000,
                stopwords = STOPWORDS,
                font_path = 'D:\\pythonProject\\pachong\\songti.ttf',
                max_font_size = 100,
                color_func=None,
                random_state = 42,
                ).generate(mytext)
plt.imshow(wc)
image_colors = ImageColorGenerator(backgroud_Image)
wc.recolor(color_func = image_colors)
plt.imshow(wc)
plt.axis('off')
plt.show()
