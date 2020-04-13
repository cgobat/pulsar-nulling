# pulsar-nulling
Analysis of radio pulsar parameters and their relationships with nulling statistics

`pulsar_diagram.py` is the original Gist that creates a P-Pdot diagram by automatically scraping the [ATNF pulsar catalog](https://www.atnf.csiro.au/people/pulsar/psrcat/):
![pulsarplot.png](https://raw.githubusercontent.com/cgobat/pulsar-nulling/master/pulsarplot.png)

`pulsarstats.csv` was manually parsed by me from the data tables in [Konar and Deka (2019)](https://www.ias.ac.in/article/fulltext/joaa/040/05/0042).

`Nulling.ipynb` contains the bulk of the analysis: it rescrapes the ATNF catalog with some additional paramters, imports the csv data, and cross-references the two to get a complete picture of radio pulsars that exhibit nulling behavior.
