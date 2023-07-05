import streamlit as st
import random
import pandas as pd
st.markdown("## 命名实体识别")
st.markdown('命名实体识别NER（Named Entity Recognition），它是自然语言处理（NLP）领域中的一个重要任务。'
            'NER的目标是从文本中识别出具有特定意义的命名实体，例如人名、地名、组织机构名、时间、日期、货币等。'
            'NER的应用非常广泛，包括信息抽取、问答系统、机器翻译、文本分类等。通过识别出文本中的命名实体，可以帮助理解文本的含义，提取关键信息，并进行更深入的语义分析和推理。')
st.markdown("## 面向中文音乐领域命名实体识别")
st.markdown('面向中文音乐领域的命名实体识别是指从文本中自动识别和提取出具有特定意义的实体名称，例如歌手名、专辑名、歌曲名、乐队名等。'
            '在中文音乐领域，NER的应用可以帮助实现音乐信息的自动化处理、搜索和分析，提升用户体验和效率。')
st.markdown("## 关系抽取")
st.markdown('关系抽取（Relation Extraction）是自然语言处理（NLP）中的一个任务，旨在从文本中提取出实体之间的关系或关联信息。该任务涉及识别文本中的实体，并确定它们之间的关系类型和具体关系。'
            '关系抽取在很多应用场景中起着重要作用，如信息抽取、问答系统、知识图谱构建等。通过识别和抽取实体之间的关系，可以帮助构建结构化的知识库，从大规模文本数据中提取有用的信息，并支持更高级的语义理解和推理。'
            )
st.markdown("## 面向中文音乐领域关系抽取")
st.markdown('面向中文音乐领域的关系抽取任务中，我们可以关注一些特定的关系类型和实体。'
            '关系抽取在中文音乐领域的应用非常广泛，它可以用于构建音乐知识图谱、推荐相关歌曲和歌手、分析音乐社交网络等。通过准确抽取出实体之间的关系，可以为音乐领域的研究和应用提供更深入的信息和洞察。')
st.balloons()
st.markdown('### 音乐实体类型介绍')
st.write(pd.DataFrame({
    "entity": ["人物", "音乐", "专辑",'影视','游戏','时间','组织','别名'],
    "introduction": ["包括歌手，组合，乐队，作词家，作曲家，编曲家等等",
                         "中文歌曲",
                         "音乐专辑",
                         "电影，电视剧，动漫等",
                         "各种手游，网游等",
                         "音乐、专辑发行时间",
                         "唱片公司，经纪公司等",
                         "歌手的昵称，英文名，外号等"],
}))
st.markdown('### 音乐关系类型介绍')
df = pd.DataFrame({
    "relation": ["艺术家-歌曲", "艺术家-专辑", "歌曲-专辑",'作词','作曲','编曲','插曲','艺术家-组织','合作','歌曲发行时间','专辑发行时间','其他'],
    "introduction": ["表明某首歌由某位歌手或组合演唱，属于他们的作品","表明某张专辑是某位歌手或组合的作品","表明某首歌曲属于某张专辑","作词家为某首歌曲作词", "作曲家为某首歌曲作曲","编曲家为某首歌曲编曲","表明某首歌曲为某部影视的插曲、片尾曲、主题曲","表明某位歌手或者组合属于某一经纪公司或唱片公司","表明两人共同完成某首作品或者合唱一首作品","某首歌曲的发行时间","某张专辑的发行时间","表明实体间的关系不属于上述类型"]
})
st.table(df)
def entity_analyzer(my_text):
    result = "{\"Person\": \"[周杰伦]\", \"Song\": \"[稻香]\"}"
    return(result)
def relation_extraction(my_text):
    # consequence = "{周杰伦 艺术家-歌曲 稻香}"
    consequence = "{周杰伦 艺术家-歌曲 稻香}"
    return consequence

def main():
    # Title
    st.title("NLP with Streamlit")
    st.subheader("Natural Language Processing On the Go..")
    st.markdown("""
        	#### Description
        	+ This is a Natural Language Processing(NLP) Based App useful for basic NLP task
        	""")
    if st.checkbox("Show Named Entities"):
        st.markdown('### 音乐命名实体识别示例')
        st.subheader('Analyze Your Text')
        message = st.text_area('Enter Text(例如:周杰伦的稻香)', 'Type Here..')
        if st.button('entity extraction'):
            entity_result = entity_analyzer(message)
            st.markdown('命名实体识别的结果是: ')
            st.json(entity_result)   #success
    if st.checkbox("Show relation extraction"):
        st.markdown('### 音乐关系抽取示例')
        st.subheader('Analyze Your Text')
        message = st.text_area('Enter Text(例如:周杰伦的稻香)', 'Type Here..')
        if st.button('relation extraction'):
            re_result = relation_extraction(message)
            st.markdown('命名实体识别的结果是: ')
            st.success(re_result)  # success

if __name__ == '__main__':
	main()