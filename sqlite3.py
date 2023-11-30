import sqlite3, spacy

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Example SQLite database connection ()
conn = sqlite3.connect("./db_copy.db")
cursor = conn.cursor()

def get_relevant_data(user_prompt):
    # Tokenize and extract keywords using spaCy
    doc = nlp(user_prompt)
    keywords = [token.text for token in doc if not token.is_stop]
    
    # Mapping keywords to database tables
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
                "table":"users", 
                "column_mapping": {
                    "user":["user_id", "username"],
                }
            },
            {
                "table":"orders", 
                "column_mapping": {
                    "user":["order_id", "product_name", "order_date", "amount"],
                    "orders":["order_id", "product_name", "order_date", "amount"],
                }
            }
        ]
    }

    # Create a list of relevant columns based on keywords
    relevant_columns = set()
    for keyword in keywords:
        if keyword in table_mapping:
            relevant_columns.update(table_mapping[keyword])

            # TODO: one more for loop to go through keywords for column

    # Dynamic SQL Query Generation
    sql_query = f"SELECT {', '.join(relevant_columns)} FROM your_table WHERE ..."

    # Execute the SQL query on the database
    cursor.execute(sql_query)
    results = cursor.fetchall()

    # Process the results (replace with your logic)
    for row in results:
        print(row)

    # Pass the relevant data as context to your model (replace with your model logic)
    model_output = your_model_function(results)

    return model_output

# Example User Prompt
user_prompt = "What is the flight time from New York to Los Angeles?"

# Call the function with the user's prompt
output = get_relevant_data(user_prompt)

# Close the database connection
conn.close()
