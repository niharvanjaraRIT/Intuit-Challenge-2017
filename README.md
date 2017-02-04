# Instructions

The main folder Intuit Challenge (2017) contains 5 folders which are stated below as follows.

**“py”** which consists of 3 python executables (.py)

* **data_mining.py** - This file transforms the data and writes it into a file Reduced-Data.csv
  which is used by feature_extraction.py

* **feature_extraction.py** - This file uses Reduced-Data.csv as its input and extracts features.
  It returns the final result in the form of Final-Data.csv
  
* **user_correlations.py** - This file uses Reduced-Data.csv as its input to generate a plot and the 
  correlation between users. The correlation matrix is in the form of User-Correlations.csv
  **NOTE: the User-Correlations.csv is a plain file and the result is converted into a xlsx for visualization
  the code does not generate the color gradients for the xlsx file.**

the files above should be executed in the top-down order as results from prior executions are used. Hence first
execute data_mining.py then feature_extraction.py and then user_correlation.py


**“phases”** folder consists of .csv and .xlsx which are intermediate results which can be viewed.
There are four files which are as follows
	
* Unique-Vendors.csv
* Transformed-Data.csv
* Merged-Data.csv
* Correlations -Features.xlsx
* Reduced-Data.csv 
  
**“results”** folder which contains final results has two files

* Final-Data.csv
* User-Correlations.xlsx   

**“images”** folder contains plots and visualized tables


**"data"** folder consists of all the 100 .csv files provided by intuit.



**_Please check all the files are contained in  every folder_** before moving forward

# Requirements 

Sofware Requirements
Python 3.5.2 or greater Python 3.0 should also work besides that a number of libraries are
required to be installed in order for the code to run such as numpy1.11.1, scipy0.18.1, pandas0.18.1, matplotlib, scikit-learn0.17.1
and seaborn0.7.1 (used for visualization)

