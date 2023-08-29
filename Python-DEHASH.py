import requests
import json
from termcolor import colored
#API can be retrieved from dehashed.com
BASE_URL = "https://api.dehashed.com/search"
EMAIL = "EMAIL"  # Replace with your email
API_KEY = "api-KEY"  # Replace with your API key

def display_menu():
    """Display the search criteria menu and retrieve user's choice."""
    options = [
        "id", "email", "ip_address", "username", "password",
        "hashed_password", "hash_type", "name", "vin", "address",
        "phone", "database_name"
    ]

    print("Select the criteria you want to search by:")
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")

    choice = int(input("Enter your choice (1-12): "))
    while choice < 1 or choice > 12:
        print("Invalid choice. Please enter a number between 1 and 12.")
        choice = int(input("Enter your choice (1-12): "))

    return options[choice - 1]

def escape_reserved_characters(value):
    reserved_characters = "+-=&||><!(){}[]^\"~*?:\\"
    for char in reserved_characters:
        value = value.replace(char, f"\\{char}")
    return value


def search_dehashed(criteria, value):
    """Search DeHashed based on given criteria."""
    
    value = escape_reserved_characters(value)
    
    # Set up the search parameters
    params = {
        "query": f'{criteria}:"{value}"'
    }

    # ... (rest of the function remains unchanged)
    response = requests.get(
        BASE_URL,
        params=params,
        headers={"Accept": "application/json"},
        auth=(EMAIL, API_KEY)
    )

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"HTTP {response.status_code}: {response.text}"}

def color_code_output(data):
    """Color-code the JSON keys and values in the output."""
    json_str = json.dumps(data, indent=4, sort_keys=True)
    lines = json_str.split('\n')
    colored_lines = []

    for line in lines:
        stripped_line = line.strip()

        if stripped_line.endswith(':') or stripped_line.endswith('{') or stripped_line.endswith('['):
            # It's just a key or the start of an object or array
            colored_lines.append(colored(line, 'blue'))
        else:
            # It's a key-value pair or the end of an object or array
            key_part, _, value_part = line.partition(':')
            colored_key = colored(key_part, 'blue')
            colored_value = colored(value_part, 'green')
            colored_lines.append(f"{colored_key}:{colored_value}")

    return '\n'.join(colored_lines)

if __name__ == "__main__":
    criteria = display_menu()
    value_to_search = input(f"Enter the {criteria} to search for: ")
    results = search_dehashed(criteria, value_to_search)

    with open("output.json", "w") as file:
        json.dump(results, file, indent=4, sort_keys=True)

    print(color_code_output(results))
import requests
import json
from termcolor import colored

BASE_URL = "https://api.dehashed.com/search"
EMAIL = "firsttolast@proton.me"  # Replace with your email
API_KEY = "p58u2jcb52kcowq9brl7fbri3gwb7xg4"  # Replace with your API key

def display_menu():
    """Display the search criteria menu and retrieve user's choice."""
    options = [
        "id", "email", "ip_address", "username", "password",
        "hashed_password", "hash_type", "name", "vin", "address",
        "phone", "database_name"
    ]

    print("Select the criteria you want to search by:")
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")

    choice = int(input("Enter your choice (1-12): "))
    while choice < 1 or choice > 12:
        print("Invalid choice. Please enter a number between 1 and 12.")
        choice = int(input("Enter your choice (1-12): "))

    return options[choice - 1]

def search_dehashed(criteria, value):
    """Search DeHashed based on given criteria."""
    
    params = {
        "query": f'{criteria}:"{value}"'
    }

    response = requests.get(
        BASE_URL,
        params=params,
        headers={"Accept": "application/json"},
        auth=(EMAIL, API_KEY)
    )

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"HTTP {response.status_code}: {response.text}"}

def color_code_output(data):
    """Color-code the JSON keys and values in the output."""
    json_str = json.dumps(data, indent=4, sort_keys=True)
    lines = json_str.split('\n')
    colored_lines = []

    for line in lines:
        stripped_line = line.strip()

        if stripped_line.endswith(':') or stripped_line.endswith('{') or stripped_line.endswith('['):
            # It's just a key or the start of an object or array
            colored_lines.append(colored(line, 'blue'))
        else:
            # It's a key-value pair or the end of an object or array
            key_part, _, value_part = line.partition(':')
            colored_key = colored(key_part, 'blue')
            colored_value = colored(value_part, 'green')
            colored_lines.append(f"{colored_key}:{colored_value}")

    return '\n'.join(colored_lines)

if __name__ == "__main__":
    criteria = display_menu()
    value_to_search = input(f"Enter the {criteria} to search for: ")
    results = search_dehashed(criteria, value_to_search)

    with open("output.json", "w") as file:
        json.dump(results, file, indent=4, sort_keys=True)

    print(color_code_output(results))
##why you still reading?
##Let me know if you have any future suggestions for this code