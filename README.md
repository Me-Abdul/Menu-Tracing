# Navigation Links Depth Parser

This script is used to parse navigation links with depth and can store the output in JSON or XML format.

## Requirements

- Python 3.x

## Usage

Run the script with the following command:
    ```
    python script_name.py <url> [-u] [-v] [-o output_file] [-f format]
    ```
    Replace `script_name.py` with the name of your script and `<url>` with the URL you want to parse.

## Arguments

- `url`: The URL to parse (compulsory).
- `-u` or `--unique`: Unique flag (optional). If set, the script will not consider unique navigation links.
- `-v` or `--verbose`: Verbose flag (optional). If set, the script will provide more detailed output.
- `-o` or `--output`: Output file (optional). If set, the script will write the output to the specified file.
- `-f` or `--format`: Output format (optional). If set, the script will write the output in the specified format ('json' or 'xml').

## Example

To parse the navigation links of '<https://www.example.com>' considering only unique links, in verbose mode, and store the output in 'output.json' in JSON format, use the following command:
    ```    python script_name.py https://www.example.com -u -v -o output.json -f json    ``` OR
    ```    python script_name.py https://www.example.com -u -v -o output.xml -f xml    ```

## Error Handling

If a URL is not provided, the script will print an error message and display the help text. If an output file is specified but the format is not, the script will not write the output to a file. It will only print the output to the console as before. 
