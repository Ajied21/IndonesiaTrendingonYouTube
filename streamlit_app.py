import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import requests
import json
import webbrowser
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from PIL import Image

sns.set_style('whitegrid')

#Load Data

YT_df = pd.read_csv('CSV file/Youtubetrend.csv', low_memory=False)

#Data months

month_1 = YT_df.loc[YT_df['publish_month']==1].sort_values(['view','title'],ascending=False).head(10)
month_2 = YT_df.loc[YT_df['publish_month']==2].sort_values(['view','title'],ascending=False).head(10)
month_3 = YT_df.loc[YT_df['publish_month']==3].sort_values(['view','title'],ascending=False).head(10)
month_4 = YT_df.loc[YT_df['publish_month']==4].sort_values(['view','title'],ascending=False).head(10)
month_5 = YT_df.loc[YT_df['publish_month']==5].sort_values(['view','title'],ascending=False).head(10)
month_6 = YT_df.loc[YT_df['publish_month']==6].sort_values(['view','title'],ascending=False).head(10)
month_7 = YT_df.loc[YT_df['publish_month']==7].sort_values(['view','title'],ascending=False).head(10)
month_8 = YT_df.loc[YT_df['publish_month']==8].sort_values(['view','title'],ascending=False).head(10)
month_9 = YT_df.loc[YT_df['publish_month']==9].sort_values(['view','title'],ascending=False).head(10)
month_10 = YT_df.loc[YT_df['publish_month']==10].sort_values(['view','title'],ascending=False).head(10)
month_11 = YT_df.loc[YT_df['publish_month']==11].sort_values(['view','title'],ascending=False).head(10)
month_12 = YT_df.loc[YT_df['publish_month']==12].sort_values(['view','title'],ascending=False).head(10)

st.set_page_config(
	 layout="wide",
     page_title="Dhoifullah Luth Majied",
     page_icon=":bar_chart:",
     initial_sidebar_state="expanded",
     menu_items= None,
 )

def load_lottieurl(url: str):
	r = requests.get(url)
	if r.status_code != 200:
		return None
	return r.json()

lottie_1= load_lottieurl('https://assets6.lottiefiles.com/packages/lf20_g8iumlrs.json')
st_lottie(lottie_1, speed=1, height=255, key="initial")

#Columns Menu

selected = option_menu(
	menu_title= None,
	options=["Profile", "Project", "Contact"], 
    icons=['person-square', 'briefcase', "envelope"], 
    menu_icon="cast", 
    default_index=0, 
    orientation="horizontal",
)

#Columns Profile

