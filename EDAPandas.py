#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Pandas is a Python library that provides extensive means for data analysis. 
Data scientists often work with data stored in table formats like .csv, .tsv, or .xlsx.
Pandas makes it very convenient to load, process, and analyze such tabular data using SQL-like queries. 
In conjunction with Matplotlib and Seaborn,
Pandas provides a wide range of opportunities for visual analysis of tabular data.


# In[ ]:


The main data structures in Pandas are implemented with Series and DataFrame classes.
The former is a one-dimensional indexed array of some fixed data type. 
The latter is a two-dimensional data structure - a table - where each column contains data of the same type.
You can see it as a dictionary of Series instances. DataFrames are great for representing real data: 
    rows correspond to instances (examples, observations, etc.), 
    and columns correspond to features of these instances.


# In[2]:


import numpy as np
import pandas as pd


# In[ ]:


We'll demonstrate the main methods in action by analyzing a dataset on the churn rate of telecom operator clients.
Let's read the data (using read_csv), and take a look at the first 5 lines using the head method:


# In[ ]:


The data set includes information about:

Customers who left within the last month – the column is called Churn
Services that each customer has signed up for – phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies
Customer account information – how long they’ve been a customer, contract, payment method, paperless billing, monthly charges, and total charges
Demographic info about customers – gender, age range, and if they have partners and dependents


# In[11]:


df = pd.read_csv("telecom_churn.csv")
df.head()


# In[ ]:


Let’s have a look at data dimensionality, feature names, and feature types.


# In[12]:


print(df.shape)


# In[13]:


print(df.columns)


# In[ ]:


We can use the info() method to output some general information about the dataframe:


# In[14]:


print(df.info())


# In[ ]:


bool, int64, float64 and object are the data types of our features.
We see that one feature is logical (bool), 3 features are of type object, and 16 features are numeric.
With this same method, we can easily see if there are any missing values. Here, there are none because each column contains 
3333 observations, the same number of rows we saw before with shape.

We can change the column type with the astype method. Let's apply this method to the Churn feature to convert it into int64:


# In[16]:


df["Churn"] = df["Churn"].astype("int64")


# In[15]:


df.describe()


# In[ ]:


In order to see statistics on non-numerical features,
one has to explicitly indicate data types of interest in the include parameter.


# In[17]:


df.describe(include=["object", "bool"])


# In[ ]:


For categorical (type object) and boolean (type bool) features we can use the value_counts method. 
Let's have a look at the distribution of Churn:


# In[18]:


df["Churn"].value_counts()


# In[ ]:


2850 users out of 3333 are loyal;
their Churn value is 0. To calculate fractions, pass normalize=True to the value_counts function.


# In[19]:


df["Churn"].value_counts(normalize=True)


# In[20]:


df.sort_values(by="Total day charge", ascending=False).head() # sorting data frame by a single column


# In[21]:


df.sort_values(by=["Churn", "Total day charge"], ascending=[True, False]).head() # sorting data frame by a multiple columns


# 
# # Indexing and retrieving data

# In[ ]:


A DataFrame can be indexed in a few different ways.

To get a single column, you can use a DataFrame['Name'] construction.
get_ipython().set_next_input("Let's use this to answer a question about that column alone: what is the proportion of churned users in our dataframe");get_ipython().run_line_magic('pinfo', 'dataframe')


# In[22]:


df["Churn"].mean()


# In[ ]:


14.5% is actually quite bad for a company; such a churn rate can make the company go bankrupt.


# In[ ]:


Boolean indexing with one column is also very convenient. The syntax is df[P(df['Name'])], where P is 
some logical condition that is checked for each element of the Name column.
The result of such indexing is the DataFrame consisting only of rows that satisfy the P condition on the Name column


# In[ ]:


# let us answer some specific questions
What are average values of numerical features for churned users


# In[23]:


df[df["Churn"] == 1].mean()


# In[ ]:


get_ipython().set_next_input('How much time (on average) do churned users spend on the phone during daytime');get_ipython().run_line_magic('pinfo', 'daytime')


# In[24]:


