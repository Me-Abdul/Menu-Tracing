# Navigation Links Depth Parser

This script is used to parse navigation links with depth.

## Requirements

- Python 3.x

## Usage

Run the script with the following command:
    ```
    python script_name.py <url> [-u] [-v]
    ```
    Replace `script_name.py` with the name of your script and `<url>` with the URL you want to parse.

## Arguments

- `url`: The URL to parse (compulsory).
- `-u` or `--unique`: Unique flag (optional). If set, the script will not consider unique navigation links.
- `-v` or `--verbose`: Verbose flag (optional). If set, the script will provide more detailed output.

## Example

To parse the navigation links of '<https://www.example.com>' considering only unique links and in verbose mode, use the following command:
    ```
    python script_name.py https://www.example.com -u -v
    ```

## Error Handling

If a URL is not provided, the script will print an error message and display the help text.
