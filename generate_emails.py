import random
from faker import Faker
import pandas as pd
from datetime import datetime, timedelta

# Set the maximum number of columns to display when printing DataFrames
pd.options.display.max_columns = None

# Seed the random number generator for Faker
Faker.seed(3245)
faker = Faker()

def generate_customer_data(num_customers=65000, max_emails_per_person=4):
    customers = [] # List to store generated customer data
    emails_sent = {} # Dictionary to track sent emails for each customer

    for i in range(num_customers):
        name = faker.name()
        account_number = faker.random_number(digits=8)
        
        # Define time range for email interactions
        start_time = datetime.now().replace(year=datetime.now().year-4, month=1, day=1, hour=6, minute=0, second=0, microsecond=0)
        end_time = datetime.now().replace(hour=1, minute=0, second=0, microsecond=0) + timedelta(days=1)
        
        # Generate a random email interaction time
        email_datetime = faker.date_time_between_dates(datetime_start=start_time, datetime_end=end_time)
        
        # Limit the number of emails to 4
        num_emails = min(max_emails_per_person, 4)
        
        # Creating email sequence list
        email_sequence = list(range(1, num_emails + 1))
        
        for j in email_sequence:
            if name not in emails_sent:
                emails_sent[name] = [j]
            elif len(emails_sent[name]) < max_emails_per_person and j not in emails_sent[name]:
                emails_sent[name].append(j)
            else:
                continue
            
            sent_datetime = email_datetime + timedelta(hours=j-1)
            
            if start_time <= sent_datetime <= end_time:
                bounce_probability = random.random()
                
                if bounce_probability <= 0.015:
                    bounce_datetime = sent_datetime + timedelta(minutes=random.randint(0, 1))
                    bounced = True
                    open_datetime = None
                    click_datetime = None
                    transaction_amount = None
                else:
                    bounce_datetime = None
                    bounced = False
                    
                    # Probabilities for opening an email
                    open_probabilities = {
                        1: 0.87,
                        2: 0.89,
                        3: 0.79,
                        4: 0.77
                    }
                    open_probability = random.random()
                    
                    if open_probability <= open_probabilities[j]:
                        open_datetime = sent_datetime + timedelta(minutes=random.randint(1, 59))
                        
                        # Probabilities for clicking on an email
                        click_probabilities = {
                            1: 0.272,
                            2: 0.325,
                            3: 0.11,
                            4: 0.24
                        }
                        click_probability = random.random()
                        
                        if click_probability <= click_probabilities[j]:
                            click_datetime = open_datetime + timedelta(minutes=random.randint(1, 59))
                            
                            # Probabilities for conversion after clicking
                            conversion_probabilities = {
                                1: 0.079,
                                2: 0.129,
                                3: 0.129,
                                4: 0.037
                            }
                            conversion_probability = random.random()
                            
                            if conversion_probability <= conversion_probabilities[j]:
                                transaction_amount = round(random.uniform(600, 1400), 2)
                                transaction_date = click_datetime + timedelta(days=random.randint(1, 30))  # Random transaction date within 30 days after the click
                            else:
                                transaction_date = None
                                transaction_amount = None
                        else:
                            click_datetime = None
                            transaction_date = None
                            transaction_amount = None
                    else:
                        open_datetime = None
                        click_datetime = None
                        transaction_date = None
                        transaction_amount = None
                
                # Email names corresponding to email numbers
                email_name = {
                    1: "Email 1 - Welcome to Wanderlust Adventures",
                    2: "Email 2 - Offers tailored just for you",
                    3: "Email 3 - Don’t miss out on your next adventures, book now and get 20% off",
                    4: "Email 4 - Thanks for choosing Wanderlust Adventures"
                }
                
                # Append customer data to the list
                customers.append({
                    'name': name,
                    'account_number': account_number,
                    'email_name': email_name[j],  # Use 'j' directly
                    'sent_date': sent_datetime.strftime('%Y-%m-%d %H:%M:%S'),
                    'open_date': open_datetime.strftime('%Y-%m-%d %H:%M:%S') if open_datetime else None,
                    'click_date': click_datetime.strftime('%Y-%m-%d %H:%M:%S') if click_datetime else None,
                    'bounce_date': bounce_datetime.strftime('%Y-%m-%d %H:%M:%S') if bounce_datetime else None,
                    'transaction_date': transaction_date.strftime('%Y-%m-%d %H:%M:%S') if transaction_date else None,
                    'transaction_amount': transaction_amount
                })
    
    return customers

# Generate customer data
customer_data = generate_customer_data()

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(customer_data)

# Save DataFrame to a CSV file
df.to_csv(r'C:\Users\Marius\Desktop\Email Marketing\unfiltered_dataset.csv', index=True, index_label='index')
