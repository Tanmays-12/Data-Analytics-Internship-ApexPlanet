# Data Dictionary

| Column Name   | Data Type | Description                                 | Business Relevance                                      |
| ------------- | --------- | ------------------------------------------- | ------------------------------------------------------- |
| Order_ID      | String    | Unique identifier for each order            | Used to uniquely identify and track customer orders     |
| Order_Date    | String    | Date on which the order was placed          | Used for sales trend analysis and time-based reporting  |
| Customer_ID   | String    | Unique identifier assigned to each customer | Enables customer-level analysis and purchase tracking   |
| Customer_Name | String    | Name of the customer                        | Helps identify customers in reports                     |
| Age           | Float     | Customer's age                              | Used for demographic and customer segmentation analysis |
| Gender        | String    | Customer gender                             | Used for demographic insights                           |
| City          | String    | Customer's city                             | Enables region-wise sales analysis                      |
| Product       | String    | Product purchased by the customer           | Used to identify product performance                    |
| Category      | String    | Category to which the product belongs       | Helps analyze sales by product category                 |
| Quantity      | Integer   | Number of units purchased                   | Used to calculate sales volume                          |
| Unit_Price    | Float     | Price of one unit of the product            | Used in revenue calculations                            |
| Total_Sales   | Float     | Total value of the transaction              | Measures revenue generated from each order              |
