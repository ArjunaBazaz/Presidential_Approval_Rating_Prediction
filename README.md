# Presidential_Approval_Rating_Prediction
Analyzing Presidential Approval Rating based on different time-series factors such as unemployment rate and S&amp;P500 value.

## Software and Platform Section
Language: Python (Jupyter Notebook) <br>
Packages: Pandas, Matplotlib, Scipy <br>
Platform: Windows, Mac <br>

## Directory
Presidential_Approval_Rating_Prediction/ <br>
├── SCRIPTS/ <br>
│   ├── 1_get_stock_data.ipynb <br>
│   ├── 1.5_add_candidate_column <br>
│   ├── 2_preliminary_data_analysis.ipynb <br>
│   ├── 2.5_more_prelim_analysis_joint_approval_ratings.ipynb <br>
│   ├── 3_linear_regression.ipynb <br>
├── DATA/ <br>
│   ├── approval_rating_biden_1.csv <br>
│   ├── approval_rating_bushjr_1_2.csv <br>
│   ├── approval_rating_bushsr_1.csv <br>
│   ├── approval_rating_carter_1.csv <br>
│   ├── approval_rating_clinton_1_2.csv <br>
│   ├── approval_rating_eisenhower_1_2.csv <br>
│   ├── approval_rating_ford_1.csv <br>
│   ├── approval_rating_johnson_1_2.csv <br>
│   ├── approval_rating_kennedy_1.csv <br>
│   ├── approval_rating_nixon_1_2.csv <br>
│   ├── approval_rating_obama_1_2.csv <br>
│   ├── approval_rating_reagan_1_2.csv <br>
│   ├── approval_rating_roosevelt_3_4.csv <br>
│   ├── approval_rating_truman_1.csv <br>
│   ├── approval_rating_trump_1.csv <br>
│   ├── median_household_income.csv <br>
│   ├── median_household_income_daily_change.csv <br>
│   ├── real_GDP_per_capita.csv <br>
│   ├── real_GDP_per_capita_daily_change.csv <br>
│   ├── sp500_historical_data.csv <br>
│   ├── sp500_historical_data_daily_change.csv <br>
│   ├── unemployment_rate.csv <br>
│   ├── approval_rating_biden_1_updated.csv <br>
│   ├── approval_rating_bushjr_1_2_updated.csv <br>
│   ├── approval_rating_bushsr_1_updated.csv <br>
│   ├── approval_rating_carter_1_updated.csv <br>
│   ├── approval_rating_clinton_1_2_updated.csv <br>
│   ├── approval_rating_eisenhower_1_2_updated.csv <br>
│   ├── approval_rating_ford_1_updated.csv <br>
│   ├── approval_rating_johnson_1_2_updated.csv <br>
│   ├── approval_rating_kennedy_1_updated.csv <br>
│   ├── approval_rating_nixon_1_2_updated.csv <br>
│   ├── approval_rating_obama_1_2_updated.csv <br>
│   ├── approval_rating_reagan_1_2_updated.csv <br>
│   ├── approval_rating_roosevelt_3_4_updated.csv <br>
│   ├── approval_rating_truman_1_updated.csv <br>
│   ├── approval_rating_trump_1_updated.csv <br>
│   ├── approval_rating.csv <br>
├── OUTPUT/ <br>
├── LICENSE.md <br>
├── README.md <br>

## Reproduction Instructions

Step 1: Download data from the American Presidency Project. Save as a tsv or csv file.  <br>
Step 2: Download real GDP per capita, unemployement rate, and median household income from the federal reserves' dataset  <br>
Step 3: Run script 1_get_stock_data.ipynb to get the S&P500 historical dataset.  <br>
Step 4: Run 1.5_add_candidate_column to add the candidate column to each dataset.  <br>
NOTE: Steps 1-4 can be skipped by forking the repository and using the existing data files. <br>
Step 5: Run 2_preliminary_data_analysis.ipynb to to get daily change versions of each of the economic datasets. In addition, it will output preliminary data anlysis  <br>
Step 6: Run 2.5_more_prelim_analysis_joint_approval_ratings.ipynb to output graph of candidate approval rating over time  <br>
Step 7: Run 3_linear_regression.ipynb to get outputs of preliminary linear regression model for comparing different variables. <br>
Step 8: Run 4_time_series_analysis.ipynb to get the final time series results and view the outcome. <br>
