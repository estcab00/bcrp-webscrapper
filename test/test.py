## Testing =======================================================================

#pip install bcrp_webscrapper==1.0.6

import time
from bcrp_webscrapper import bcrp
print(dir(bcrp))

## bcrp_search =======================================================================

df = bcrp.bcrp_search('PBI')
df.head()

df = bcrp.bcrp_search('Inflación', 'Mensual')
df.head()

df = bcrp.bcrp_search('Expectativas', 'Mensual')
df.head()

## testing time execution of bcrp_search ===================================================================

st = time.time()
bcrp.bcrp_search('Inflación')
et = time.time()
elapsed_time = et - st
print('Execution time of bcrp_search:', elapsed_time, 'seconds')

st = time.time()
bcrp.bcrp_search('Inflación', 'Mensual')
et = time.time()
elapsed_time = et - st
print('Execution time of bcrp_search:', elapsed_time, 'seconds')

st = time.time()
bcrp.bcrp_search('PBI')
et = time.time()
elapsed_time = et - st
print('Execution time of bcrp_search:', elapsed_time, 'seconds')

st = time.time()
bcrp.bcrp_search('PBI', 'Trimestral')
et = time.time()
elapsed_time = et - st
print('Execution time of bcrp_search:', elapsed_time, 'seconds')

st = time.time()
bcrp.bcrp_search('Expectativas', 'Mensual')
et = time.time()
elapsed_time = et - st
print('Execution time of bcrp_search:', elapsed_time, 'seconds')

## bcrp_scrapper =======================================================================

df = bcrp.bcrp_scrapper('PD04637PD', '2012-03-12' , '2022-05-30' , 'Diario' )
df.head()

df = bcrp.bcrp_scrapper( ['PD04637PD', 'PD04638PD'] , '2012-03-12' , '2022-05-30' , 'Diario' )
df.head()

df = bcrp.bcrp_scrapper(['PN39030BQ', 'PD37942PQ'], '2020-03', '2022-06', 'Trimestral')
df.head()

df = bcrp.bcrp_scrapper(['PD09919MA', 'PD09920MA', 'PD09921MA', 'PD09922MA', 'PD09923MA', 'PD09924MA', 'PD09925MA', 'PD09926MA', 'PD09932MA', 'PD09933MA'], '2009-01', '2023-01', 'Anual')
df.head()

## testing time execution of bcrp_scrapper =================================================================

st = time.time()
bcrp.bcrp_scrapper(['PN01288PM', 'PN01218PM', 'PN01219PM'], '2009-06', '2020-03', 'Mensual' ).head()
et = time.time()
elapsed_time = et - st
print('Execution time of bcrp_scrapper:', elapsed_time, 'seconds')

st = time.time()
bcrp.bcrp_scrapper(['PN39030BQ', 'PD37942PQ'], '2020-03', '2022-06', 'Trimestral').head()
et = time.time()
elapsed_time = et - st
print('Execution time of bcrp_scrapper:', elapsed_time, 'seconds')

st = time.time()
bcrp.bcrp_scrapper(['PD09919MA', 'PD09920MA', 'PD09921MA', 'PD09922MA', 'PD09923MA', 'PD09924MA', 'PD09925MA', 'PD09926MA', 'PD09932MA', 'PD09933MA'], '2009-01', '2023-01', 'Anual').head()
et = time.time()
elapsed_time = et - st
print('Execution time of bcrp_scrapper:', elapsed_time, 'seconds')

## bcrp_dataframe =======================================================================

series     = ['PN01271PM', 'PN01280PM', 'PN01282PM', 'PN01278PM', 'PN09817PM','PN09816PM', 'PN01276PM', 'PN01313PM', 'PN01314PM',  
             'PN01315PM', 'PN09818PM','PN01286PM']
start_date = '2003-01'
end_date   = '2023-12'
freq       = 'Mensual'

df = bcrp.bcrp_dataframe( series , start_date , end_date , freq )

df.head() 

series     = ['PN02528AQ', 'PN02539AQ', 'PN02529AQ', 'PN02533AQ', 'PN02530AQ', 'PN02534AQ']
start_date = '2003-03'
end_date   = '2024-06'
freq       = 'Trimestral'

df = bcrp.bcrp_dataframe( series , start_date , end_date , freq )

df.head() 

## testing time execution of bcrp_dataframe =================================================================

st = time.time()
bcrp.bcrp_dataframe( series , start_date , end_date , freq )
et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')

## bcrp_graph =======================================================================

bcrp.bcrp_graph( ['PD04637PD', 'PD04638PD'] , '2020-03-01' , '2020-06-01')

bcrp.bcrp_graph( ['PD09919MA', 'PD09920MA'] , '2015' , '2022' , format= 'jpg')