# We import all necessary libraries

# Selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Options driver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

# Dataframes
import pandas as pd
import itertools
import os
from io import StringIO
import time
import requests

# Simulating human behavior
import time
from time import sleep
import random

# Clear data
import unidecode

# Json files
import json
import re
import numpy as np
import itertools
from pandas import json_normalize

# To use explicit waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Download files
import urllib.request
import requests
from openpyxl import Workbook

# Graphs files
from IPython.display import SVG, display, IFrame

# # pytesseract
# from PIL import Image
# from io import BytesIO
# import pytesseract
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# function bcrp_search()

def bcrp_search( series, frequency=None):
    ''' 
    Objective: 
    This function provides a basic searcher for the BCRP Database website. We provide the name of the series and the frequency we want
    and search for the data available. Ir returns a dataframe with all series that match our input.

    Input:
        series (str) : The name of the series we want, i.e: 'Inflación', 'PBI', 'Tasa de referencia', etc.

        frequency (str) : The frequency of the series, i.e: 'Mensual', 'Anual', 'Trimestral', etc.

    Output:
        The function creates a dataframe with all the series that match our input. The dataframe contains three columns:
        Código = Code of the series
        Descripción = Name of the series
        Frecuencia = The frequency of the series
    
    '''

    
    url     = 'https://estadisticas.bcrp.gob.pe/estadisticas/series/'
    options = Options()
    options.add_argument( '--headless' )
    driver  = webdriver.Chrome(options = options)        
    driver.get( url )
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    search_box = wait.until( EC.element_to_be_clickable( ( By.XPATH, '//*[@id="txtbuscador"]' ) ) )
    search_box.send_keys( series )
    search_box.send_keys(Keys.RETURN)

    table_element = wait.until ( EC.element_to_be_clickable( (By.XPATH, '//*[@id="consultadata"]') ) )
    table_html    = table_element.get_attribute( 'outerHTML' )
    table_html_io = StringIO( table_html )
    table_df      = pd.read_html( table_html_io )[ 0 ]
    table_df = table_df.drop(columns=['Unnamed: 0'])
    table_df = table_df[:-1]

    # If we specify the frequency, we filter only those that match the frequency desired
    if frequency != None:
       table_df = table_df[table_df['Frecuencia'] == frequency]
        
    return table_df



# function bcrp_scrapper()

def scrapper_diario( driver ):

    '''
    Objective: 
        This function is called within bcrp_scrapper(). It is used to scrap daily series.

    Input: 
        Our only input is the driver, which is defined inside bcrp_scrapper().

    Output:
        It returns a dataframe with the series
    '''

    month_s = ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Set','Oct','Nov','Dic']
    month_d = ['-01-','-02-','-03-','-04-','-05-','-06-','-07-','-08-','-09-','-10-','-11-','-12-']

    table_element = driver.find_element(By.XPATH, '//*[@id="frmDiarias"]/div[3]/table')
    table_html    = table_element.get_attribute( 'outerHTML' )
    table_html_io = StringIO( table_html )
    table_df      = pd.read_html( table_html_io )[ 0 ]

    for (s,d) in zip(month_s,month_d):
        table_df['Fecha'] = table_df['Fecha'].str.replace(s,d)
        
    table_df['Fecha'] = pd.to_datetime(table_df['Fecha'], format = '%d-%m-%y')
    table_df.set_index(table_df['Fecha'], inplace=True)
    table_df = table_df.drop(columns=['Fecha'])

    return table_df

def scrapper_mensual( driver ):

    '''
    Objective: 
        This function is called within bcrp_scrapper(). It is used to scrap monthly series.

    Input: 
        Our only input is the driver, which is defined inside bcrp_scrapper().

    Output:
        It returns a dataframe with the series
    '''
    
    month_s = ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']
    month_d = ['01-01-','01-02-','01-03-','01-04-','01-05-','01-06-','01-07-','01-08-','01-09-','01-10-','01-11-','01-12-']

    table_element = driver.find_element(By.XPATH, '//*[@id="frmMensual"]/div[3]/table')
    table_html    = table_element.get_attribute( 'outerHTML' )
    table_html_io = StringIO( table_html )
    table_df      = pd.read_html( table_html_io )[ 0 ]
    
    for (s,d) in zip(month_s,month_d):
        table_df['Fecha'] = table_df['Fecha'].str.replace(s,d)
        
    table_df['Fecha'] = pd.to_datetime(table_df['Fecha'], format = '%d-%m-%y')
    table_df.set_index(table_df['Fecha'], inplace=True)
    table_df = table_df.drop(columns=['Fecha'])

    return table_df

