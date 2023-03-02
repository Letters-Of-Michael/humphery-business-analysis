import streamlit as st
import pandas as pd
from IPython.display import IFrame
from PIL import Image
import matplotlib.pyplot as plt

header = st.container()
background = st.container()
dataset = st.container()
question = st.container()
Data_Development = st.container()
visualization = st.container()
copywright = st.container()


with header:
	st.title('Humphery Business Sales Analysis')
	st.write('A sales performance analysis to provide general insights about the business. The business owners and leaders use this to determine how viable sales strategies are, note areas that need improvement and track progress of sales ideas and strategies deployed. Overall, this analysis helps to provide pointers on revenue generating advantages of the business and to improve on these.')

	with background:
		st.header("COMPANY'S BACKGROUND")
		st.write('A multinational company that deals in manufacturing and sales of bicycle, bicycle parts, accessories and spare parts. They have market reach in over 6 countries which includes United States of America, Australia, Germany etc.')

	with dataset:
		st.header("Data gathered from the company's database.")
		st.write('Here, the dataset contains about 113, 036 recorded sales activities, This includes sales and production activities over a period of 6 years (2011-2016).')

		sales_data = pd.read_csv('./image/JVEC.csv')
		st.write(sales_data.head())

	with question:
		st.header('Analysis Background')
		st.write('In this section, I provided more insights on some important questions that could arise during performance measurement. This insights will be a guide to our analysis and visualization as a whole')


		st.markdown('* **first:** How country, age, gender performed in contributing to the overall revenue generating for the company over the year.')
		st.markdown('* **second:** What the business currently delivers using certain metrics and how it compares to other years of being in the business.')


	with Data_Development:
		st.header('Data Development')
		st.write("I compiled the dataset from the company's database using SQL to create the table, preparing the table for the kind of data we expect for each entry, thereafter, I used python for the data cleaning process and to get the general overview of our dataset: removed unwanted columns, calculated the margin for each sales, then imported our data into microsoft powerbi for visualization and to answer our questions and guide our analysis.")



	with visualization:
		st.header('Time to visualize our data!')
		st.write('#SalesAnalysis, #DataAnalysis, #BusinessAnalysis, #BusinessIntelligence, #DataVisualization, #PowerBi')

		sel_col, disp_col = st.columns(2)

		#Dashboard = IFrame(src" ", width = 1000, height = 600)
		#display(Dashboard)

		img = Image.open("./image/8.jpg")
		st.image(img)

		#url = ('https://app.powerbi.com/view?r=eyJrIjoiZTNjOGI4YWItZTE3ZS00MDUwLTg4MGMtMzA3MDc5ZTliNGZjIiwidCI6IjhlOTVjNGQxLWRiZmQtNGFmNS1iODA2LTIwMGJkZDY2ZDJjZSJ9')
		#st.markdown(f'''<a href={url}><button style="background-color:GreenYellow;">Live-Dashboard</button></a>''', unsafe_allow_html=True)

		url = 'To view the interactive live dashboard on powerbi service, click  [Dashboard](https://app.powerbi.com/view?r=eyJrIjoiZTNjOGI4YWItZTE3ZS00MDUwLTg4MGMtMzA3MDc5ZTliNGZjIiwidCI6IjhlOTVjNGQxLWRiZmQtNGFmNS1iODA2LTIwMGJkZDY2ZDJjZSJ9)'
		st.markdown(url,unsafe_allow_html=True)

		#for web: <iframe title="Report Section" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiZTNjOGI4YWItZTE3ZS00MDUwLTg4MGMtMzA3MDc5ZTliNGZjIiwidCI6IjhlOTVjNGQxLWRiZmQtNGFmNS1iODA2LTIwMGJkZDY2ZDJjZSJ9" frameborder="0" allowFullScreen="true"></iframe>
		#for email: https://app.powerbi.com/view?r=eyJrIjoiZTNjOGI4YWItZTE3ZS00MDUwLTg4MGMtMzA3MDc5ZTliNGZjIiwidCI6IjhlOTVjNGQxLWRiZmQtNGFmNS1iODA2LTIwMGJkZDY2ZDJjZSJ9

	with copywright:
		st.text('By Oluwaseyi Michael')




