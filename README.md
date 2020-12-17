# Quantified-Self
The Quantified Self project takes data collected on myself over the course of a semester, and uses it in a number of data science tasks. The data consists of two CSV files: screen_time.csv and health_data.csv. In the Jupyter Notebooks, the data is cleaned and aggregated, then put into new csv files (revised_screen_time.csv and revised_health.csv). THe main body of the project is broken into two Jupyter notebooks, each of which carry out different tasks.

## AggregationAndHypoTesting.ipynb
This portion of the project is dedicated to loading and cleaning the data, then performing exploratory data analysis. This is the first part of the project, where visualizations and hypothesis testing are used to determine what attribute should be classified in the second portion of the project, and what attributes will be most helpful in the classification process.

## Classification.ipynb
The second portion of the project is dedicated to the development and adjustment of classifiers to predict the schedule type of an instance given health and screen time data. The data is loaded from the revised files (from part 1 of the project). Then, the data is prepped for classification, and the two data frames are merged into a single data frame. From there, various kNN and decision tree classifiers are used and adjusted to best represent the data, until the best possible accuracy for the classifier is achieved.

## utils.py
The utility file utils.py contains functions used throughout the project that better off modularized than integrated into the notebook. This is mainly directed at the visualizations conducted in AggregationAndHypoTesting.ipynb, allowing charts to be constructed with a single line of code. This is mainly to help me keep from cluttering up the notebooks and making errors.
