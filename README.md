# Email-Marketing-Campaign-Dashboard
This repository showcases the Python fake data generating scripts used in my personal Tableau project - Email Marketing Campaign Dashboard based on the client work I have previously done.

![image](https://github.com/Marius321/Email-Marketing-Campaign-Dashboard/assets/117634180/aff9e96d-0ce1-4c0e-b5bc-3c8ed79742cb)
![Dashboard Page 2](https://github.com/Marius321/Email-Marketing-Campaign-Dashboard/assets/117634180/9b9e5231-4ad2-4d5d-b853-f8c838bedc15)

The dashboard is available [here]().

The dashboard was inspired by Chimdi Nwosu viz #RWFD NYC Community Service Requests which can be found [here](https://public.tableau.com/app/profile/chimdi.nwosu/viz/RWFD-NYCCommunityServiceRequests/Overview). Below I outlined the steps taken to create this dashboard.

## STEP 1. Setting up the IDE
First I have installed Anaconda Navigator onto my local machine and setted up a Spyder IDE with Python 3.9 in order to start generating the scripts. 

## STEP 2. Generating Scripts
Data is generated by three different scripts:
#### Script 1. Data generating script
This script uses faker library to generate fake email data inluding customer name, email name, sent dates etc as per below:

![Columns Data](https://github.com/Marius321/Email-Marketing-Campaign-Dashboard/assets/117634180/5edfdca5-7d8e-432a-9462-15c73af81257)

#### Script 2. Filtering script
The 1st script generates data with all customers receiving 4 emails, this script filters some of the emails out for certain groups of customers based on specified percentiles, so it mimics real world data better where different customers receive different number of emails.

#### Script 3. Sankey script
This script transforms the data from the previous script in the format needed to build a Sankey Funnel Chart. Format available in the screenshot below. Script filters the data down to the month of August and to the year of 2023, later unioning the results to allow period filterability on dashboard.

![image](https://github.com/Marius321/Email-Marketing-Campaign-Dashboard/assets/117634180/99f49745-76bf-4b4f-bd80-4adea18406fd)

*Some of the scripts were written with the help of Chat GPT in order to speed up the process of generating scripts. 

## STEP 3. Setting up the Data Model
The datamodel for this dashbaord is realtively simple. It includes to tables with no real realtionship established between two of them. One is the sankey dataset, that feeds the sankey, and the other one is email metrics dataset that feeds the rest.

## STEP 4. Building Tableau dashboard
Sankey Funnel was build following the [blog](https://www.flerlagetwins.com/2019/11/sankey-funnel.html) by Ken Flerlage. I have also used [this](https://www.youtube.com/watch?v=NwV6FWAbPAM) Youtube tutorial to build gradient bar charts. The other Tableau functionality and features used.
- Parameter and Select Actions
- Navigation Buttons
- Gradient images created using Figma
- Custom number formatting to dsiplay up/down indicators

## Python Code Snippets
Full scripts: 
1. [Email Data Generating Script](https://github.com/Marius321/Email-Marketing-Campaign-Dashboard/blob/main/generate_emails.py)
2. [Filtering Script](https://github.com/Marius321/Email-Marketing-Campaign-Dashboard/blob/main/filter_emails.py)
3. [Sankey Script](https://github.com/Marius321/Email-Marketing-Campaign-Dashboard/blob/main/sankey.py)

## Shout outs and inpiration from:
Ken Flerlage

## Social Media
[Tableau Public](https://public.tableau.com/app/profile/marius5597)
[Twitter](https://twitter.com/VizMarius)
[LinkedIn](https://www.linkedin.com/in/mariusnikiforovas/)