if selected == "Profile":

        lottie_2= load_lottieurl('https://assets5.lottiefiles.com/packages/lf20_dzn3alb1.json')
        st_lottie(lottie_2, speed=1, height=200)

        st.markdown("<h1 style='text-align: center;'>Welcome My Portfolio</h1>", unsafe_allow_html=True)
        
        col1, col2, col3,col4 = st.columns(4)
        with col1:
                st.write(" ")
        with col2:
                st.image("Images/fotoprofile.png", width= 305)
        with col3:
                st.markdown("<h2 style='text-align: left;color:Red;font-size:18px'>I'm Dhoifullah Luth Majied</h2>", unsafe_allow_html=True)
                st.markdown('<div style="text-align: justify;">"A graduate of management with a concentration in marketing who has experience in running social media campaigns. I’m also creatived in creating pillar content on social media, Microsoft Office (word, excel and power point) and graphic design (Adobe Photoshop and Adobe Illustrator), able to understand organic social media, advertising, marketing and process data analysis with Python, MySQL, Big Query and Google Colab."</div>', unsafe_allow_html=True)
        with col4:
                st.write(" ")

        st.markdown("<h2 style='text-align: center;'>Hobby</h2>", unsafe_allow_html=True)
        col1, col2, col3,col4, col5, col6, col7 = st.columns(7)
        with col1:
                st.write(" ")
        with col2:
                st.image("Images/bola.png", caption='Futsal',width= 105)
        with col3:
                st.image("Images/coding&desain.png", caption='Coding & Design',width= 105)
        with col4:
                st.image("Images/traveling.png", caption='Travelling',width= 105)
        with col5:
                st.image("Images/e-sport.png", caption='E-Sports',width= 105)
        with col6:
                st.image("Images/investment.png", caption='Investment',width= 105)
        with col7:
                st.write(" ")

        st.markdown("<h2 style='text-align: center;'>Tools and Devices</h2>", unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
                st.write(" ")
        with col2:
                st.image("Images/Gambar1.jpg", width= 650)
        with col3:
                st.write(" ")
        with col4:
                st.write(" ")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
                st.write(" ")
        with col2:
                st.image("Images/Gambar2.jpg", width= 650)
        with col3:
                st.write(" ")
        with col4:
                st.write(" ")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
                st.write(" ")
        with col2:
                st.image("Images/Gambar3.jpg", width= 650)
        with col3:
                st.write(" ")
        with col4:
                st.write(" ")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
                st.write(" ")
        with col2:
                st.image("Images/Gambar4.jpg", width= 650)
        with col3:
                st.write(" ")
        with col4:
                st.write(" ")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
                st.write(" ")
        with col2:
                st.image("Images/Gambar5.jpg", width= 650)
        with col3:
                st.write(" ")
        with col4:
                st.write(" ")

        st.markdown("<h6 style='text-align: center'>Copyright &copy; 2022</h6>", unsafe_allow_html=True)

#Columns Project

if selected == "Project":

        lottie_3= load_lottieurl('https://assets7.lottiefiles.com/private_files/lf30_bntlaz7t.json')
        st_lottie(lottie_3, speed=2, height=200)

        st.markdown("<h1 style='text-align: center;'>Indonesia's Trending YouTube Video 2021</h1>", unsafe_allow_html=True)

        st.markdown("<h7 style='text-align: justify;'>This application shows the development of YouTube trends in 2021 where I have carried out the process of exploratory data analysis and cleaning data. Next, i display my visualization results by taking data on the variable x (title, channel_name) and variable y (view, like, dislike, comments) which I use as an analysis to see trending videos and channel names YouTube in 2021.</h7>", unsafe_allow_html=True)

        option = st.selectbox('Choose Month :', ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'))

        if option == "January":

                st.markdown("<h3 style='text-align: center;'>Top 10 Viewers and Video Trending on January 2021</h3>", unsafe_allow_html=True)

                month_j = px.bar(
                data_frame=month_1,
                x="view",
                y="title",
                orientation="h",
                height=600,
                width=1000,
                color_discrete_sequence=["#dc3912"],
                template="plotly_white",
                text_auto=True,
                )
                
                month_j.update_layout(
                plot_bgcolor="rgba(0,0,0,0)",
                xaxis=(dict(showgrid=False))
                )

                month_j.update_traces(
                textfont_size=14, 
                textangle=0, 
                )

                month_j.update_yaxes(
                categoryorder='total ascending'
                )

                st.plotly_chart(month_j)

        if option == "February":

                st.markdown("<h3 style='text-align: center;'>Top 10 Viewers and Video Trending on February 2021</h3>", unsafe_allow_html=True)

                month_f = px.bar(
                data_frame=month_2,
                x="view",
                y="title",
                orientation="h",
                height=600,
                width=1000,
                color_discrete_sequence=["#dc3912"],
                template="plotly_white",
                text_auto=True,
                )
                
                month_f.update_layout(
                plot_bgcolor="rgba(0,0,0,0)",
                xaxis=(dict(showgrid=False))
                )

                month_f.update_traces(
                textfont_size=14, 
                textangle=0, 
                )

                month_f.update_yaxes(
                categoryorder='total ascending'
                )

                st.plotly_chart(month_f)

        if option == "March":

                st.markdown("<h3 style='text-align: center;'>Top 10 Viewers and Video Trending on March 2021</h3>", unsafe_allow_html=True)

                month_m = px.bar(
                data_frame=month_3,
                x="view",
                y="title",
                orientation="h",
                height=600,
                width=1000,
                color_discrete_sequence=["#dc3912"],
                template="plotly_white",
                text_auto=True,
                )
                
                month_m.update_layout(
                plot_bgcolor="rgba(0,0,0,0)",
                xaxis=(dict(showgrid=False))
                )

                month_m.update_traces(
                textfont_size=14, 
                textangle=0, 
                )

                month_m.update_yaxes(
                categoryorder='total ascending'
                )

                st.plotly_chart(month_m)

        if option == "April":

                st.markdown("<h3 style='text-align: center;'>Top 10 Viewers and Video Trending on April 2021</h3>", unsafe_allow_html=True)

                month_a = px.bar(
                data_frame=month_4,
                x="view",
                y="title",
                orientation="h",
                height=600,
                width=1000,
                color_discrete_sequence=["#dc3912"],
                template="plotly_white",
                text_auto=True,
                )
                
                month_a.update_layout(
                plot_bgcolor="rgba(0,0,0,0)",
                xaxis=(dict(showgrid=False))
                )

                month_a.update_traces(
                textfont_size=14, 
                textangle=0, 
                )

                month_a.update_yaxes(
                categoryorder='total ascending'
                )

                st.plotly_chart(month_a)

        if option == "May":

                st.markdown("<h3 style='text-align: center;'>Top 10 Viewers and Video Trendingon May 2021</h3>", unsafe_allow_html=True)

                month_ma = px.bar(
                data_frame=month_5,
                x="view",
                y="title",
                orientation="h",
                height=600,
                width=1000,
                color_discrete_sequence=["#dc3912"],
                template="plotly_white",
                text_auto=True,
                )
                
                month_ma.update_layout(
                plot_bgcolor="rgba(0,0,0,0)",
                xaxis=(dict(showgrid=False))
                )

                month_ma.update_traces(
                textfont_size=14, 
                textangle=0, 
                )

                month_ma.update_yaxes(
                categoryorder='total ascending'
                )

                st.plotly_chart(month_ma)

        if option == "June":

                st.markdown("<h3 style='text-align: center;'>Top 10 Viewers and Video Trending on June 2021</h3>", unsafe_allow_html=True)

                month_jun = px.bar(
                data_frame=month_6,
                x="view",
                y="title",
                orientation="h",
                height=600,
                width=1000,
                color_discrete_sequence=["#dc3912"],
                template="plotly_white",
                text_auto=True,
                )
                
                month_jun.update_layout(
                plot_bgcolor="rgba(0,0,0,0)",
                xaxis=(dict(showgrid=False))
                )

                month_jun.update_traces(
                textfont_size=14, 
                textangle=0, 
                )

                month_jun.update_yaxes(
                categoryorder='total ascending'
                )

                st.plotly_chart(month_jun)

        if option == "July":

                st.markdown("<h3 style='text-align: center;'>Top 10 Viewers and Video Trending on July 2021</h3>", unsafe_allow_html=True)

                month_jul = px.bar(
                data_frame=month_7,
                x="view",
                y="title",
                orientation="h",
                height=600,
                width=1000,
                color_discrete_sequence=["#dc3912"],
                template="plotly_white",
                text_auto=True,
                )
                
                month_jul.update_layout(
                plot_bgcolor="rgba(0,0,0,0)",
                xaxis=(dict(showgrid=False))
                )

                month_jul.update_traces(
                textfont_size=14, 
                textangle=0, 
                )

                month_jul.update_yaxes(
                categoryorder='total ascending'
                )

                st.plotly_chart(month_jul)

        if option == "August":

                st.markdown("<h3 style='text-align: center;'>Top 10 Viewers and Video Trending on August 2021</h3>", unsafe_allow_html=True)

                month_au = px.bar(
                data_frame=month_8,
                x="view",
                y="title",
                orientation="h",
                height=600,
                width=1000,
                color_discrete_sequence=["#dc3912"],
                template="plotly_white",
                text_auto=True,
                )
                
                month_au.update_layout(
                plot_bgcolor="rgba(0,0,0,0)",
                xaxis=(dict(showgrid=False))
                )

                month_au.update_traces(
                textfont_size=14, 
                textangle=0, 
                )

                month_au.update_yaxes(
                categoryorder='total ascending'
                )

                st.plotly_chart(month_au)

        if option == "September":

                st.markdown("<h3 style='text-align: center;'>Top 10 Viewers and Video Trending on September 2021</h3>", unsafe_allow_html=True)

                month_s = px.bar(
                data_frame=month_9,
                x="view",
                y="title",
                orientation="h",
                height=600,
                width=1000,
                color_discrete_sequence=["#dc3912"],
                template="plotly_white",
                text_auto=True,
                )
                
                month_s.update_layout(
                plot_bgcolor="rgba(0,0,0,0)",
                xaxis=(dict(showgrid=False))
                )

                month_s.update_traces(
                textfont_size=14, 
                textangle=0, 
                )

                month_s.update_yaxes(
                categoryorder='total ascending'
                )

                st.plotly_chart(month_s)

        if option == "October":

                st.markdown("<h3 style='text-align: center;'>Top 10 Viewers and Video Trending on October 2021</h3>", unsafe_allow_html=True)

                month_o = px.bar(
                data_frame=month_10,
                x="view",
                y="title",
                orientation="h",
                height=600,
                width=1000,
                color_discrete_sequence=["#dc3912"],
                template="plotly_white",
                text_auto=True,
                )
                
                month_o.update_layout(
                plot_bgcolor="rgba(0,0,0,0)",
                xaxis=(dict(showgrid=False))
                )

                month_o.update_traces(
                textfont_size=14, 
                textangle=0, 
                )

                month_o.update_yaxes(
                categoryorder='total ascending'
                )

                st.plotly_chart(month_o)

        if option == "November":

                st.markdown("<h3 style='text-align: center;'>Top 10 Viewers and Video Trending on November 2021</h3>", unsafe_allow_html=True)

                month_no = px.bar(
                data_frame=month_11,
                x="view",
                y="title",
                orientation="h",
                height=600,
                width=1000,
                color_discrete_sequence=["#dc3912"],
                template="plotly_white",
                text_auto=True,
                )
                
                month_no.update_layout(
                plot_bgcolor="rgba(0,0,0,0)",
                xaxis=(dict(showgrid=False))
                )

                month_no.update_traces(
                textfont_size=14, 
                textangle=0, 
                )

                month_no.update_yaxes(
                categoryorder='total ascending'
                )

                st.plotly_chart(month_no)

        if option == "December":

                st.markdown("<h3 style='text-align: center;'>Top 10 Viewers and Video Trending on December 2021</h3>", unsafe_allow_html=True)

                month_d = px.bar(
                data_frame=month_12,
                x="view",
                y="title",
                orientation="h",
                height=600,
                width=1000,
                color_discrete_sequence=["#dc3912"],
                template="plotly_white",
                text_auto=True,
                )
                
                month_d.update_layout(
                plot_bgcolor="rgba(0,0,0,0)",
                xaxis=(dict(showgrid=False))
                )

                month_d.update_traces(
                textfont_size=14, 
                textangle=0, 
                )

                month_d.update_yaxes(
                categoryorder='total ascending'
                )

                st.plotly_chart(month_d)

        st.markdown("<h3 style='text-align: center;color:black'>Total View Top 10 Title Videos Trending in 2021</h3>", unsafe_allow_html=True)

        top_title_by_views_1 = YT_df.groupby('title').agg({'view':'sum'})
        top_title_by_views_1 = top_title_by_views_1.sort_values('view',ascending=False)
        top_title_by_views_1['view']=top_title_by_views_1['view'].apply(lambda x:int(x))
        top_title_by_views_1 = top_title_by_views_1.head(10)

        col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12=st.columns(12)
        with col1:
                st.write(" ")
        with col2:
                top_10_title= px.bar(
                data_frame=top_title_by_views_1,
                orientation="h",
                height=600,
                width=1000,
                color_discrete_sequence=["#3366cc"],
                template="plotly_white",
                opacity=0.9,
                text_auto=True,
                )
                
                top_10_title.update_layout(
                plot_bgcolor="rgba(0,0,0,0)",
                xaxis=(dict(showgrid=False))
                )

                top_10_title.update_traces(
                textfont_size=14, 
                textangle=0, 
                )

                top_10_title.update_yaxes(
                categoryorder='total ascending'
                )

                st.plotly_chart(top_10_title)
        with col3:
                st.write(" ")
        with col4:
                st.write(" ")
        with col5:
                st.write(" ")
        with col6:
                st.write(" ")
        with col7:
                st.write(" ")
        with col8:
                st.write(" ")
        with col9:
                st.write(" ")
        with col10:
                st.write(" ")
        with col11:
                st.write(" ")
        with col12:
                st.write(" ")

        st.markdown("<h3 style='text-align: center;color:black'>Total Like, Dislike and Comment by 10 Top Title Videos Trending in 2021</h3>", unsafe_allow_html=True)

        YT_df_1=YT_df.reset_index()
        YT_df_1.columns=['index','publish_time','publish_month','channel_name','title','local_title','local_description','description','view','like','dislike','comment','trending_time','duration (minutes)']
        YT_df_1=YT_df_1.head(10)

        col1,col2,col3=st.columns(3)
        with col1:
                st.write(" ")
        with col2:
                Top_10_video_like = px.pie(YT_df_1, values='like', names='title', hover_data=['dislike','comment'], labels={'title':'none'})
                Top_10_video_like.update_traces(textposition='inside',textinfo='percent')
                Top_10_video_like.update_layout(uniformtext_minsize=14, uniformtext_mode='hide')
                Top_10_video_like.update_layout(margin=dict(t=40, b=40, l=40, r=40))
                st.plotly_chart(Top_10_video_like)
        with col3:
                st.write(" ")

        st.markdown("<h3 style='text-align: center;color:black'>Total Uploads Video by Top 10 Channel Popularity in 2021</h3>", unsafe_allow_html=True)

        top_channel_by_views_2 = YT_df.groupby('channel_name').agg({'view':'sum','like':'sum','dislike':'sum','comment':'sum','title':'count'})
        top_channel_by_views_2 = top_channel_by_views_2.sort_values('view',ascending=False)
        top_channel_by_views_2['view']=top_channel_by_views_2['view'].apply(lambda x:int(x))
        top_channel_by_views_2 = top_channel_by_views_2.head(10)

        col1,col2,col3,col4,col5,col6,col7,col8,col9,col10=st.columns(10)
        with col1:
                st.write(" ")
        with col2:
                top_10_channel= px.bar(
                data_frame=top_channel_by_views_2,
                orientation="v",
                height=500,
                width=1000,
                opacity=0.9,
                color_discrete_sequence=["#3366cc", "#109618", "#dc3912", "#990099", "#FF9900"],
                template="plotly_white",
                barmode="relative",
                text_auto=True,
                )
                
                top_10_channel.update_layout(
                plot_bgcolor="rgba(0,0,0,0)",
                barmode='stack',
                xaxis=(dict(showgrid=False))
                )

                top_10_channel.update_traces(
                textfont_size=14, 
                textangle=0, 
                textposition="outside", 
                cliponaxis=False,
                )

                st.plotly_chart(top_10_channel)
        with col3:
                st.write(" ")
        with col4:
                st.write(" ")
        with col5:
                st.write(" ")
        with col6:
                st.write(" ")
        with col7:
                st.write(" ")
        with col8:
                st.write(" ")
        with col9:
                st.write(" ")
        with col10:
                st.write(" ")

        st.markdown("<h3 style='text-align: center;color:black'>Total Like, Dislike, and Comment Video by Top 10 Channel Popularity in 2021</h3>", unsafe_allow_html=True)

        col1,col2,col3,col4,col5,col6=st.columns(6)
        with col1:
                st.write(" ")
        with col2:
                Top_10_channel_like = px.pie(YT_df_1, values='like', names='channel_name', hover_data=['dislike','comment'], labels={'title':'none'})
                Top_10_channel_like.update_traces(textposition='inside',textinfo='percent')
                Top_10_channel_like.update_layout(uniformtext_minsize=16, uniformtext_mode='hide')
                Top_10_channel_like.update_layout(margin=dict(t=30, b=30, l=30, r=30))
                st.plotly_chart(Top_10_channel_like)
        with col3:
                st.write(" ")
        with col4:
                st.write(" ")
        with col5:
                st.write(" ")
        with col6:
                st.write(" ")

        st.markdown("<h3 style='text-align: center;color:black'>Top 10 channel indonesia more uploaded video in 2021</h3>", unsafe_allow_html=True)

        top_channel_by_views_3 = YT_df.groupby('channel_name').agg({'title':'count'})
        top_channel_by_views_3 = top_channel_by_views_3.sort_values('title',ascending=False)
        top_channel_by_views_3['title']=top_channel_by_views_3['title'].apply(lambda x:int(x))
        top_channel_by_views_3 = top_channel_by_views_3.head(10)

        col1,col2,col3,col4,col5,col6,col7,col8,col9,col10=st.columns(10)
        with col1:
                st.write(" ")
        with col2:
                mosthly_10_channel_indonesia= px.bar(
                data_frame=top_channel_by_views_3,
                orientation="v",
                height=500,
                width=1000,
                color_discrete_sequence=["#ff9900"],
                template="plotly_white",
                text_auto=True,
                )
                
                mosthly_10_channel_indonesia.update_layout(
                plot_bgcolor="rgba(0,0,0,0)",
                xaxis=(dict(showgrid=False))
                )

                mosthly_10_channel_indonesia.update_traces(
                textfont_size=14, 
                textangle=0, 
                )

                st.plotly_chart(mosthly_10_channel_indonesia)
        with col3:
                st.write(" ")
        with col4:
                st.write(" ")
        with col5:
                st.write(" ")
        with col6:
                st.write(" ")
        with col7:
                st.write(" ")
        with col8:
                st.write(" ")
        with col9:
                st.write(" ")
        with col10:
                st.write(" ")

        st.markdown("<h3 style='text-align: center;color:black'>The Correlations</h3>", unsafe_allow_html=True)

        col1,col2,col3,col4,col5,col6,col7,col8,col9,col10=st.columns(10)
        with col1:
                st.write(" ")
        with col2:
                heatmap = px.imshow(YT_df.drop('publish_month',axis=1).corr(), labels=dict(x="Correlation Between Each Columns", y="Variable", color="Value"), text_auto=True, aspect="auto")
                heatmap.update_xaxes(side="top")
                heatmap.layout.height = 600
                heatmap.layout.width = 900
                st.write(heatmap)
        with col3:
                st.write(" ")
        with col4:
                st.write(" ")
        with col5:
                st.write(" ")
        with col6:
                st.write(" ")
        with col7:
                st.write(" ")
        with col8:
                st.write(" ")
        with col9:
                st.write(" ")
        with col10:
                st.write(" ")
 
        st.markdown("<h3 style='text-align: center;color:black'>The List of Words That Are Often Searched On Youtube by Indonesian Viewers in 2021</h3>", unsafe_allow_html=True)
             
        col1,col2,col3,col4,col5,col6=st.columns(6)
        with col1:
                st.write(" ")
        with col2:
                st.image("Images/wr.png", width=750, channels="RGB", output_format="auto")
        with col3:
                st.write(" ")
        with col4:
                st.write(" ")
        with col5:
                st.write(" ")
        with col6:
                st.write(" ")

        col1,col2=st.columns(2)
        with col1:
                st.markdown("<h3 style='text-align: center;color:black'>Goal</h3>", unsafe_allow_html=True)
                st.write("The purpose of this visualization of the data is to be able to provide an overview of the data, provide brief knowledge of the trending youtube videos in 2021, display the diversity of creators, show the diversity of events currently happening on YouTube and around the world, and can be used as research material in the future.")
        with col2:
                st.markdown("<h3 style='text-align: center;color:black'>Results</h3>", unsafe_allow_html=True)
                st.write("I can find hidden patterns in the data. With the information I got, I can decide that in 2021 the trending video and youtube channel will be the video with the title BTS (방탄소년단) 'Butter' Official MV and as for the channel, HYBE LABELS. With this popularity, I can conclude that the majority of Indonesians, especially the millennial generation, prefer or favorite the video. In the application above, of course, it is certain that it will continue to increase and develop every time depending on the channel that promotes the video.")

        st.markdown("<h3 style='text-align: center;color:black'>Data Trends Video on Youtube in 2021</h3>", unsafe_allow_html=True)

        #st.dataframe(YT_df)
	
        col1,col2,col3=st.columns(3)
	 with col1:
		"""
        	Dataset Created on [Kaggle](https://www.kaggle.com/")
        	"""
	 with col2:
		f"""
        	[![GitHub Repo watchers](https://img.shields.io/github/watchers/Ajied21/IndonesiaTrendingonYouTubein2021?style=social)][gh]

        	[gh]: https://github.com/Ajied21/IndonesiaTrendingonYouTube
        	"""
	 with col3:
		st.download_button(
		label="Download Data (CSV)",
		data=YT_df.to_csv(),
		file_name='Youtubetrend.csv',
		mime='text/csv',
		)
	
	st.markdown("<h6 style='text-align: center'>Copyright &copy; 2022</h6>", unsafe_allow_html=True)

#Columns Contact

if selected == "Contact":

        lottie_5= load_lottieurl('https://assets8.lottiefiles.com/packages/lf20_klyobmoq.json')
        st_lottie(lottie_5, speed=1, height=200)

        st.markdown("<h1 style='text-align: center;'>More Information</h1>", unsafe_allow_html=True)

        st.markdown("<h3 style='text-align: center;'>Thank You...</h3>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center;'>If You Require Any Further Information Feel Free to Contact Me</h6>", unsafe_allow_html=True)

        col1,col2,col3=st.columns(3)
        with col1:
                st.write()
        with col2:
                st.write("Please Click The Contact Below and Connect With Me :point_down:")
        with col3:
                st.write()

        col1,col2,col3,col4,col5=st.columns(5)
        with col1:
                st.markdown("###### [![this is an image link](https://imgur.com/wteSenr.png)](https://api.whatsapp.com/send?phone=087787106077)")
        with col2:
                st.markdown("###### [![this is an image link](https://imgur.com/6WMJii5.png)](https://mail.google.com/mail/u/0/?view=cm&tf=1&fs=1&to=dhoifullah.luthmajied05@gmail.com)")
        with col3:               
                st.markdown("###### [![this is an image link](https://imgur.com/ym2j1LR.png)](https://www.linkedin.com/in/dhoifullahluthmajied/)")
        with col4:
                st.markdown("###### [![this is an image link](https://imgur.com/6VGjF5d.png)](https://www.instagram.com/ajied_dhoifullah/)")
        with col5:
                st.markdown("###### [![this is an image link](https://imgur.com/rBdMWct.png)](https://twitter.com/Ajied_Dhoifulah)")

        st.markdown("<h6 style='text-align: center'>Copyright &copy; 2022</h6>", unsafe_allow_html=True)


hide_menu_style = """
       <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
