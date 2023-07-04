import streamlit as st
from PIL import Image


st.markdown("# 面向中文音乐领域命名实体识别")
st.markdown('面向中文音乐领域的命名实体识别（Named Entity Recognition, NER）是指从文本中自动识别和提取出具有特定意义的实体名称，例如歌手名、专辑名、歌曲名、乐队名等。在中文音乐领域，NER的应用可以帮助实现音乐信息的自动化处理、搜索和分析，提升用户体验和效率。')
image1 = Image.open('D:\\PycharmProjects\\pythonProject\\streamlit\\HG.png')
image2 = Image.open('D:\\PycharmProjects\\pythonProject\\streamlit\\music_entity.png')
# image3 = Image.open('D:\\PycharmProjects\\pythonProject\\streamlit\\songs.png')
# st.image(image3,caption='歌手节点展示')
# st.image(image2,caption='歌曲节点展示')
st.image(image1,caption='音乐知识图谱展示')
st.image(image2,caption='音乐实体类型说明')
st.balloons()

st.markdown("### 音乐命名实体识别示例")

video_file = open('D:\\PycharmProjects\\pythonProject\\streamlit\\music_ner.mp4','rb')
video_bytes = video_file.read()
st.video(video_bytes,format='video/mp4')



#text = st.text_input('输入一段文本后回车:(例如周杰伦的稻香) ').replace(' ', '')
st.markdown('输入一段文本:(例如周杰伦的稻香)')
st.markdown('命名实体识别的结果是:{''Person'':[周杰伦],''Song'':[稻香]}')
#st.write('{''Person'':[周杰伦],''Song'':[稻香]}')
