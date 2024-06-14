import csv
import json
from pathlib import Path

def csv_to_json(csv_file_path, json_file_path):
    try:
        # Ensure the file paths are valid
        csv_file_path = Path(csv_file_path)
        json_file_path = Path(json_file_path)

        # Create an empty list to store the data
        data = []

        # Open the CSV file for reading
        with csv_file_path.open(mode='r', encoding='utf-8-sig') as csv_file:
            # Create a CSV reader object
            csv_reader = csv.DictReader(csv_file)
            
            # Loop through each row in the CSV file
            for row in csv_reader:
                # Append each row to the data list
                data.append(row)

        # Convert the list of dictionaries to a JSON string
        json_data = json.dumps(data, ensure_ascii=False, indent=4)

        # Write the JSON string to a file
        with json_file_path.open(mode='w', encoding='utf-8') as json_file:
            json_file.write(json_data)

    except FileNotFoundError:
        print(f"The file {csv_file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Provide the path to your CSV file and the desired output path for the JSON file
csv_file_path = 'path/to/your/input.csv'
json_file_path = 'path/to/your/output.json'

# Call the function to convert CSV to JSON
csv_to_json(csv_file_path, json_file_path)
