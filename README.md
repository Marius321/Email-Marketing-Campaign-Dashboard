# Email-Marketing-Campaign-Dashboard
This repository showcases the Python fake data generating scrips used in my personal Tableau project - Email Marketing Campaign Dashboard based on the client work I have previously done. I have used Spyder IDE through Anaconda and Python 3.9.

![image](https://github.com/Marius321/Email-Marketing-Campaign-Dashboard/assets/117634180/aff9e96d-0ce1-4c0e-b5bc-3c8ed79742cb)
![Dashboard Page 2](https://github.com/Marius321/Email-Marketing-Campaign-Dashboard/assets/117634180/9b9e5231-4ad2-4d5d-b853-f8c838bedc15)

The dashboard is available [here]().

The dashboard was inspired by Chimdi Nwosu viz #RWFD NYC Community Service Requests which can be found [here](https://public.tableau.com/app/profile/chimdi.nwosu/viz/RWFD-NYCCommunityServiceRequests/Overview). Below I outlined the steps taken to create my dashboard.

## STEP 1. Setting up the IDE
First I have installed Anaconda Navigator onto my local machine and setted up a Spyder IDE with Python 3.9 in order to start generating the scripts. 

## STEP 2. Generating Scripts
There are three scripts that performs different operations:
#### Script 1. Data generating script
This script uses faker library to generate fake email data inluding customer name, email name, sent dates etc. 
![Columns Data](https://github.com/Marius321/Email-Marketing-Campaign-Dashboard/assets/117634180/5edfdca5-7d8e-432a-9462-15c73af81257)
#### Script 2. Filtering script
This script filters the output from the previous script based on certain percentiles so number of emails received would differ for different customers.
#### Script 3. Sankey script
This script transforms the data from the previous script in the format needed to build a Sankey Funnel Chart, as per the screenshot below. The final dataset has data transformed for the month of August and then for the whole year of 2023 to allow filterability on dashboard.
![image](https://github.com/Marius321/Email-Marketing-Campaign-Dashboard/assets/117634180/99f49745-76bf-4b4f-bd80-4adea18406fd)


## Shout outs and inpiration from:
