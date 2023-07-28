# -*- coding:utf-8 -*-
import streamlit as st
import random
import pandas as pd
st.markdown("## Named Entity Recognition")
st.markdown('Named Entity Recognition (NER) is an essential task in the field of Natural Language Processing (NLP). '
            'The goal of NER is to identify specific entities with meaningful names from the text, such as person names, location names, organization names, dates, times, currencies, etc.'
            'NER finds widespread applications in information extraction, question-answering systems, machine translation, text classification, and more. '
            'By recognizing named entities in the text, it helps in understanding the meaning of the text, extracting key information, and enabling more in-depth semantic analysis and reasoning.')


st.markdown("## NER for the Chinese music domain")
st.markdown('Named Entity Recognition (NER) for the Chinese music domain refers to the automatic identification and extraction of specific meaningful entity names from the text, '
            'such as singer names, album names, song names, band names, etc.'
            'In the Chinese music domain, the application of NER can facilitate automated processing, searching, and analysis of music information, thereby enhancing user experience and efficiency.')

st.markdown('### Music entity types')
# st.write(pd.DataFrame({
#     "entity": ["Person", "Music", "Album",'FTC','Game','Time','Organization','Alias'],
#     "introduction": ["including singers, groups, bands, lyricists, composers, arrangers, etc.",
#                          "chinese music",
#                          "music album",
#                          "films, tv series, cartoon, etc.",
#                          "including online games, hand games, etc.",
#                          "including songs, album release time,etc",
#                          "Including record labels, agencies, etc.",
#                          "Singer's nickname, nickname, English name, etc."],
# }))

df = pd.DataFrame({
    "entity": ["Person", "Music", "Album",'FTC','Game','Time','Organization','Alias'],
    "introduction": ["including singers, groups, bands, lyricists, composers, arrangers, etc.","chinese music", "music album","films, tv series, cartoon, etc.","including online games, hand games, etc.","including songs, album release time,etc","Including record labels, agencies, etc.","Singer's nickname, nickname, English name, etc."]
})

st.table(df)
st.markdown("## Relation Extraction")
st.markdown('Relation Extraction is a task in Natural Language Processing (NLP) that aims to extract relationships or associations between entities from text. '
            'This task involves identifying entities in the text and determining their relation types and specific relations.'
            'RE plays a crucial role in various application scenarios, such as information extraction, question-answering systems, knowledge graph construction, and more. '
            'By identifying and extracting relations between entities, it aids in building structured knowledge bases, extracting valuable information from large-scale textual data, and supporting advanced semantic understanding and reasoning.'
            )

st.markdown("## RE for Chinese music domain")
st.markdown('In the task of relation extraction for the Chinese music domain, we can focus on specific relationship types and entities.'
            'RE has extensive applications in the Chinese music domain, including constructing music knowledge graphs, recommending related songs and artists, analyzing music social networks, and more. '
            'By accurately extracting relations between entities, it can provide deeper insights and information for research and applications in the field of music.')
# st.balloons()
st.markdown('### Music relation types')
df = pd.DataFrame({
    "relation": ["Artist-music", "Artist-album", "Music-album",'Writing','Compose','Arrangement','Episode','Artist-organization','Cooperation','Music release date','Album release date','Other'],
    "introduction": ["Character-songs, indicating that a particular song belongs to a particular singer or group","Character-Album, indicating that an album belongs to a particular artist or group","Song-Album, indicating that the song is included in an album and belongs to one of the tracks","Characters - Songs, Lyricists for Songs", "Characters-songs, composers for songs","Characters - Songs, Arranger Arranges the Songs","Song - Movie or TV, indicating that the song is the theme, ending or interlude song of a movie or TV ","Artist-agency, indicating that a singer, band group belongs to a record label or agency","Character-Character, indicating that the two wrote or sang a song together","Song-Time, indicating when a song was released","Album-Time, indicating when an album was released","IndicatIng that the relationship between the two entities involved in the text is unknown or non-existent"]
})
st.table(df)
def entity_analyzer(my_text):
    if my_text == '周杰伦的稻香':
        a = "{\"Person\": \"[周杰伦]\", \"Song\": \"[稻香]\"}"
        return a
    if my_text == '宋祖英的好日子':
        b = "{\"Person\": \"[宋祖英]\", \"Song\": \"[好日子]\"}"
        return b
    if my_text == '林俊杰的曹操':
        c = "{\"Person\": \"[林俊杰]\", \"Song\": \"[曹操]\"}"
        return c

def relation_extraction(my_text):
    # consequence = "{周杰伦 艺术家-歌曲 稻香}"
    if my_text == '周杰伦的稻香':
        a = "{周杰伦 艺术家-歌曲 稻香}"
        return a
    if my_text == '宋祖英的好日子':
        b = "{宋祖英 艺术家-歌曲 好日子}"
        return b
    if my_text == '林俊杰的曹操':
        c = "{林俊杰 艺术家-歌曲 曹操}"
        return c

def main():
    # Title
    # st.subheader("Natural Language Processing On the Go..")
    st.markdown("""
        	## Description
        	+ This is a simple example of the Chinese music information extraction natural language task
        	""")
    if st.checkbox("Task 1: Chinese music NER"):
        st.markdown('### Music Named Entity Recognition Example')
        # st.subheader('analysis your text')
        message = st.text_area('Input your text(example:周杰伦的稻香)', 'Type Here..')
        if st.button('Entity extraction'):
            if message == '周杰伦的稻香':
                entity_result = entity_analyzer(message)
                st.markdown('The result of Named Entity Recognition: ')
                st.json(entity_result)   #success
            elif message == '宋祖英的好日子':
                entity_result = entity_analyzer(message)
                st.markdown('The result of Named Entity Recognition: ')
                st.json(entity_result)   #success
            elif message == '林俊杰的曹操':
                entity_result = entity_analyzer(message)
                st.markdown('The result of Named Entity Recognition: ')
                st.json(entity_result)   #success
            else:
                st.markdown('There was an error in your entry, please re-enter!')

    if st.checkbox("Task 2: Chinese music RE"):
        st.markdown('### Music relation extraction example')
        # st.subheader('analysis your text')
        text = st.text_area('Input your text(example:周杰伦的稻香)', 'Type Here..')
        if st.button('relation extraction'):
            if text == '周杰伦的稻香':
                re_result = relation_extraction(text)
                st.markdown('The result of Relation extraction: ')
                st.success(re_result)  # success

            elif text == '宋祖英的好日子':
                re_result = relation_extraction(text)
                st.markdown('The result of Relation extraction: ')
                st.success(re_result)  # success
            elif text == '林俊杰的曹操':
                re_result = relation_extraction(text)
                st.markdown('The result of Relation extraction: ')
                st.success(re_result)  # success
            else:
                st.markdown('There was an error in your entry, please re-enter!')

if __name__ == '__main__':
	main()