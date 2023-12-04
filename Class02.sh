#!/bin/bash



# Script to show Date and Time

echo `date`
# Assign variables to capture the Year only
#!/bin/bash

# Get the current date and store it in a variable
current_date=$(date)

# Extract only the year from the date
year=$(date -d "$current_date" +"%Y")

# Print the extracted year
echo "Current Year: $year"

# Get the current month and store it in a variable. Use B for month.
current_month=$(date +"%B")
# You can also use month=`date +%m`

# Print the current month
echo "Current Month: $current_month"

# Get the current day of the month and store it in a variable
current_day=$(date +"%d")
# You can also use day=`date +%d`
# Print the current day of the month
echo "Current Day of the Month: $current_day"

# Get the complete date and store it in a variable
complete_date=$(date +"%A, %B %d, %Y")

# Print the complete date
echo "Complete Date: $complete_date"
# You can make it even simpler by scpriting
echo "Current Date: $day-$month-$year"
echo "Current Date: $(date +%d-%m-%Y)"

# How to append this content to a file

# The >> dbl carrot will append to the file
echo "My new string with date: $(date +%d-%m-%Y)" >> test.txt

mv test.txt test-$(date +%d-%m-%Y)