def scrapper_trimestral( driver ):

    '''
    Objective: 
        This function is called within bcrp_scrapper(). It is used to scrap quarterly series.

    Input: 
        Our only input is the driver, which is defined inside bcrp_scrapper().
    
    Output:
        It returns a dataframe with the series
    '''

    month_s = ['T1','T2','T3','T4']
    month_d = ['01-03-','01-06-','01-09-','01-12-']

    table_element = driver.find_element(By.XPATH, '//*[@id="frmTrimestral"]/div[3]/table')
    table_html    = table_element.get_attribute( 'outerHTML' )
    table_html_io = StringIO( table_html )
    table_df      = pd.read_html( table_html_io )[ 0 ]
    
    for (s,d) in zip(month_s,month_d):
        table_df['Fecha'] = table_df['Fecha'].str.replace(s,d)
        
    table_df['Fecha'] = pd.to_datetime(table_df['Fecha'], format = '%d-%m-%y')
    table_df.set_index(table_df['Fecha'], inplace=True)
    table_df = table_df.drop(columns=['Fecha'])

    return table_df 

def scrapper_anual( driver ):

    '''
    Objective: 
        This function is called within bcrp_scrapper(). It is used to scrap anual series.

    Input: 
        Our only input is the driver, which is defined inside bcrp_scrapper().

    Output:
        It returns a dataframe with the series
    '''

    table_element = driver.find_element(By.XPATH, '//*[@id="frmAnual"]/div[3]/table')
    table_html    = table_element.get_attribute( 'outerHTML' )
    table_html_io = StringIO( table_html )
    table_df      = pd.read_html( table_html_io )[ 0 ]
    table_df['Fecha'] = pd.to_datetime(table_df['Fecha'], format="%Y")
    table_df.set_index(table_df['Fecha'], inplace=True)
    table_df = table_df.drop(columns=['Fecha'])

    return table_df

def bcrp_scrapper( series , start_date , end_date , freq ):

    '''
    Objective: 
        This function scraps series from the BCRP Database and gives us a dataframe with the series.

    Input: 
        series (str/list) : The code of the series we want to webscrap, i.e: '	PN38705PM'. In case we want to scrap many series, we enter a list with each code 
                            separated by a coma, up to 10 codes, i.e: ['PN38706PM', 'PN38707PM', 'PN38708PM', 'PN38708PM']

        start_date (str)  : The starting date of the series. For daily series it must follow the patter 'yyyy-mm-dd'. For other frequencies it must 
                            follow 'yyyy-mm'. For anual series it can be specified just as 'yyyy'.

        end_date (str)    : The starting date of the series. For daily series it must follow the patter 'yyyy-mm-dd'. For other frequencies it must 
                            follow 'yyyy-mm'. For anual series it can be specified just as 'yyyy'.

        freq (str)        : The frequency of the series. It accepts one of the following values: 'Diaria', 'Mensual', 'Trimestral', 'Anual'. It is
                            important that freq matches the frequency of the code/codes in series.
 
    Output:
        It returns a dataframe with the series.
    '''
    
    base     = 'https://estadisticas.bcrp.gob.pe/estadisticas/series/api/'

    if isinstance( series , list):
        string = ''
        for element in series : 
            string += element
            string += '-'
        string =  string[:-1]
        serie  = string

    else:
        serie  =  series
    anio1     = start_date
    anio2     = end_date
    url       = base + serie + '/' + 'html' + '/' + anio1  + '/' + anio2
    options   = Options()
    options.add_argument( '--headless' )
    driver    = webdriver.Chrome(options = options)        
    driver.get( url )
    driver.maximize_window()

    if freq == 'Diario' :

        table_df = scrapper_diario( driver )

    elif freq == 'Mensual' :

        table_df = scrapper_mensual( driver )

    elif freq == 'Trimestral' :

        table_df = scrapper_trimestral( driver )

    else:

        table_df = scrapper_anual( driver )
        
    return table_df


