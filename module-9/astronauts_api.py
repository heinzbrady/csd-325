import requests

ASTROS_URL = "http://api.open-notify.org/astros.json"

def test_connection():
    """Tests the connection to the API and prints the status code."""
    response = requests.get(ASTROS_URL, timeout=10)
    print("Testing connection to:", ASTROS_URL)
    print("Status code:", response.status_code)
    response.raise_for_status()
    print("Connection test: SUCCESS\n")

def get_astronaut_data():
    """Gets astronaut data (JSON) from the API."""
    response = requests.get(ASTROS_URL, timeout=10)
    response.raise_for_status()
    return response.json()

def print_formatted(data):
    """Print astronaut list formatted like the tutorial."""
    print("===== FORMATTED OUTPUT =====")
    number = data["number"]
    people = data["people"]

    print(f"There are currently {number} people in space.\n")
    for person in people:
        print(f"{person['name']} is on the {person['craft']}")
    print("============================")

def main():
    test_connection()
    data = get_astronaut_data()
    print_formatted(data)

if __name__ == "__main__":
    main()