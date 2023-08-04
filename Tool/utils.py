import os
import json
import time
from typing import Any, Dict, List
import openai

def write_to_file(file_name: str, data: str) -> None:
    """
    Function to write a string to a file. If the file already exists, a timestamp is appended to the filename
    to prevent overwriting. The function will automatically create a directory if it doesn't exist.
    
    :param file_name: The name of the file to write to
    :param data: The data to write to the file
    :return: None
    """
    
    # Check if directory exists and if not, create it
    default_directory_name = 'data/text_input'
    if not os.path.exists(default_directory_name):
        os.makedirs(default_directory_name)

    # Create the full file path
    full_file_name = os.path.join(default_directory_name, file_name)
    base, extension = os.path.splitext(full_file_name)
    new_file_name = f"{base}_{int(time.time())}{extension}"

    # Write data to the file
    try:
        with open(new_file_name, 'w') as f:
            f.write(data)
        print(f"Data successfully written to {new_file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_from_file(file_name: str) -> str:
    """
    Function to read data from a file. The function will read the file from the directory 
    where the write_to_file function writes its data.
    
    :param file_name: The name of the file to read from
    :return: The data read from the file as a string
    """
    # Define the default directory name
    default_directory_name = 'data/text_input'
    
    # Create the full file path
    full_file_name = os.path.join(default_directory_name, file_name)

    # Read data from the file
    try:
        with open(full_file_name, 'r') as f:
            data = f.read()
        print(f"Data successfully read from {full_file_name}")
        return data
    except Exception as e:
        print(f"An error occurred: {e}")

def append_json_to_file(model_name: str, json_object: Dict[str, Any]) -> None:
    """
    Function to append a JSON object to a file. The function loads the existing data, appends the new object, 
    and writes all the data back to the file. The function will automatically create a directory if it doesn't exist.

    :param model_name: The model name, used to categorize the data. Must be one of the following: ['GPT-3.5', 'GPT-4'].
    :param json_object: The JSON object to append to the file.
    :return: None
    """

    # Check the model name is valid
    valid_models = ['GPT-3.5', 'GPT-4']
    if model_name not in valid_models:
        raise ValueError(f"'{model_name}' is not a valid argument. Choose from {valid_models}.")
    
    # Check if directory exists and if not, create it
    default_directory_name = os.path.join('data', 'LLM_output')
    if not os.path.exists(default_directory_name):
        os.makedirs(default_directory_name)
    
    # Create the full file path
    file_name = model_name + '.json'
    file_path = os.path.join(default_directory_name, file_name)

    data = []

    # If file exists, load the existing data
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)

    # Append the new JSON object
    data.append(json_object)

    # Write the updated data back to the file
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def read_json_from_file(model_name: str) -> List[Dict[str, Any]]:
    """
    Function to read JSON data from a file. The function will read the file from the directory 
    where the append_json_to_file function writes its data.
    
    :param model_name: The model name, used to locate the data. Must be one of the following: ['GPT-3.5', 'GPT-4'].
    :return: The data read from the file as a list of JSON objects (Python dictionaries).
    """
    # Check the model name is valid
    valid_models = ['GPT-3.5', 'GPT-4']
    if model_name not in valid_models:
        raise ValueError(f"'{model_name}' is not a valid argument. Choose from {valid_models}.")

    # Define the default directory name
    default_directory_name = os.path.join('data', 'LLM_output')
    
    # Create the full file path
    file_name = model_name + '.json'
    full_file_name = os.path.join(default_directory_name, file_name)

    # Read JSON data from the file
    try:
        with open(full_file_name, 'r') as f:
            data = json.load(f)
        print(f"Data successfully read from {full_file_name}")
        return data
    except Exception as e:
        print(f"An error occurred: {e}")

def is_valid_json(s: str) -> bool:
    """
    Function to check if a string is a valid JSON object.
    
    :param s: The string to check
    :return: True if the string is valid JSON, False otherwise
    """
    try:
        json.loads(s)
        return True
    except json.JSONDecodeError:
        return False

def is_valid_openai_api_key(api_key):
    openai.api_key = api_key
    try:
        # Attempt to list the available engines
        openai.Engine.list()
        return True
    except openai.error.OpenAIError as e:
        # Handle specific error types as needed
        print(f"{str(e)}")
        return False