[https://pypi.python.org/pypi/numpy/1.11.1](https://pypi.python.org/pypi/numpy/1.11.1) (Numpy)

[https://pypi.python.org/pypi/scipy](https://pypi.python.org/pypi/scipy) (Scipy)

[https://pypi.python.org/pypi/pandas/0.18.1/](https://pypi.python.org/pypi/pandas/0.18.1/)  (Pandas)

[https://pypi.python.org/pypi/matplotlib](https://pypi.python.org/pypi/matplotlib)	(Matplotlib)

[http://scikit-learn.org/0.17/install.html](ttp://scikit-learn.org/0.17/install.html)  (Scikit-Learn)

[https://pypi.python.org/pypi/seaborn/](https://pypi.python.org/pypi/seaborn/)  (Seaborn)

Seaborn is used for visualization.

# Execution

* To execute the files set up the python(3.0 >) interpreter with the following modules working.
* Set up the project and copy files  **data_mining.py**  , **feature_extraction.py** and **user_correlations.py** 
  into your workspace. 
* Copy the **"data"** folder into your workspace. The folder contains 100 (.csv) files
* Change the path in all of the .py files so that they are able to access the .csv files. Comments are added in the .py
  files to show where path changes should be made.
* Run the .py files in the following order data_mining.py , feature_extraction.py then user_correlations.py

**_Note: data_mining.py takes some amount of time._**


# Methodology

As described in the problem statement the goal of this problem is to find relevant features in the data in order to describe any user based on their transactional data.

To get an intuitive understanding of the data a couple of files (.csv) of random users was opened in Microsoft Excel and explored. Visually the data looked clean. For deeper understanding python was used to explore data after exploration ETL was performed on the data as described below.  

The files were read into Pandas Dataframe and the objects of the frame were stored in a list. Exploratory and Statistical analysis were performed on the Dataframes inorder to find relevant features and to check discrepancy in the data. The data was then transformed in order to serve the goal. 

Features which provided very little information of the user were dropped and not included in the new table. Feature Extraction was performed on the new table and new discrete features of the users were extrapolated. For example, if someone is interested into Art and 

Music this new feature is encoded as either ‘Yes’ or ‘No’. The final new table consists of 100 rows and 25 Columns (excluding Auth_id). Every row describes an instance of the user and every column describes the feature/attribute of the user.
After transforming the data, the compatibility of the users was calculated and a heatmap plot was generated in order to better understand the compatibility of the users. For the compatibility only thr

# Analysis and Results 

No missing values were found in any of the user transaction files and the values contained in each attribute are of a single type. The data is found to be clean and consistent but there are still semantic errors in the tables for example the value of date are not in correct range (eg. 12/32/2014).

Distinct values for each feature for all users gave some vital information for example it showed that all people lived in California (“CA”).  As Location does not contain any other values other than “CA” we can safely remove this feature as this feature imparts very little information to differentiate users from each other. 

The number of unique “auth_ids” found were 100 which corroborates the fact that there are 100 users. 640 different days were found in the period of two years when the users made the purchases. 100 unique vendors were found. Date was dropped from the dataframes as there were too many days and grouping users based on date did not give much information besides the time periods of purchases made. 

To identify lifestyles of users the only attribute valuable in this scenario is “Vendor” and the associated “Amount” spent on each vendor. Hence the tables were grouped based on the distinct vendors. Once grouped based on vendor sum of the amounts were for each distinct vendor, giving the total amount of money spent on each vendor for a period of two years. 

Hence now the tables were transformed such that it consisted of one row (unique user) and the columns now represented the 100 vendors. Hence there were now 100 tables of dimensions 1 x 100. Values in the table where users did not purchase the product were filled with 0. The 100 transformed tables of size 1x100 were merged to create a new table of size 100 x 100 where every row is now a unique user and every column is a feature. Even though the size of the dataset is reduced and merged to one table there still are too many features which still makes it difficult to differentiate users efficiently. 

A method to reduce the number of features in this problem is to club features which are highly correlated into a single feature. Hence correlation matrix was calculated between every pair of vendors and vendors having positive correlation greater than 0.7 were merged into a single category.

A small sample of the correlation matrix of the features is shown  below:
 
![alt text](https://github.com/niharvanjaraRIT/Intuit-Challenge-2017/blob/master/Intuit%20Challenge%20(2017)/images/correlated_features.png)

As shown above green shows high  positive correlation whereas red shows negative correlation. All pairs which showed high correlation were merged. We can see above that books and atheletic equipments share a slight negative correlation. where it is obvious that any feature is correlated with itself hence the value is 1.

Each category consists of those vendors which have an inter-correlation of at least 0.7, for each category some of the features are listed here because of the long list. You can view all the categories and their sub-categories by running the code. The partial categories are shown and described below.

**Category 1 (Fitness/Sports)**	

People into fitness and sports belong into this category. They show similar expenditure in products related to sports. Few vendors belonging to this category are shown below.
		
* GNC
* Dick's Sporting Goods
* Athletic Apparel
* Total Gym Fees
* NBA Ticket – Lakers

**Category 2 (Geek)**

This category consists of people who are avid book readers, watch sci-fi movies and love to play games and high on caffeine. Hence they spend a lot of amount on such products hence the category is rightly named geek/nerd. (No offense) 

* Mary's Book Store
* DVD - Star Trek
* Video Game - PlayStation
* Coffee
* Science Museum
* Amazon Order - Mathematics Book

**Category 3 (Artist)**

The Artist spends a lot of money on music, arts and craft. That’s all there is in this category. Some examples are shown below. 

* Music Lessons - Piano
* Guitar Center
* Ashley's Craft Store
* Painting Course Fees
* Amazon Order - Paint Canvas


**Category 4 (Unpunctual)**

Users belonging in this category never pay the bill on time. They are usually late in paying almost all the payments. Hence they have to pay the late fee penalty.examples shown below.

* Credit Card Overdraft Fee
* Water & Sewer - Late Payment Penalty
* Bank Fee - Negative Balance
* Housing Rent - Late Fee
* Time Warne Cable - Late Payment Fee


**Category 5 (Party Person)**

People in this category love to party and hangout and socialize with other people. Hence they spend a lot of amount on clubbing, bowling, movies and concerts. Some examples shown below.

* Owl Night Club
* Rodriguez's Bar and Grill
* Bowling
* Concert Ticket
* Movie Ticket



**Category 6 (Home Alone/ Elderly)**

Users of this category either like staying home or are too old to go out and have fun. Don’t know which of these it is but they definitely like ordering wine, food, watch TV. They might also own a cat/dog (Pet Person). Some examples are mentioned below.

* Podcast Subscription
* Wine Delivery
* Food Delivery - Uber Eats
* On Demand TV
* Pet Supply - Cat Food

The above categories were found due to correlations in the correlation matrix. But even after merging these categories into the 6 categories there still were many vendors which were not correlated. There were still 50 categories remaining after the transformation.

To reduce more features. Features were looked manually and clubbed based on intuition. For example, there were 9 vendors related to transport and travel. All these were clubbed into one as they shared similar amounts of expenditure for each user. Similarly, other categories like housing, groceries, student loans, utilities were created and vendors sharing similar cost and types were merged into the same category. This reduced the features to just 15. Where each feature is a category consisting of net expenditure/savings for the 2-year period. To see which features helped differentiate users, variance of each feature was calculated and features with variance almost 0 were dropped as they did not vary much internally which did help to achieve the purpose of differentiating users. Before calculating the variance l2 normalization is performed in order to control the range of the variance. Housing, travel and restaurants were dropped as there was almost no variance. It can be concluded that these are common expenses that every person endures and are roughly the same for every user hence can be excluded.

Some new features were also then extracted in order to answer questions inferred from the table. 5 features are created which are described as follows. The feature values were encoded as “YES” or “NO”

Hobbies (Fitness/Sports) – is the person interested into fitness and health
Hobbies (Art/Music) – is the person interested in art and music
Hobbies (Books/Gaming) is the person interested in books, gaming and science.
Hobbies (Socialize) – does the person like to mingle with people
Likes Indoors – does the person like to stay indoors
Parent – is the user a parent
Divorcee – is the user a divorcee
Student – is the user a student 
Has credit card – does the user own/use a credit card
Unpunctual – does the user pay late
Income Strata – Does the user belong to high income, medium income, low income encoded as “HIGH”,” MEDIUM”,” LOW”
Free utilities – Does he have to pay for the utilities.

The final table consists of all these attributes giving us 100 rows (users) and 25 columns (features) excluding user_id ( Auth_id )

# Bonus
For the bonus to find the how compatible the users are we can create a correlation matrix between every pair of users. The correlation matrix is a 100 x 100 matrix. The values of the matrix range from -1 to 1 for this problem negative values are rounded to zero. Hence the final values in the matrix are from 0 to 1 where the closer the value to 1 the more similarities the users emulate.

The correlation matrix between users is plotted below.

![alt text](https://github.com/niharvanjaraRIT/Intuit-Challenge-2017/blob/master/Intuit%20Challenge%20(2017)/images/correlated_users.png)


