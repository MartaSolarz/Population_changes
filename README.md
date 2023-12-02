# Informatics, Systems and Programming - project

## 1. Idea
**Visualization of population changes in European Union countries on an interactive map in the years 1960-2050.**

The project involves creating an interactive data visualization application that illustrates the changes in population across selected countries from the year 1960 to 2050. This project primarily focuses on using data visualization techniques and tools to present complex data in a more accessible and engaging manner. The main components of this project could include the following:

**1. Data Acquisition:**

Collecting population data for different countries from the year 1960 to 2050: https://databank.worldbank.org/source/population-estimates-and-projections/preview/on. 

**2. Data Processing and Analysis:**

Processing and analyzing the acquired data to extract relevant information. This step may involve data cleaning and computation of population changes over the specified period for each country.

**3. Interactive Map Creation:**

Utilizing appropriate data visualization Folium library, to create an interactive map that displays the changes in population for each country. The map should be interactive, allowing users to explore different years.

**4. Time Series Visualization:**

Implementing a user-friendly interface that enables users to select specific years or range of years to observe the changes in population dynamically. 

**5. Visualization presentation in the web application:**

Providing the option to display an interactive map on the Internet, which can be used locally on your computer (localhost).

By implementing these key components, the project aims to provide users with an engaging and informative way to visualize and comprehend the changes in the population of countries worldwide over nearly six decades. This project not only highlights the power of data visualization in conveying complex information effectively but also enables users to gain valuable insights into global population dynamics.

## 2. How to run the project?

#### Using bash:

```bash
voila main.ipynb --no-browser --port=8080 --VoilaConfiguration.enable_nbextensions=True
```

#### Using Docker:

```bash
docker build -t population_map .
````

```bash
docker run -p 8080:8080 population_map
```