import csv

# Open the log file for reading and the CSV file for writing
with open('datasets\sample_log_cty_final.log.txt', 'r') as log_file, open('log.csv', 'w', newline='') as csv_file:

    # Create a CSV writer object
    writer = csv.writer(csv_file)

    # Loop through each line in the log file
    for line in log_file:

        # Split the line into fields using the appropriate delimiter
        fields = line.split(' ')

        # Write the fields to the CSV file
        writer.writerow(fields)