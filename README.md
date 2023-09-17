# Email-Marketing-Campaign-Dashboard
This repository showcases Python scripts used in generating fake data and the rest of the steps taken behind my personal Tableau project - Email Marketing Campaign Dashboard. It is based on the client work I have done. The dashboard is available [here]().

Dashboard - Overview:
![image](https://github.com/Marius321/Email-Marketing-Campaign-Dashboard/assets/117634180/8a35ae91-6ddb-4eb7-a164-04f3006a4bfb)

## STEP 1. Setting up the IDE
I have started by installing Anaconda Navigator onto my local machine and setting up a Spyder IDE with Python 3.9 in order to start generating the scripts. 

## STEP 2. Generating Scripts*
It was then followed by writing the actual Python scripts I have generated three scripts for three operations:

#### Script 1. Data generating script
This script uses faker library to generate fake email data including customer name, email name, sent dates etc. as per below:

![Columns Data](https://github.com/Marius321/Email-Marketing-Campaign-Dashboard/assets/117634180/5edfdca5-7d8e-432a-9462-15c73af81257)

Full code available [here](https://github.com/Marius321/Email-Marketing-Campaign-Dashboard/blob/main/generate_emails.py).

#### Script 2. Filtering script 
The second script takes the output from the first script and filters it down. This was needed, because the first script generates 4 emails per customer, while I wanted differing numbers of emails for different customers, so this code, filters out some of the emails based on percentiles to better mimic real-world data.

Full code available [here](https://github.com/Marius321/Email-Marketing-Campaign-Dashboard/blob/main/filter_emails.py).

#### Script 3. Sankey script
This script transforms the filtered data into the format suitable to build a Sankey Funnel Chart. The format is available in the screenshot below. Script filters the data down to the month of August and to the year 2023, later unioning the results to allow period filterability on the dashboard.

![image](https://github.com/Marius321/Email-Marketing-Campaign-Dashboard/assets/117634180/99f49745-76bf-4b4f-bd80-4adea18406fd)

Full code available [here](https://github.com/Marius321/Email-Marketing-Campaign-Dashboard/blob/main/sankey.py).

*Some of the code was written with the help of Chat GPT to speed up the process. 

## STEP 3. Setting up the Data Model
The data model for this dashboard is relatively simple. It includes two tables with no relationship established between the two of them. One is the sankey dataset, which is used to build the sankey, and the other one is the email metrics dataset that was used to build the rest of the dashboard.

## STEP 4. Building Tableau dashboard
Sankey Funnel was built following the [blog](https://www.flerlagetwins.com/2019/11/sankey-funnel.html) by Ken Flerlage. I have also used [this](https://www.youtube.com/watch?v=NwV6FWAbPAM) YouTube tutorial to build gradient bar charts. The other Tableau functionality and features used are outlined below:
- Parameter and Select Actions
- Filters
- Navigation Buttons
- Gradient images created using Figma
- Custom number formatting to display up/down indicators
- String formatting functions and Regex to format dynamic field values (e.g. currency, percentages, numbers etc.)

## Python Code Snippets
Generating fake data
```
name = faker.name()
account_number = faker.random_number(digits=8)
```
Selecting columns and filtering
```
customers_all_emails_in_2023 = df.groupby('name').filter(lambda group: all('2023' in date for date in group['sent_date']))
df_filtered_2023 = df[df['name'].isin(customers_all_emails_in_2023['name'])]
```
Defining custom functions
```
def filter_email_2(df):
    return df[df['email_name'].str.contains('Email 1|Email 2|Email 3')]
def filter_email_3(df):
    return df[df['email_name'].str.contains('Email 1|Email 2|Email 3|Email 4')]
```
For loops
```
for j in email_sequence:
    if name not in emails_sent:
        emails_sent[name] = [j]
    elif len(emails_sent[name]) < max_emails_per_person and j not in emails_sent[name]:
        emails_sent[name].append(j)
    else:
        continue
```
Merging and unioning data frames
```
merged = pd.merge(grouped_counts, model, on='Link')
df_union = pd.concat([data_2023, data_august], axis=0, ignore_index=True)
```
Pivoting data frames
```
df_pivoted = df.pivot(index='name', columns='email_name', values='email_name')
```
Applying functions to the data
```
num_emails = min(max_emails_per_person, 4)
len(emails_sent[name])
df[df['email_name'].str.contains('Email 2|Email 3')]
```
Changing the data types
```
percentile_index = int(total_customers * percentile) * 4
'sent_date': sent_datetime.strftime('%Y-%m-%d %H:%M:%S')
```
Importing different Python libraries
```
import random
from faker import Faker
import pandas as pd
from datetime import datetime, timedelta
```
Creating columns and assigning values
```
data_2023['Month/Year'] = "Year"
data_august['Month/Year'] = "Month"
```
Renaming columns
```
grouped_counts = grouped_counts.rename(columns={"Email 1": "Step 1", "Email 2": "Step 2", "Email 3": "Step 3", "Email 4": "Step 4"})
```
Reading and writing to Excel files
```
df = pd.read_csv(r'C:\Users\Marius\Desktop\Email Marketing\unfiltered_dataset.csv')
combined_result.to_csv(r'C:\Users\Marius\Desktop\Email Marketing\filtered_dataset.csv', index=False)
```
## Inspiration
The dashboard was inspired by Chimdi Nwosu viz #RWFD NYC Community Service Requests which can be found [here](https://public.tableau.com/app/profile/chimdi.nwosu/viz/RWFD-NYCCommunityServiceRequests/Overview).

## Social Media
📊 [Tableau Public](https://public.tableau.com/app/profile/marius5597)

🐤 [Twitter/X](https://twitter.com/VizMarius)

👨‍💼 [LinkedIn](https://www.linkedin.com/in/mariusnikiforovas/)
