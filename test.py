import replicate

while True:
    output = replicate.run(
    "01-ai/yi-34b-chat:914692bbe8a8e2b91a4e44203e70d170c9c5ccc1359b283c84b0ec8d47819a46",
    input={
        "top_k": 50,
        "top_p": 0.8,
        "prompt": input(),
        "temperature": 0.3,
        "max_new_tokens": 1024,
        "prompt_template": "<|im_start|>system\nYou are a helpful assistant<|im_end|>\n<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n",
        "repetition_penalty": 1.2
    }
    )

    # Convert the generator to a list
    output_list = list(output)

    # Print the results
    for o in output_list:
        print(o, end="")
    print()