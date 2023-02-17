###################################################################################################################
#bibliotecas e dependências

import sweetviz as sv
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport
import streamlit as st
import codecs
import streamlit.components.v1 as components
import datetime
from datetime import date
from PIL import Image

###################################################################################################################
#funções

@st.cache_data
def st_display_sweetviz(report_html,width=1000,height=500):
	report_file = codecs.open(report_html,'r')
	page = report_file.read()
	components.html(page,width=width,height=height,scrolling=True)

@st.cache_data	
def generate_report_sweetviz(df, target):
	if target == False:
		my_report = sv.analyze(df)
	else:
		feature_config = sv.FeatureConfig(force_num=target)
		my_report = sv.analyze(df, target_feat=target, feat_cfg=feature_config)
	st.success('🔰Done!')
	my_report.show_html(filepath='SWEETVIZ_REPORT.html', open_browser=True, layout='widescreen', scale=None)
	st_display_sweetviz("SWEETVIZ_REPORT.html")
	with open("SWEETVIZ_REPORT.html", "rb") as file:
	     btn = st.download_button(label="Download do relatório Sweetviz", data=file, file_name="SWEETVIZ_REPORT.html")

@st.cache_data	
def generate_report_pandas_profiling(df):
	profile = ProfileReport(df)
	st_profile_report(profile)


###################################################################################################################
#configuração do nome da aba e cabeçalhos do app

st.set_page_config(
    page_title="Orbe.ai - Exploratory Data Analysis",
    page_icon="📊",
)

st.title("📊 Orbe.ai - Exploratory Data Analysis")

###################################################################################################################
#configuração do frame Treine seu modelo:
with st.expander('Trabalhar com seus dados tabulares 🪟:'):	
	uploaded_file = st.file_uploader("Carregue seu arquivo em formato csv, xls ou xlsx", type = ['csv', 'xls', 'xlsx', 'parquet'])
	if uploaded_file is not None:
		if uploaded_file.name.endswith('.csv'):
			df = pd.read_csv(uploaded_file)
		elif uploaded_file.name.endswith('.xls') or uploaded_file.name.endswith('.xlsx'):
			df = pd.read_excel(uploaded_file)
		elif uploaded_file.name.endswith('.parquet'):
			df = pd.read_parquet(uploaded_file)
		else:
			st.error('⛔ Arquivo não está em formato planilha (csv, xls, xlsx)!')
			st.stop()
		
		for col in df.columns:
			weird = (df[[col]].applymap(type) != df[[col]].iloc[0].apply(type)).any(axis=1)
			if len(df[weird]) > 0:
				df = df.drop(col, 1)
		
		#df = pd.get_dummies(df)
		#head = st.checkbox('Visualizar primeiras Linhas')
		#if head:
		#	st.dataframe(df.head())
		#st.write(df.dtypes)
		biblio = st.selectbox('Qual biblioteca deseja utilizar?', ('Sweetviz', 'Pandas Profiling'))
		if biblio == 'Sweetviz':
			option = st.radio('Deseja definir a variável target?', ('Sim', 'Não'))
			if option == 'Sim':
				target = st.selectbox('Qual é a coluna target?', list(df.columns))
				if st.button("Gerar Visualização"):
					generate_report_sweetviz(df, target)
			else:
				target = False
				if st.button("Gerar Visualização"):
					generate_report_sweetviz(df, target)
		else:			
			if st.button("Gerar Visualização"):
				generate_report_pandas_profiling(df)
