import csv

def copy_previous_value(csv_file_path, column_index):
    updated_rows = []

    with open(csv_file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        previous_value = ""

        for row in reader:
            if row[column_index] == "":
                row[column_index] = previous_value
            else:
                previous_value = row[column_index]

            updated_rows.append(row)

    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in updated_rows:
            writer.writerow(row)

# Example usage
csv_file_path = 'input.csv'
column_index = 1  # Assuming the specific column index is 2

copy_previous_value(csv_file_path, column_index)