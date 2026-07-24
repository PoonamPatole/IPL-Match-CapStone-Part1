1. Loaded matches.csv CSV file's Shape is (1095, 20)
2. Total Data columns (total 20 columns)
3. Missing Value Columns are :-
city,
player_Of_match,
winner,
result_margin,
target_runs,
target_overs,
method
4. Drop Column = method. because it has so many null values.and it contain no useful information.
5. Categorical columns imputed with mode: city, player_of_match, winner
6. Numeric columns imputed with median: result_margin, target_runs, target_overs
7. categorial columns are fiiled with mode(the most frquent value) because median or mean is not as much sutaible for text data.
8. numeric columns with less than 10% missing values, so missing values were filled using the median, which is robust to outliers and better represents the typical value than the mean.
9. No Duplicate rows are there.
10. Outlier Detection Method: Used the Interquartile Range (IQR) method.
    Lower Bound = Q1 − 1.5 × IQR
    Upper Bound = Q3 + 1.5 × IQR
11. We choose Cap because we loose match records if we remove the duplicate rows. For Soprts dataset all records are important.

1. Now i have deliveries.csv file. 
2. Its shape is (260920, 17)
3. All columns have correct data types.
4. These are missing values columns:-
    extras_type
    player_dismissed
    dismissal_kind
    fielder
5. So they are related with ball and wickets thats why we do not remove or drop any cloumns and do changes any of them. We keep as it is.
6. Outlier Detection (IQR Method)
The best numeric columns to check are:
    batsman_runs
    total_runs

1. MySQL Database is created and tables were loaded in that database.

1. ALl SQL queries is Performed. SELECT, GROUPBY, ORDERBY, HAVING, BETWEEN
2. After that we Visualse all dataset in different types of Charts. Like.. Bar, Histogram, Scatter_Plot, Line and GroupBy Line chart.

Libraries used....
pandas
numpy
matplotlib
mysql-connector-python
SQLAlchemy
PyMySQL
python-dotenv