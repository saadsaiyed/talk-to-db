import sqlite3
import spacy

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
    keyword_to_column = {
        'laptops': 'product_name',
        'sold': 'order_date'  # Assuming 'sold' relates to 'order_date' in your schema
    }

    conditions = []
    for keyword in keywords:
        if keyword in keyword_to_column:
            conditions.append(f"{keyword_to_column[keyword]} LIKE '%{keyword}%'")

    if not conditions:
        return None

    # Constructing a basic SQL query (customize based on your schema)
    sql_query = f"SELECT COUNT(*) FROM orders WHERE {' AND '.join(conditions)}"
    return sql_query

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
