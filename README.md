# bcrp-webscrapper
This repository has a module that allows the scrapping of the Peruvian Central of Reserve (BCRP) Statistics Database. 

## Functions
The module defines the following main functions:

### ```bcrp_search()``` 

This function provides a basic searcher for the BCRP Database website. We provide the name of the series and the frequency we want and search for the data available. Ir returns a dataframe with all series that match our input.

### ```bcrp_scrapper()```

This function scraps series from the BCRP Database and gives us a dataframe with the series.

### ```bcrp_graph()```

This function graphs series from the BCRP Database.

### ```downlodad_graph()```

This function scraps series from the BCRP Database and downloads the image in the given format (png, jpg, pdf).

## Structure
The repository contains the following folders:
-  ```scr``` : we find the ```.py``` file where the functions are defined.
- ```test``` : we find some examples of the functions being used.

