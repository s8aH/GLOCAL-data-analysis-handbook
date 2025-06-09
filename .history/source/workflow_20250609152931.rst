Data Analysis Workflow
======================

Step 1: Exploratory Data Analysis (EDA)
---------------------------------------
- Show summary statistics for your data (e.g., mean, min, median, max, percentiles, etc.) to understand the overall distribution.
- Plot distributions for each column and list the unique categories in categorical columns.
- This helps you spot missing or unusual data early, so you can quickly decide if you need to switch datasets or merge with other datasets to fill in missing information.

Step 2: Data Cleaning
---------------------
- Rename columns for clarity and drop any columns that won’t be useful for analysis.
- Format/convert data: e.g., ensure numbers are integers/floats and dates are in a consistent format.
- Handle missing data: fill in, impute, or drop missing values if they’re below a chosen threshold (e.g., less than 3% missing).
- Check for duplicated rows or inconsistent formats and fix them as needed.

Step 3: Feature Engineering
---------------------------
- Sometimes a single column contains too much information packed together—for example, a value like "$50, North Glengarry, Township, Ontario." You can split this into separate columns (e.g., price, city, municipality, province), which makes it much easier to analyze and visualize specific patterns in the data

Step 4: Data Visualization
--------------------------
- Use various plot types to highlight trends and patterns in your data—choose the ones that are most interpretable for your audience.
- You can display multiple plots in the same frame (like line and bar), use side-by-side plots for comparison, or create stacked bar charts to show multiple trends together.

Step 5: Data Analysis
---------------------
- Summarize the most important or interesting findings from your visualizations and tables.
- Clearly highlight insights that could influence decisions or guide further analysis.