def bcrp_dataframe( series , start_date , end_date, freq):
    '''
    Objective:
        This function uses the API interface of the Peruvian Central Bank of Reserve (BCRP) to create a pandas dataframe 
        with time series data available at the BCRP Statistics Database
    
    Input:
        series (str/list) = The code of the series that we will extract from the BCRP
        
        start_date (str)  = The starting date in format "yyyy-mm"
        
        end_date (str)    = The ending date in format "yyyy-mm"

        freq (str)        = The frequency of the series. It can have one the following values: 
                            "Diaria", " Mensual", "Trimestral", "Anual".
    Output:
        It returns a pandas dataframe with a time-series index including the series that we have extracted
         
    '''
    
    url_base = 'https://estadisticas.bcrp.gob.pe/estadisticas/series/api/'
    
    month_s  = ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']
    month_d  = ['-01-','-02-','-03-','-04-','-05-','-06-','-07-','-08-','-09-','-10-','-11-','-12-']

    month_s_mensual  = ['Ene.','Feb.','Mar.','Abr.','May.','Jun.','Jul.','Ago.','Sep.','Oct.','Nov.','Dic.']
    month_d_mensual = ['01-01-','01-02-','01-03-','01-04-','01-05-','01-06-','01-07-','01-08-','01-09-','01-10-','01-11-','01-12-']

    month_s_trimestral = ['T1.','T2.','T3.','T4.']
    month_d_trimestral = ['01-03-','01-06-','01-09-','01-12-']
    
    form_out = '/json'
    
    cod_var = series
    period = '/' + start_date + '/' + end_date
    
    df = pd.DataFrame()
    
    try:

        for j in cod_var:
            url_aux   = url_base + j + form_out + period
            resp      = requests.get(url_aux)
            resp_json = resp.json()
            periods   = resp_json['periods']

            value = []
            dates = []

            for i in periods:
                aux_dat = i['name']
                aux_val = i['values']
                dates.append(aux_dat)
                value.append(float(aux_val[0]))

            dict_aux = {'Fecha' : dates, 
                         resp_json['config']['series'][0]['name'] : value}
            df_aux = pd.DataFrame(dict_aux)
            
            if freq == 'Diario' :

                for (s,d) in zip(month_s,month_d):
                    df_aux['Fecha'] = df_aux['Fecha'].str.replace(s,d)
                df_aux['Fecha'] = pd.to_datetime(df_aux['Fecha'], format="%Y-%m-%d") 
            
            elif freq == 'Mensual' :

                for (s,d) in zip(month_s_mensual,month_d_mensual):
                    df_aux['Fecha'] = df_aux['Fecha'].str.replace(s,d)                    
                df_aux['Fecha'] = pd.to_datetime(df_aux['Fecha'], format="%d-%m-%Y") 

            elif freq == 'Trimestral' :

                for (s,d) in zip(month_s_trimestral,month_d_trimestral):
                    df_aux['Fecha'] = df_aux['Fecha'].str.replace(s,d)
                df_aux['Fecha'] = pd.to_datetime(df_aux['Fecha'], format="%d-%m-%y")            
                      
            
            df_aux.set_index(df_aux['Fecha'], inplace=True)
            df_aux = df_aux.drop(columns=['Fecha'])
            df    = pd.concat([df, df_aux], axis=1)
            
    except Exception as err:
        print(f'There has been an exception: {err}. Try with a different code.')
        
    return df


