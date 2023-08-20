import jsonlines

# jsonl input and output paths
jsonl_input_paths = ["OPL-QA.jsonl", "OPL-Language.jsonl", "OPL-Examples.jsonl"]
jsonl_output_path = "train.jsonl"

# Open the output JSONL file
with open(jsonl_output_path, "w") as output_file:
    json_writer = jsonlines.Writer(output_file)

    for jsonl_input_path in jsonl_input_paths:
        with open(jsonl_input_path, "r") as input_file:
            json_reader = jsonlines.Reader(input_file)

            for entry in json_reader:
                try:
                    # Combine prompt and completion into the desired format
                    formatted_text = f"<s>[INST] {entry['prompt']} [/INST] {entry['completion']} </s>"

                    # Write the formatted text as a JSONL line
                    json_writer.write({"text": formatted_text})
                except Exception as e:
                    print(f"Error parsing JSON in {jsonl_input_path}:", entry, e)
