import requests

URL = "https://swapi.dev/api/people/1/"

def test_connection():
    response = requests.get(URL, timeout=10)
    print("Testing connection to:", URL)
    print("Status code:", response.status_code)
    response.raise_for_status()
    print("Connection test: SUCCESS\n")

def get_data():
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    return response.json()

def print_raw(data):
    print("----- RAW RESPONSE (no formatting) -----")
    print(data)
    print("----------------------------------------\n")

def print_formatted(data):
    print("===== FORMATTED OUTPUT =====")
    print(f"Name        : {data['name']}")
    print(f"Birth Year  : {data['birth_year']}")
    print(f"Gender      : {data['gender']}")
    print(f"Height      : {data['height']} cm")
    print(f"Mass        : {data['mass']} kg")
    print(f"Hair Color  : {data['hair_color']}")
    print(f"Eye Color   : {data['eye_color']}")
    print(f"Skin Color  : {data['skin_color']}")
    print("============================")

def main():
    test_connection()
    data = get_data()
    print_raw(data)
    print_formatted(data)

if __name__ == "__main__":
    main()