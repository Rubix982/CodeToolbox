#!/bin/sh

# Add this to your shell configuration to redirect the output generated to a timestamp-ed file to revisit logs easily.
ts_out() {
    if [[ $# -lt 2 ]]; then
        echo "Usage: ts_out <command> <script> [args...]"
        return 1
    fi

    local cmd=$1       # The command (e.g., python3)
    shift              # Shift to the next argument
    local script=$1    # The script name (e.g., app.py)
    shift              # Shift again to allow more arguments if needed

    # Remove any existing "_output" before timestamping
    local base_name="${script%.*}"  # Removes extension (.py, .sh, etc.)
    local output_file="${base_name}_$(date +%Y-%m-%d_%H-%M-%S).txt"

    "$cmd" "$script" "$@" > "$output_file"
}
