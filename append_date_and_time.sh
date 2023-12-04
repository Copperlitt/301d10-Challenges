#!/bin/bash

# Script Name:                    Append; Date and Time
# Author:                         Basil Evelyn
# Date of last revision           12/04/2023

# Copy /var/log/syslog to the current working directory
cp /var/log/syslog .

echo "syslog copied to the current working directory."

# Filename with the current date and time
filename="append_date_and_time_$(date +'%Y%m%d_%H%M%S').sh"

# Appending a message to the file
echo "#!/bin/bash" > "$filename"
echo "echo 'Hello, this script was created at $(date)'" >> "$filename"

echo "Script created: $filename"