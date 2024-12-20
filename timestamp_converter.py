#!/usr/bin/env python3
import argparse
from datetime import datetime


def unix_to_readable(unix_timestamp):
    # Convert Unix timestamp to a datetime object
    dt_object = datetime.fromtimestamp(int(unix_timestamp))
    # Format the datetime object to a readable string
    readable_format = dt_object.strftime('%Y-%m-%d %H:%M:%S')
    return readable_format


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Convert Unix timestamp to human-readable format.")
    parser.add_argument("timestamp", help="Unix timestamp to be converted")

    # Parse arguments
    args = parser.parse_args()

    # Convert the Unix timestamp
    readable_time = unix_to_readable(args.timestamp)

    # Print the result
    print(f"Human-readable format: {readable_time}")


if __name__ == "__main__":
    main()
