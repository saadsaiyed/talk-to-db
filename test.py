import replicate, os, logging


def import_db():
    database_file_name = "./db.mysql"
    if os.path.exists(database_file_name):
        if os.path.getsize(database_file_name) > 0:
            with open(database_file_name) as database:
                current_data = database

data = ""
prompt_template = '''
<|im_start|>system
You are a Data Scientist that can understand DataBase in-depth. You will be given exported data from MySQL including the relation between the tables.
Your job is to answer the question precisely and solely based on the data given.
Following is the mysql exported data.
```mysql
'''+data+'''```<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant
'''

while True:
    output = replicate.run(
    "01-ai/yi-34b-chat:914692bbe8a8e2b91a4e44203e70d170c9c5ccc1359b283c84b0ec8d47819a46",
    input={
        "top_k": 50,
        "top_p": 0.8,
        "prompt": input(),
        "temperature": 0.3,
        "max_new_tokens": 1024,
        "prompt_template": prompt_template,
        "repetition_penalty": 1.2
    }
    )

    # Convert the generator to a list
    output_list = list(output)

    # Print the results
    for o in output_list:
        print(o, end="")
    print()