def bcrp_graph( series , start_date , end_date , format= 'png'):
    '''
    Objective: 
        This function scraps series from the BCRP Database and graphs the image in the given format.

    Input: 
        series (str/list) : The code of the series we want to webscrap, i.e: 'PN38705PM'. In case we want to scrap many series, we enter a list with each code 
                            separated by a coma, up to 10 codes, i.e: ['PN38706PM', 'PN38707PM', 'PN38708PM', 'PN38708PM']

        start_date (str)  : The starting date of the series. For daily series it must follow the patter 'yyyy-mm-dd'. For other frequencies it must 
                            follow 'yyyy-mm'. For anual series it can be specified just as 'yyyy'.

        end_date (str)    : The starting date of the series. For daily series it must follow the patter 'yyyy-mm-dd'. For other frequencies it must 
                            follow 'yyyy-mm'. For anual series it can be specified just as 'yyyy'.

        format (str)      : It tells us the format of the download. It can be 'jpg' or 'png'. By default it downloads a png picture.
 
    Output:
        It graphs the BCRP series after downloading it.
    '''


    base     = 'https://estadisticas.bcrp.gob.pe/estadisticas/series/api/'

    if isinstance( series , list):
        string = ''
        for element in series : 
            string += element
            string += '-'
        string =  string[:-1]
        serie  = string

    else:
        serie  =  series
    anio1     = start_date
    anio2     = end_date
    url       = base + serie + '/' + 'html' + '/' + anio1  + '/' + anio2
    options   = Options()
    # options.add_argument( '--headless' )
    driver    = webdriver.Chrome(options = options)        
    driver.get( url )
    driver.maximize_window()

    driver.find_element(By.XPATH, '//*[@id="btnGrafico"]').click()

    # We go to the next window and download the image in selected format.
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)

    # Depending on the format we choose, the image is downloaded    
    if format   == 'png':
        driver.find_element(By.XPATH, '//*[@id="chart-selector"]/li[2]/img').click()
        time.sleep(4)

    elif format == 'jpg':
        driver.find_element(By.XPATH, '//*[@id="chart-selector"]/li[1]/img').click()
        time.sleep(4)

    # elif format == 'pdf':
    #     driver.find_element(By.XPATH, '//*[@id="chart-selector"]/li[3]/img').click()
    #     time.sleep(4)

    download_dir = os.path.expanduser('~/Downloads')
    files = os.listdir(download_dir)
    paths = [os.path.join(download_dir, basename) for basename in files if basename.lower().endswith(('.png', '.jpg'))]
    latest_file = max(paths, key=os.path.getctime)
    
    print(f'Most recent download: {latest_file}')
    
    
    # Muestra la imagen descargada en Jupyter Notebook (si es una imagen)
    from IPython.display import Image as IPImage, display
    if latest_file.endswith('.png') or latest_file.endswith('.jpg'):
        display(IPImage(latest_file))


    # elif latest_file.endswith('.pdf'):
    #     display(IFrame(latest_file, width=600, height=800))

    return


def download_graph( series , start_date , end_date , format= 'png'):
    '''
    Objective: 
        This function scraps series from the BCRP Database and downloads the image in the given format.

    Input: 
        series (str/list) : The code of the series we want to webscrap, i.e: 'PN38705PM'. In case we want to scrap many series, we enter a list with each code 
                            separated by a coma, up to 10 codes, i.e: ['PN38706PM', 'PN38707PM', 'PN38708PM', 'PN38708PM']

        start_date (str)  : The starting date of the series. For daily series it must follow the patter 'yyyy-mm-dd'. For other frequencies it must 
                            follow 'yyyy-mm'. For anual series it can be specified just as 'yyyy'.

        end_date (str)    : The starting date of the series. For daily series it must follow the patter 'yyyy-mm-dd'. For other frequencies it must 
                            follow 'yyyy-mm'. For anual series it can be specified just as 'yyyy'.

        format (str)      : It tells us the format of the download. It can be 'jpg', 'png', 'pdf'. By default it downloads a png picture.
 
    Output:
        It downloads the image in the given format.
    '''
    base     = 'https://estadisticas.bcrp.gob.pe/estadisticas/series/api/'

    if isinstance( series , list):
        string = ''
        for element in series : 
            string += element
            string += '-'
        string =  string[:-1]
        serie  = string

    else:
        serie  =  series
    anio1     = start_date
    anio2     = end_date
    url       = base + serie + '/' + 'html' + '/' + anio1  + '/' + anio2
    options   = Options()
    options.add_argument( "--headless=new" )
    driver    = webdriver.Chrome(options = options)        
    driver.get( url )
    driver.maximize_window()

    driver.find_element(By.XPATH, '//*[@id="btnGrafico"]').click()

    # We go to the next window and download the image in selected format.
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)

    # Depending on the format we choose, the image is downloaded    
    if format   == 'png':
        driver.find_element(By.XPATH, '//*[@id="chart-selector"]/li[2]/img').click()
        time.sleep(4)

    elif format == 'jpg':
        driver.find_element(By.XPATH, '//*[@id="chart-selector"]/li[1]/img').click()
        time.sleep(4)

    elif format == 'pdf':
        driver.find_element(By.XPATH, '//*[@id="chart-selector"]/li[3]/img').click()
        time.sleep(4)

    return

