import sqlite3, spacy

nlp = spacy.load("en_core_web_sm")

def get_relevant_data(user_prompt):
    # Tokenize and extract keywords using spaCy
    doc = nlp(user_prompt)
    keywords = [token.text for token in doc if not token.is_stop]
    
    # TODO @ibrahim: Check if the keywords are accurate and add if necessary
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
                "table":"orders", 
                "column_mapping": {
                    "user":["order_id", "product_name", "order_date", "amount"],
                    "orders":["order_id", "product_name", "order_date", "amount"],
                }
            }
        ]
    }
    
    # Create a list of relevant columns based on keywords
    for keyword in keywords:
        print(keyword)
        # if keyword in table_mapping:
        #     # Instead of directly adding columns to the relevant_columns set, create a temporary set for each keyword and merge it with the main set
        #     temp_relevant_columns = set()
        #     for table_entry in table_mapping[keyword]:
        #         temp_relevant_columns.update(table_entry["column_mapping"].values())
        #     relevant_columns.update(temp_relevant_columns)


            # TODO @ibrahim: one more for loop to go through keywords for column

            # # Dynamic SQL Query Generation
            # sql_query = f"SELECT {', '.join(relevant_columns)} FROM your_table WHERE ..."

            # # Execute the SQL query on the database
            # cursor.execute(sql_query)
            # results = cursor.fetchall()
    
    # # Process the results (replace with your logic)
    # for row in results:
    #     print(row)

    # relevant_data_for_model = []

    # for row in results:
    #     # Extracting relevant data from the results
    #     relevant_data_for_model.append({
    #         'user_id': row['user_id'],
    #         'username': row['username'],
    #         'email': row['email'],
    #         'order_id': row['order_id'],
    #         'product_name': row['product_name'],
    #         'order_date': row['order_date'],
    #         'amount': row['amount']
    #     })


    # # @ibrahim: I will be expecting results to have most relevant data to be fed to model function

    # # TODO @sishui: Create the function and its logic
    # # Pass the relevant data as context to your model (replace with your model logic)
    # model_output = your_model_function(results)

    return None

# Example User Prompt
user_prompt = "how many orders we have?"

# Call the function with the user's prompt
output = get_relevant_data(user_prompt)
