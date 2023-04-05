import numpy as np #module for data annalysis
import pandas  as pd #module for data annalysis
import seaborn as sns # module for plotting 
import  matplotlib.pyplot  as plt # for charts/graphs 
# %matplotlib inline

fifa = pd.read_csv(r"WorldCups.csv")
fifa.tail(10)
fifa.head(10)
print(fifa.ndim)
fifa.size
fifa.info()
fifa.isnull().values.any()
fifa.describe()
sns.displot(fifa['MatchesPlayed'])
plt.show()
fifa['Winner'].value_counts(ascending = False)
m1 = fifa['QualifiedTeams'].mean()  # mean
print(m1)
m2 = fifa['QualifiedTeams'].median()  # median
print(m2)
m3 = fifa['QualifiedTeams'].mode()[0]  # mode
print(m3)
fifa[fifa['QualifiedTeams']>m1]['Country']
GS_median = np.median(fifa['GoalsScored'])
print(GS_median)
QT_median = np.median(fifa['MatchesPlayed'])
print(QT_median)
fifa[fifa['GoalsScored']==fifa['GoalsScored'].min()]['Country']
sns.pairplot(fifa[['GoalsScored', 'QualifiedTeams', 'MatchesPlayed']])
plt.show()
sns.scatterplot(x= fifa['Year'], y= fifa['Country'])
plt.show()
plt.figure(figsize=(8,6))

sns.countplot(x=fifa['Winner'])

plt.title('How many times Country played matches between 1930 to 2014')

plt.xlabel('Country')

plt.ylabel('Frequency')

plt.show()

fifa = fifa.drop(['Third'], axis=1) 
fifa.head()

corr_matrix = fifa.corr()

corr_matrix
