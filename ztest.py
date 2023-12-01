import sqlite3, spacy

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Function to read SQL commands from a file
def read_sql_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Create an in-memory SQLite database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Read and execute SQL commands from the file
sql_commands = read_sql_file('sample.sql')
cursor.executescript(sql_commands)

def extract_keywords(question):
    doc = nlp(question)
    return [token.text.lower() for token in doc if not token.is_stop and token.is_alpha]

def construct_query(keywords):
    # Example: Map keywords to potential columns
    table_mapping = {
        "user": [
            {
                "table":"users", 
                "column_mapping": {
                    "user":["user_id", "username", "email"]
                }
            },
            {
                "table":"orders", 
                "column_mapping": {
                    "user":["order_id", "user_id"],
                    "orders":["order_id", "user_id", "product_name", "amount"],
                }
            }
        ],
        "customer": [
            {
                "table":"users", 
                "column_mapping": {
                    "user":["user_id", "username", "email"]
                }
            },
            {
                "table":"orders",
                "column_mapping": {
                    "user":["order_id", "user_id"],
                    "orders":["order_id", "user_id", "product_name", "amount", "order_date"]
                }
            }
        ],
        "orders": [
            {
                "table":"orders", 
                "column_mapping": {
                    "user":["order_id", "product_name", "order_date", "amount", "user_id"],
                    "orders":["order_id", "product_name", "order_date", "amount"]
                }
            }            
        ],
        "products": [
            {
                "table":"orders", 
                "column_mapping": {
                    "user":["order_id", "product_name", "order_date", "amount"],
                    "orders":["order_id", "product_name", "order_date", "amount"],
                }
            }
        ]
    }

    keyword_to_column = {
        'laptops': 'product_name',
        'sold': 'order_date'  # Assuming 'sold' relates to 'order_date' in your schema
    }
    table_selections = []
    column_selections = []
    for keyword in keywords:
        if keyword in table_mapping:
            for i in table_mapping[keyword]:
                table_selections.append(f"{i['table']} LIKE '%{keyword}%'")

    if not table_selections:
        return None

    # Constructing a basic SQL query (customize based on your schema)
    queries = []
    for i in table_selections:
        queries.append(f"SELECT COUNT(*) FROM orders")
    return queries

def get_relevant_data(question):
    keywords = extract_keywords(question)
    print(keywords)
    query = construct_query(keywords)
    print(query)

    if query:
        cursor.execute(query)
        result = cursor.fetchone()
        return result
    else:
        return "No relevant data found."

# Example usage
question = "How many laptops have we sold?"
result = get_relevant_data(question)
print(result)

# Close the database connection
conn.close()