df[df["Churn"] == 1]["Total day minutes"].mean()


# In[ ]:


get_ipython().set_next_input('What is the maximum length of international calls among loyal users (Churn == 0) who do not have an international plan');get_ipython().run_line_magic('pinfo', 'plan')


# In[25]:


df[(df["Churn"] == 0) & (df["International plan"] == "No")]["Total intl minutes"].max()


# In[ ]:


DataFrames can be indexed by column name (label) or row name (index) or by the serial number of a row.
The loc method is used for indexing by name, while iloc() is used for indexing by number.

In the first case below, we say "give us the values of the rows with index from 0 to 5 (inclusive) and columns labeled 
from State to Area code (inclusive)". In the second case, we say "give us the values of the first five rows in the first
three columns"
(as in a typical Python slice: the maximal value is not included).


# In[26]:


df.loc[0:5, "State":"Area code"]


# In[27]:


df.iloc[0:5, 0:3]


# In[ ]:


If we need the first or the last line of the data frame, we can use the df[:1] or df[-1:] construct:


# In[28]:


df[-1:]


# In[ ]:


# Apply family of functions


# In[ ]:


Applying Functions to Cells, Columns and Rows
To apply functions to each column, use apply():


# In[29]:


df.apply(np.max)


# In[ ]:


he apply method can also be used to apply a function to each row. To do this, specify axis=1.
Lambda functions are very convenient in such scenarios.
For example, if we need to select all states starting with W, we can do it like this:


# In[30]:


df[df["State"].apply(lambda state: state[0] == "W")].head()


# In[ ]:


The map method can be used to replace values 
in a column by passing a dictionary of the form {old_value: new_value} as its argument:


# In[31]:


d = {"No": False, "Yes": True}
df["International plan"] = df["International plan"].map(d)
df.head()


# In[ ]:


The same thing can be done with the replace method:


# In[32]:


df = df.replace({"Voice mail plan": d})
df.head()


# # Grouping
# In general, grouping data in Pandas works as follows:

# In[ ]:


df.groupby(by=grouping_columns)[columns_to_show].function()


# In[ ]:


First, the groupby method divides the grouping_columns by their values. They become a new index in the resulting dataframe.
Then, columns of interest are selected (columns_to_show). If columns_to_show is not included, all non groupby clauses
will be included.
Finally, one or several functions are applied to the obtained groups per selected columns.
Here is an example where we group the data according to the values of the Churn variable and display statistics of three 
columns in each group


# In[33]:


columns_to_show = ["Total day minutes", "Total eve minutes", "Total night minutes"]

df.groupby(["Churn"])[columns_to_show].describe(percentiles=[])


# In[ ]:


let’s do the same thing, but slightly differently by passing a list of functions to agg():


# In[34]:


columns_to_show = ["Total day minutes", "Total eve minutes", "Total night minutes"]

df.groupby(["Churn"])[columns_to_show].agg([np.mean, np.std, np.min, np.max])


# # Summary tables
# Suppose we want to see how the observations in our sample are distributed in the context of two variables -
# Churn and International plan.
# To do so, we can build a contingency table using the crosstab method:

# In[35]:


pd.crosstab(df["Churn"], df["International plan"])


# In[36]:


pd.crosstab(df["Churn"], df["Voice mail plan"], normalize=True)


# In[37]:


We can see that most of the users are loyal and do not use additional services (International Plan/Voice mail).


# 
# # DataFrame transformations

# In[ ]:


Like many other things in Pandas, adding columns to a DataFrame is doable in many ways. 

For example, if we want to calculate the total number of calls for all users, 
let's create the total_calls Series and paste it into the DataFrame:


# In[38]:


total_calls = (
    df["Total day calls"]
    + df["Total eve calls"]
    + df["Total night calls"]
    + df["Total intl calls"]
)
df.insert(loc=len(df.columns), column="Total calls", value=total_calls)
# loc parameter is the number of columns after which to insert the Series object
# we set it to len(df.columns) to paste it at the very end of the dataframe
df.head()


# In[ ]:


