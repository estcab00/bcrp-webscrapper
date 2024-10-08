# bcrp-webscrapper
This repository has a module that allows the scrapping of the Peruvian Central of Reserve (BCRP) Statistics Database.

## Structure

The repository contains the following folders:

- `src` : Contains the `.py` files where the functions are defined, specifically under the `bcrp_webscrapper` subdirectory.
- `test` : Includes example usage and tests for the functions.
- `dist` : Contains the distribution packages, such as `.tar.gz` and `.whl` files, for different versions of the project.
- `build` : Holds build-related files, including intermediate files and directories used during the packaging process.

## Getting Started

### Prerequisites

You need to make sure you have installed the following modules.

- Requests
- Unidecode
- Selenium
- Webdriver_manager
- openpyxl

```bash
pip install requests
pip install unidecode
pip install selenium
pip install webdriver_manager
pip install openpyxl
pip install more-itertools
```

### Installation
```bash
pip install bcrp-webscrapper
```

## Functions
The module defines the following main functions:

### `bcrp_search()`

This function provides a basic searcher for the BCRP Database website. We provide the name of the series and the frequency we want and search for the data available. It returns a dataframe with all series that match our input.

### `bcrp_dataframe()`

This function scraps series from the BCRP Database and gives us a dataframe with the series.

### `bcrp_graph()`

This function graphs series from the BCRP Database.

### `download_graph()`

This function scraps series from the BCRP Database and downloads the image in the given format (png, jpg, pdf).

## Usage

- **Example 1**

```python
from bcrp_webscrapper import *

var = "Expectativas"
freq = "Mensual"
print(bcrp.bcrp_search( var , freq))

var2 = "PBI"
print(bcrp.bcrp_search( var2 ))
```

- **Example 2**
```python
from bcrp_webscrapper import *

codes      = ['PD04637PD', 'PD04638PD']
start_date = '2012-03-12'
end_date   = '2022-05-30'
freq       = 'Diario'

bcrp.bcrp_dataframe( codes , start_date , end_date , freq)
```
- **Example 3**
```python
from bcrp_webscrapper import *

codes      = ['PD09919MA', 'PD09920MA']
start_date = '2015'
end_date   = '2022'

bcrp.bcrp_graph( codes , start_date , end_date )
```

For more examples, please refer to the [the test folder](https://github.com/estcab00/bcrp-webscrapper/blob/main/test/test.py).

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

- **Email:** [estcab00@gmail.com](mailto:estcab00@gmail.com)


