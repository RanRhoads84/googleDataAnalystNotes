from google.cloud import bigquery

# Create a client object
client = bigquery.Client()

# Construct a reference to the dataset
dataset_ref = client.dataset('hacker_news', project='bigquery-public-data')

# API request - fetch the dataset
dataset = client.get_dataset(dataset_ref)

# List all the tables in the "hacker_news" dataset
tables = list(client.list_tables(dataset))

# Print names of all the tables in the dataset
for table in tables:
    print(table.table_id)


# Construct a reference tp the "full" table 
table_ref = dataset_ref.table("full")

# API request - fetch the table
table = client.get_table(table_ref)

