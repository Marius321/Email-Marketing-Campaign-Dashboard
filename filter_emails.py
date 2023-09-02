import pandas as pd

# Example functions to filter DataFrame based on the values in email_name column
def filter_email_1(df):
    
    """
    Filters the DataFrame so email_name column only contains "Email 1".
    Args:
        df (DataFrame): Input DataFrame (with email_name column containing Email 1, Email 2, Email 3 and Email 4)
    Returns:
        DataFrame: Filtered DataFrame (with email_name column only containing Email 1)
    """        
    return df[df['email_name'].str.contains('Email 1')]

#other filter functions works the same just produce differently filtered output

def filter_email_2(df):
    return df[df['email_name'].str.contains('Email 1|Email 2|Email 3')]

def filter_email_3(df):
    return df[df['email_name'].str.contains('Email 1|Email 2|Email 3|Email 4')]

def filter_email_4(df):
    return df[df['email_name'].str.contains('Email 1|Email 2|Email 4')]

def filter_email_5(df):
    return df[df['email_name'].str.contains('Email 2|Email 3')]

def filter_email_6(df):
    return df[df['email_name'].str.contains('Email 2|Email 4')]

def filter_email_7(df):
    return df[df['email_name'].str.contains('Email 2|Email 3|Email 4')]

# Load the CSV file into a DataFrame
df = pd.read_csv(r'C:\Users\Marius\Desktop\Email Marketing\unfiltered_dataset.csv')

# Calculate the row indices for specific percentiles based on total number of customers
total_customers = len(df) // 4  # Each customer gets 4 emails

# Mapping of percentiles to corresponding filter functions
percentile_mapping = {
    0.20: filter_email_1,
    0.45: filter_email_2,
    0.50: filter_email_3,
    0.60: filter_email_4,
    0.80: filter_email_5,
    0.90: filter_email_6,
    1.00: filter_email_7
}

# Initialize an empty DataFrame to store the combined results
combined_result = pd.DataFrame()

# Iterate through the defined percentiles and apply corresponding filters
for percentile, filter_func in percentile_mapping.items():
    percentile_index = int(total_customers * percentile) * 4
    
    if percentile == min(percentile_mapping.keys()):
        subset = df.iloc[:percentile_index]
    else:
        previous_percentile = sorted([p for p in percentile_mapping.keys() if p < percentile])[-1]
        previous_percentile_index = int(total_customers * previous_percentile) * 4
        subset = df.iloc[previous_percentile_index:percentile_index]
    
    filtered_subset = filter_func(subset)  # Apply the filter function
    
    # Concatenate the filtered subset to the combined_result DataFrame
    combined_result = pd.concat([combined_result, filtered_subset])

# Print the combined filtered result
combined_result.to_csv(r'C:\Users\Marius\Desktop\Email Marketing\filtered_dataset.csv', index=False)