To delete columns or rows, use the drop method, passing the required indexes and the axis parameter 
(1 if you delete columns, and nothing or 0 if you delete rows). The inplace argument tells whether to change
the original DataFrame. With inplace=False, the drop method doesn't change the existing DataFrame 
and returns a new one with dropped rows or columns. With inplace=True, it alters the DataFrame.


# In[40]:


# get rid of just created columns
df.drop(["Total calls"], axis=1, inplace=True)
# and here’s how you can delete rows
df.drop([1, 2]).head()


# # Contingency Tables

# In[ ]:


Let's see how churn rate is related to the International plan feature.
We'll do this using a crosstab contingency table and also through visual analysis with Seaborn 
(however, visual analysis will be covered more thoroughly in the next article).


# In[41]:


pd.crosstab(df["Churn"], df["International plan"], margins=True)


# In[42]:


# some imports to set up plotting
import matplotlib.pyplot as plt
# pip install seaborn
import seaborn as sns

# Graphics in retina format are more sharp and legible
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")


# In[43]:


sns.countplot(x="International plan", hue="Churn", data=df)


# In[ ]:


We see that, with International Plan, the churn rate is much higher, which is an interesting observation! 
Perhaps large and poorly controlled expenses with international calls are very conflict-prone and lead to dissatisfaction 
among the telecom operator's customers.

Next, let's look at another important feature – Customer service calls. Let's also make a summary table and a picture.


# In[44]:


pd.crosstab(df["Churn"], df["Customer service calls"], margins=True)


# In[45]:


sns.countplot(x="Customer service calls", hue="Churn", data=df)


# In[ ]:


Although it's not so obvious from the summary table, it's easy to see from the above plot that
the churn rate increases sharply from 4 customer service calls and above.

Now let's add a binary feature to our DataFrame – Customer service calls > 3. And once again, 
let's see how it relates to churn.


# In[46]:


df["Many_service_calls"] = (df["Customer service calls"] > 3).astype("int")

pd.crosstab(df["Many_service_calls"], df["Churn"], margins=True)


# In[47]:


sns.countplot(x="Many_service_calls", hue="Churn", data=df)


# In[ ]:


Let's construct another contingency table that relates Churn with both International plan and 
freshly created Many_service_calls.


# In[48]:


pd.crosstab(df["Many_service_calls"] & df["International plan"], df["Churn"])


# In[ ]:


Therefore, predicting that a customer is not loyal (Churn=1) in the case when the number of calls to the service center
is greater than 3 and the International Plan is added (and predicting Churn=0 otherwise), we might expect an accuracy of
85.8% (we are mistaken only 464 + 9 times). This number, 85.8%, that we got through this very simple reasoning serves as a 
good starting point (baseline) for the 
further machine learning models that we will build.


# In[ ]:


As we move on in this course, recall that, before the advent of machine learning, the data analysis process looked something like this. 
Let's recap what we've covered:


# In[ ]:


1. The share of loyal clients in the sample is 85.5%. The most naive model that always predicts a "loyal customer" 
on such data will guess right in about 85.5% of all cases. That is, the proportion of correct answers (accuracy) of 
subsequent models should be no less than this number, 
and will hopefully be significantly higher;


# In[ ]:


2. With the help of a simple forecast that can be expressed by the following formula: 
    "International plan = True & Customer Service calls > 3 => Churn = 1, else Churn = 0", 
    we can expect a guessing rate of 85.8%, which is just above 85.5%. Subsequently, we'll talk about decision trees 
    and figure out how to find such rules automatically based only on the input data;


# In[ ]:


3. We got these two baselines without applying machine learning, and they'll serve as the starting point for our 
subsequent models. If it turns out that with enormous effort,
we increase the share of correct answers by 0.5% per se, then possibly we are doing something wrong, and it 
suffices to confine ourselves to a simple model with two conditions;


# In[ ]:


4. Before training complex models, it is recommended to manipulate the data a bit, make some plots, 
and check simple assumptions. Moreover, in business applications of machine learning, 
they usually start with simple solutions and then experiment with more complex ones.

