from typing import Any, List, Dict, Tuple, Union
import json
import openai
from Tool.utils import write_to_file, append_json_to_file, is_valid_json
from Tool.prompt import ds_prompt, se_prompt, general_prompt

def llm_completion(model_name: str, role_name: str, user_message: str) -> Tuple[str, Dict[str, int]]:
    """
    Generates a language model completion for a given model, role, and user message.

    :param model_name: Name of the model to use, must be one of ['GPT-3.5', 'GPT-4'].
    :param role_name: Role for the conversation, must be one of ['Data relevant', 'Software Engineer', 'General'].
    :param user_message: The user's input message for the conversation(A job description in our case).
    :return: A tuple containing the content response from the model and a dictionary of token usage details.
    """
    def get_completion_from_messages(messages: List[Dict[str, str]],
                                     model: str,
                                     temperature: float = 0,
                                     max_tokens: int = 500) -> Tuple[str, Dict[str, int]]:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        content = response.choices[0].message["content"]

        token_dict = {
            'prompt_tokens':response['usage']['prompt_tokens'],
            'completion_tokens':response['usage']['completion_tokens'],
            'total_tokens':response['usage']['total_tokens'],
        }

        return content, token_dict

    # Check the model name is valid
    valid_models = ['GPT-3.5', 'GPT-4']
    if model_name not in valid_models:
        raise ValueError(f"'{model_name}' is not a valid argument. Choose from {valid_models}.")
    model_APInames_ = ['gpt-3.5-turbo', 'gpt-4']
    model_dict = dict(zip(valid_models, model_APInames_))
    # Check role name is valid
    valid_roles = ['Data relevant', 'Software Engineer', 'General']
    if role_name not in valid_roles:
        raise ValueError(f"'{role_name}' is not a valid argument. Choose from {valid_roles}.")  

    # Prompt preparation
    if role_name == 'Data relevant':
        system_message = ds_prompt
    elif role_name == 'Software Engineer':
        system_message = se_prompt
    else:
        system_message = general_prompt
    messages =  [
    {'role':'system',
    'content': system_message},
    {'role':'user',
    'content': f"####{user_message}####"},
    ]
    response, token_usage = get_completion_from_messages(messages, model_dict[model_name])
    return response, token_usage
    
def llm_run(model_name: str, role_name: str, user_message: str) -> Tuple[Dict[str, Union[float, str]], Union[str, None]]:
    """
    Runs the language model completion for a given model, role, and user message, 
    with moderation checks and response handling.

    :param model_name: Name of the model to use, e.g., 'GPT-3.5' or 'GPT-4'.
    :param role_name: Role for the conversation, e.g., 'Data relevant', 'Software Engineer', 'General'.
    :param user_message: The user's message for the conversation.
    :return: A tuple containing a response dictionary with the cost and optionally the company information,
             and an info string if there are issues with the input or response (e.g., 'flagged', 'not_job', 'not_json').

    :raises ValueError: If the model_name or role_name is not valid (checked in llm_completion).
    """
    # Check appropriateness of input
    moderation_output = openai.Moderation.create(user_message)["results"][0]
    info = None
    if moderation_output['flagged']:
        info = 'flagged'
        response_dict = {'cost': 0}
        return response_dict, info
    else:
        # API call
        response, token_usage = llm_completion(model_name, role_name, user_message)

    # Check if the input is relevant to job descriptions
    if token_usage['completion_tokens'] == 8:
        info = 'not_job'
        response_dict = {}
    # Check output from LLM
    elif not is_valid_json(response):
        info = 'not_json'
        response_dict = {}
    if info is None:
        # Parse output
        response_dict = json.loads(response)
        # Store data
        company_name = response_dict['Company']
        file_name = '_'.join(company_name.split(' ')) + '.txt'
        write_to_file(file_name, user_message)
        append_json_to_file(model_name, response_dict)

    # Calculate cost
    cost = api_cost(model_name, token_usage)
    response_dict['cost'] = cost
    return response_dict, info

def llm_deploy_run(model_name: str, role_name: str, user_message: str) -> Tuple[Dict[str, Union[float, str]], Union[str, None]]:
    """
    Same as llm_run except when running in deployed environment do not store data.

    :param model_name: Name of the model to use, e.g., 'GPT-3.5' or 'GPT-4'.
    :param role_name: Role for the conversation, e.g., 'Data relevant', 'Software Engineer', 'General'.
    :param user_message: The user's message for the conversation.
    :return: A tuple containing a response dictionary with the cost and optionally the company information,
             and an info string if there are issues with the input or response (e.g., 'flagged', 'not_job', 'not_json').

    :raises ValueError: If the model_name or role_name is not valid (checked in llm_completion).
    """
    # Check appropriateness of input
    moderation_output = openai.Moderation.create(user_message)["results"][0]
    info = None
    if moderation_output['flagged']:
        info = 'flagged'
        response_dict = {'cost': 0}
        return response_dict, info
    else:
        # API call
        response, token_usage = llm_completion(model_name, role_name, user_message)

    # Check if the input is relevant to job descriptions
    if token_usage['completion_tokens'] == 8:
        info = 'not_job'
        response_dict = {}
    # Check output from LLM
    elif not is_valid_json(response):
        info = 'not_json'
        response_dict = {}
    if info is None:
        # Parse output and don't store
        response_dict = json.loads(response)

    # Calculate cost
    cost = api_cost(model_name, token_usage)
    response_dict['cost'] = cost
    return response_dict, info

def api_cost(model_name: str, token_dict: Dict[str, int]) -> float:
    """
    Calculates the cost for an API call based on the model name and token usage.

    :param model_name: Name of the model used in the API call, must be one of ['GPT-3.5', 'GPT-4'].
    :param token_dict: Dictionary containing the token usage details, with keys 'prompt_tokens' and 'completion_tokens'.
    :return: Calculated cost for the API call.

    :raises ValueError: If the model_name is not valid.
    """
    # Check the model name is valid
    valid_models = ['GPT-3.5', 'GPT-4']
    if model_name not in valid_models:
        raise ValueError(f"'{model_name}' is not a valid argument. Choose from {valid_models}.")

    # Calculate cost based on the model name
    if model_name == 'GPT-3.5':
        cost = token_dict['prompt_tokens'] / 1000 * 0.0015 + token_dict['completion_tokens'] / 1000 * 0.002
    elif model_name == 'GPT-4':
        cost = token_dict['prompt_tokens'] / 1000 * 0.03 + token_dict['completion_tokens'] / 1000 * 0.06
    else:
        cost = 0
    return cost
