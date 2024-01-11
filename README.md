# bcrp-webscrapper
This repository has a module that allows the scrapping of the Peruvian Central of Reserve (BCRP) Statistics Database. The module defines three main functions:

```bcrp_search()```: This function provides a basic searcher for the BCRP Database website. We provide the name of the series and the frequency we want
    and search for the data available. Ir returns a dataframe with all series that match our input.

```bcrp_scrapper()```: This function scraps series from the BCRP Database and gives us a dataframe with the series.

```downlodad_graph()```: This function scraps series from the BCRP Database and downloads the image in the given format (png, jpg, pdf).

Under the modules folder we will find the bcrp_webscrapper.py file. Under the test folder we will find some examples of the functions being used.

