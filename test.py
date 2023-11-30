# logging.debug(f"something {type(something)}: {something}")
import replicate, os, logging, tiktoken
from transformers import AutoTokenizer

import load_db

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.basicConfig(filename='./.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

model = "01-ai/Yi-34B-chat"
sub_model = "914692bbe8a8e2b91a4e44203e70d170c9c5ccc1359b283c84b0ec8d47819a46"

# this was just for testing
def import_db():
    def read_sql_file(file_path):
        with open(file_path, 'r') as sql_file:
            sql_text = sql_file.read()
        return sql_text
    
    def token_counter(prompt):
        tokenizer = AutoTokenizer.from_pretrained(model)
        encoding = tokenizer(prompt, return_tensors="pt")
        token_count = encoding.input_ids.size(1)
        print(f"\n\nToken count: {token_count}\n")
        return token_count

    sql_query = read_sql_file("./sample.sql")

    token_counter(sql_query)
    return sql_query

    
def main():
    prompt = input("What do you want to know about your Database?\n")
    
    data = load_db.get_relevant_data(prompt)
    
    prompt_template = '''
    <|im_start|>system
    You are a Data Scientist that can understand DataBase in-depth. You will be given exported data from MySQL including the relation between the tables.
    Your job is to answer the question precisely and solely based on the data given.
    Following is the mysql exported data.
    ```
    '''+data+'''
    ```
    <|im_end|>
    <|im_start|>user
    {prompt}
    <|im_end|>
    <|im_start|>assistant
    '''

    while True:
        output = replicate.run(
            model.lower()+":"+sub_model.lower(),
            input={
                "top_k": 50,
                "top_p": 0.8,
                "prompt": prompt,
                "temperature": 0.3,
                "max_new_tokens": 1024,
                "prompt_template": prompt_template,
                "repetition_penalty": 1.2
            }
        )

        # Convert the generator to a list
        output_list = list(output)
        response = ""
        for o in output_list: response += o

        print(response, end="\n\n")
main()