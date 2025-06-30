# convert.py
import csv
import json
import os
from argparse import ArgumentParser
from pathlib import Path


def expand_path(path):
    """
    Expands the user home directory (~) in the path.
    """
    return os.path.expanduser(path)


def read_csv(path, delimiter=";", has_headers=True, skip_lines=0):
    """
    Read CSV formatted data from `path` and return a list of rows.
    """
    path = expand_path(path)  # Expand user home directory (~)
    
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        data = list(reader)
        
        # Skip lines at the beginning if specified
        data = data[skip_lines:]

        if has_headers:
            headers = data[0]
            rows = data[1:]
            return headers, rows
        else:
            return None, data


def write_csv(path, data, delimiter="|", headers=None):
    """
    Write list of rows to a CSV file at `path` using `delimiter`.
    Optionally includes headers if provided.
    """
    path = expand_path(path)  # Expand user home directory (~)
    
    with open(path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter)
        if headers:
            writer.writerow(headers)  # Write headers if they exist
        writer.writerows(data)


def write_json(path, data, headers=None):
    """
    Write list of rows to a JSON file at `path`.
    Each row is converted to a dictionary with header-value pairs.
    The resulting JSON will be an array of dictionaries.
    """
    path = expand_path(path)  # Expand user home directory (~)

    json_data = []
    
    for row in data:
        # If headers are provided, use them as dictionary keys
        if headers:
            row_dict = {headers[i]: row[i] for i in range(len(headers))}
        else:
            # If no headers, use generic column names as keys
            row_dict = {f"column{i+1}": row[i] for i in range(len(row))}
        json_data.append(row_dict)

    with open(path, 'w', encoding='utf-8') as jsonfile:
        json.dump(json_data, jsonfile, indent=2)


def convert():
    """
    Convert data from one CSV format to another CSV format or JSON.
    """
    parser = ArgumentParser(description="Convert CSV to CSV or JSON with new formatting.")
    
    # Positional arguments for input and output files
    parser.add_argument("input_file", help="Input CSV file path")
    parser.add_argument("output_file", help="Output file path (without extension)")
    
    # Optional flags
    parser.add_argument("-d", default=";", help="Input CSV delimiter (default: ';')")
    parser.add_argument("-t", default="|", help="Output CSV delimiter (default: '|')")
    parser.add_argument("-f", choices=["csv", "json"], default="csv", help="Specify the output format (csv or json)")
    parser.add_argument("-v", action="store_true", help="Enable verbose logging")
    parser.add_argument("-H", action="store_true", help="Specify if input file contains headers")
    parser.add_argument("-s", type=int, default=0, help="Number of lines to skip at the start of the file")

    args = parser.parse_args()

    if args.v:
        print("Verbose mode enabled.")
        print(f"Input file: {args.input_file}")
        print(f"Output file: {args.output_file}")
        print(f"Input delimiter: {args.d}")
        print(f"Output delimiter: {args.t}")
        print(f"Output format: {args.f}")
        print(f"Skip lines: {args.s}")

    headers, data = read_csv(args.input_file, delimiter=args.d, has_headers=args.H, skip_lines=args.s)

    # Write the output based on the format
    output_path = f"{args.output_file}.csv" if args.f == "csv" else f"{args.output_file}.json"
    
    if args.f == "csv":
        write_csv(output_path, data, delimiter=args.t, headers=headers)
    else:
        write_json(output_path, data, headers=headers)


if __name__ == "__main__":
    convert()