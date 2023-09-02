import pandas as pd
pd.options.display.max_columns = None

df = pd.read_csv(r'C:\Users\Marius\Desktop\Email Marketing\filtered_dataset.csv')
model = pd.read_excel(r'C:\Users\Marius\Desktop\Email Marketing\Sankey Template Multi Level.xlsx', sheet_name='Model')

def transform_dataframe(df):
    # Pivot the DataFrame
    df_pivoted = df.pivot(index='name', columns='email_name', values='email_name')
    
    # Rename the columns
    df_pivoted = df_pivoted.rename(columns={
        "Email 1 - Welcome to Wanderlust Adventures": "Email 1",
        "Email 2 - Offers tailored just for you": "Email 2", 
        "Email 3 - Don’t miss out on your next adventures, book now and get 20% off": "Email 3",
        "Email 4 - Thanks for choosing Wanderlust Adventures": "Email 4"
    })
    
    # Apply the "Qualified" or "Not Qualified" labeling
    df_labeled = df_pivoted.applymap(lambda x: "Qualified" if pd.notnull(x) else "Not Qualified")
    
    # Change "Email 1" to blank if labeled as "Not Qualified"
    df_labeled.loc[df_labeled["Email 1"] == "Not Qualified", "Email 1"] = ""
    
    # Change "Email 2", "Email 3", and "Email 4" to blank if "Email 1" is Qualified and they are "Not Qualified"
    qualified_mask = (df_labeled["Email 1"] == "Qualified") & (df_labeled[["Email 2", "Email 3", "Email 4"]] == "Not Qualified").all(axis=1)
    df_labeled.loc[qualified_mask, ["Email 2", "Email 3", "Email 4"]] = ""
    
    # Set "Email 3" to Skiped this Stage if "Email 2" and "Email 4" are Qualified while "Email 3" is "Not Qualified"
    qualified_mask_2 = (df_labeled["Email 2"] == "Qualified") & (df_labeled["Email 4"] == "Qualified") & (df_labeled["Email 3"] == "Not Qualified")
    df_labeled.loc[qualified_mask_2, "Email 3"] = "Skiped stage"
    
    # Set "Email 4" to blank if "Email 2" and "Email 3" are Qualified while "Email 4" is "Not Qualified"
    qualified_mask_3 = (df_labeled["Email 2"] == "Qualified") & (df_labeled["Email 3"] == "Qualified") & (df_labeled["Email 4"] == "Not Qualified")
    df_labeled.loc[qualified_mask_3, "Email 4"] = ""
    
    # Set "Email 2" to "No Response" if "Email 2", "Email 3" and "Email 4" are blank while "Email 1" is "Qualified"
    qualified_mask_4 = (df_labeled["Email 1"] == "Qualified") & (df_labeled["Email 2"] == "") & (df_labeled["Email 3"] == "") & (df_labeled["Email 4"] == "")
    df_labeled.loc[qualified_mask_4, "Email 2"] = "No Response"
    
    # Set "Email 4" to "No Response" if "Email 2" is not No interests while "Email 4" is blank
    qualified_mask_5 = (df_labeled["Email 2"] != "No Response") & (df_labeled["Email 4"] == "")
    df_labeled.loc[qualified_mask_5, "Email 4"] = "No Response"
    
    # Set "Email 3" and "Email 4" to blank if "Email 1", "Email 2" are qualified and "Email 3" and "Email 4" are Not Qualified
    qualified_mask_6 = (df_labeled["Email 2"] == "Qualified") & (df_labeled["Email 1"] == "Qualified") & (df_labeled["Email 3"] == "Not Qualified") & (df_labeled["Email 4"] == "Not Qualified")
    df_labeled.loc[qualified_mask_6, "Email 3"] = ""
    df_labeled.loc[qualified_mask_6, "Email 4"] = ""
    
    # Rename "Qualified" to "New Leads" in "Email 1" at the end
    df_labeled.loc[df_labeled["Email 1"] == "Qualified", "Email 1"] = "New Leads"
    
    # Rename "Qualified" to "Existing Customers" and "Not Qualified" to "Provided Interests" in "Email 2"
    df_labeled.loc[(df_labeled["Email 2"] == "Qualified") & (df_labeled["Email 1"] == ""), "Email 2"] = "Exsisting Customers"
    df_labeled.loc[(df_labeled["Email 2"] == "Qualified") & (df_labeled["Email 1"] != ""), "Email 2"] = "Provided Interests"
    
    # Rename "Qualified" to "Chased with Discount" in "Email 3"
    df_labeled.loc[df_labeled["Email 3"] == "Qualified", "Email 3"] = "Discount"
    
    # Rename "Qualified" to Qualified/booked in "Email 4"
    df_labeled.loc[df_labeled["Email 4"] == "Qualified", "Email 4"] = "Qualified/Booked"
    
    # Add a new column called "Link" with constant value "link"
    df_labeled = df_labeled.assign(Link="link")
    
    email_columns = ["Email 1", "Email 2", "Email 3", "Email 4"]
    grouped_counts = df_labeled.groupby(email_columns + ["Link"]).size().reset_index(name='Size')
    
    grouped_counts = grouped_counts.rename(columns={"Email 1": "Step 1", "Email 2": "Step 2", "Email 3": "Step 3", "Email 4": "Step 4"})
    
    merged = pd.merge(grouped_counts, model, on='Link')
    
    return merged

# Get customer names with all emails sent in 2023
customers_all_emails_in_2023 = df.groupby('name').filter(lambda group: all('2023' in date for date in group['sent_date']))

# Filter original DataFrame based on these customers
df_filtered_2023 = df[df['name'].isin(customers_all_emails_in_2023['name'])]

#Apply the above function to get sankey data for 2023
data_2023 = transform_dataframe(df_filtered_2023)

#Assign a Year value to the Month/Year column
data_2023['Month/Year'] = "Year"

# Get customer names with all emails sent in August
customers_all_emails_in_august = df.groupby('name').filter(lambda group: all('2023-08' in date for date in group['sent_date']))

# Filter original DataFrame based on these customers
df_filtered_august = df[df['name'].isin(customers_all_emails_in_august['name'])]

#Apply the above function to get sankey data for august
data_august = transform_dataframe(df_filtered_august)

#Assign a Year value to the Month/Year column
data_august['Month/Year'] = "Month"

#Union the sankey data for 2023 and for August
df_union = pd.concat([data_2023, data_august], axis=0, ignore_index=True)

print(df_union)

df_union.to_csv(r'C:\Users\Marius\Desktop\Email Marketing\sankey.csv', index=False)