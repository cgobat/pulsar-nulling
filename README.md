# Pulsar nulling
Statistical and timing analysis of radio pulsar parameters and their relationships with the nulling phenomenon by looking at data from numerous places (dynamically where possible) and from numerous angles.

`Nulling.ipynb` contains the bulk of the analysis: arguably the most notable feature of this code is that it pulls and consolidates data from a multitude of sources, including the [ATNF pulsar catalog](https://www.atnf.csiro.au/people/pulsar/psrcat/), data tables in [Konar and Deka (2019)](https://www.ias.ac.in/article/fulltext/joaa/040/05/0042), [EPTA's EPN database](http://www.epta.eu.org/epndb/), and the [Jodrell Bank Center for Astrophysics' glitch catalogue](http://www.jb.man.ac.uk/pulsar/glitches.html).
The script makes all of this data available in an extensible, versatile format for comprehensive analysis. For example, it reads the ATNF catalog to grab some parameters, imports the nulling table csv data, and cross-references the two to get a complete picture of radio pulsars that exhibit nulling behavior. Any number of other variables can be compared by bringing in these other datasets.

`pulsarstats.csv` was manually parsed by me from the data tables in [Konar and Deka (2019)](https://www.ias.ac.in/article/fulltext/joaa/040/05/0042).

`pulsar_diagram.py` is the original Gist that creates a P-Pdot diagram by automatically scraping the [ATNF pulsar catalog](https://www.atnf.csiro.au/people/pulsar/psrcat/):
![pulsarplot.png](https://raw.githubusercontent.com/cgobat/pulsar-nulling/master/pulsarplot.png)
