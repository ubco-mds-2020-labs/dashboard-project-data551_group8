[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=371704&assignment_repo_type=GroupAssignmentRepo)

## Motivation and Purpose 
**The Dashboard Designers:** Okanagan Wine Enthusiasts (Graduate students at the University of British Columbia)
**The Audience:** Those interested in knowing what physicochemical properties fundamentally make or break a high quality wine (vinho verde) from Northern Portugal

Wine is a multi billion dollar global industry. With 36 billion bottles of wine produced each year [1](https://www.winespectator.com/articles/how-many-bottles-of-wine-are-there-in-the-world-46410), producers are constantly looking for ways to outperform the competition and create the best wines they can. Portugal in particular is second in the world for per-capita wine consumption [2](https://www.nationmaster.com/nmx/ranking/wine-consumption-per-capita) and eleventh for wine production, creating over 600,000 litres per year [3](https://en.wikipedia.org/wiki/List_of_wine-producing_regions). Physicochemical components are fundamental to a wine’s quality and those who understand this aspect of wine will have a greater edge into crafting an enjoyable and profitable product. 

Wine quality evaluation is the main part of the certification process to improve wine making. It is generally assessed by physicochemical tests and sensory analysis. The relationship between physicochemical structure and subjective quality is complex. No individual component can be used to accurately predict a wine’s quality, and interactions are as important as the components themselves. For example, perhaps higher alcohol content only improves a wine within a certain range of sulphate content, and wines outside this range are made worse by higher alcohol content. Trained wine tasting experts are able to reliably score wine on a scale ranging from 0 (very bad) to 10 (excellent), and those scores can be used to determine how these physicochemical properties affect quality. 

Our interactive dashboard will allow users to explore a number of physicochemical variables and how they interact to determine the subjective quality of a wine. Our visualizations will allow users to test and discover for themselves these relationships. Wine producers, wine enthusiasts, and curious individuals can all make use of this dashboard.


## Description of the Data
The dashboard is built on the famous wine quality data set from Cortez et al., 2009. Data was collected from Portuguese Vinho Verde wines which originate in the northwest regions of Portugal. Vinho Verde has a medium alcohol content, and is particularly sought for its freshness in summer months. Each wine sample was evaluated by at least three sensory assessors (using blind tastes) who graded the wine from 0 (worst) to 10 (best). The final quality score is given by the median of these evaluations.

Our dataset consists of the physiochemical composition and sensory test results for 4898 white and 1599 red wine samples which were collected from May 2004 to February 2007. Each wine sample contains 12 variables that provide the acidity properties (fixed acidity, volatile acidity, citric acid, pH), sulphides contents (free sulfur dioxide, total sulfur dioxide, sulphates), density related properties (residual sugar, alcohol, density), and salt content (chlorides). It also contains quality as the response variable. In order to improve classification analyses, we define a new variable, quality_factor. Any wine with a quality score less than six is classified as “below average”, a score of 6 is “average”, and above 6 is “above average”.

## Research Questions
- Which physicochemical factors contribute most to excellent Vinho Verde wine quality, which lead to poor wine quality, and which do not have much in either direction?
- How do these variables interact with each other? What relationships exist between predictors? Which variables have strong covariance with each other?
- How do physicochemical properties differentially affect red and white wines?

## Usage Scenario
Alice is a winemaker in BC’s Okanagan Valley. She would like to create a new summer wine and hopes to take inspiration from the Vinho Verde wines, known for their refreshing qualities. Alice seeks our dashboard to better understand what wine attributes she should focus on to provide a tasting experience comparable to the very best Vinho Verde wines. However, there are some physicochemical properties she has little control over due to the soils and grape species available to her. Due to the above average alkalinity of Okanagan soil, she knows that her wines will typically be less acidic than true Vinho Verde wines, and the altitude means the chloride content will be lower as well. She wants to try to optimize the variables she has control over to make the best wine possible. She looks to our dashboard to see how Vinho Verde wines with higher pH and lower chloride content tend to fare. Looking at the interactive scatterplots, she sees that wines which have values within her possible ranges for these variables tend to be of very poor quality when they are also high in residual sugar, but less sweet wines are of good quality. She then consults the histograms and sees that there are not very many wines available that have these properties, so she knows that she will not have much direct competition should she go forward with this design. A few years later, she released this wine to broad critical acclaim and millions in profit.

## App Sketch and Description:
[sketch](a png)

**Description:**

The Vinho Verde wine Dashboard has three tabs; Interactive Graphics, Explore the Dataset, and Machine Learning. 

The Interactive Graphics page contains a number of graphis to explore the effects of physicochemical properties on wine quality. On the left hand side users are able to select the wine type (eg. red wine, white wine) as well as the physicochemical features of interest. Some possible visualizations are as follows:
1. Variable density distributions for each quality category comparing red vs white.
2. Stacked distribution of variable counts in each quality factor.
3. Scatterplot with interactive slide bar for the quality label and dropdown for property to plot against. This plot will also allow users to select a specific area and generate a bar plot demonstrating the quality distribution in this range.
4. Scatterplot to plot any two physicochemical properties against each other.

The Explore the Dataset tab will focus on descriptive data analysis, allowing users to generate summary statistics for groups of their choice. 

Lastly, the Machine learning tab will focus on modelling and machine learning techniques. This section will be primitive in the early stage of the project.
