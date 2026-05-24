# DiceStats

Statistics based on dice roll

WHAT IS THE PROGRAM?

I have created a program in Python that simulates a 10-sided dice rolling 1000 times​

I have then used this data for real-time statistical analysis​

The program also displays a histogram with all the relevant data​

HISTOGRAM PLOT

I chose an aligned bins histogram plot, as it allows me to treat the data as a numerical distribution​

It also allows me to plot statistics such as sample mean and median onto the graph, unlike bar charts​

Furthermore, the data in this case is discrete, which is suited for this type of histogram

STATISTICAL ANALYSIS

I have computed multiple statistical values from this
data:​

Sample Mean (the average value of the 1000 rolls)​

Experimental Probability (chance of receiving each
number from the 10-sided dice based on the data)​

Sample Variance (average squared distance from the
sample mean)​

Sample Standard Deviation (average distance from the
sample mean in original units of the data)​

Chi-square statistic (measure of how far values deviate
from expected)​

p-value (probability of seeing this unevenness on the
histogram by chance)

MEANING OF STATISTICAL VALUES​

​Sample standard deviation allows you to understand the
distribution of the data and how spread out it is​

Low deviation means values are close together (narrow
histogram), high deviation means values are spread out
(wider histogram)​

Sample variance is the squared version – it is used for
calculations and calculus because it behaves in a simpler
manner ​

Chi-square statistic measures how different the experimental
values are from the theoretical ones​

It is used to test whether these differences are due to
randomness, or due to a biased/unfair dice​

p-value tells us the chance of these differences being due to
randomness (high p-value, very fair dice)​

COMPARISON WITH THEORETICAL VALUES

The experimental values won't perfectly match the theoretical values​

This is due to random sampling variation, which causes small deviations​

However, as the p-value is >0.05, and the valuesare relatively close, the die behaves like a fair uniform distribution​

Chi-square and p-value do not have any theoretical values to compare against as they depend entirely on the sample, not the die’s behavior​

They are test statistics, to see whether the die is fair​
​

​​
