import csv
import os

def remove_spaces_from_csv_in_place(file_path):
    # Read the original content of the file
    with open(file_path, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        rows = []
        for row in reader:
            # Remove spaces from each cell
            processed_row = [cell.replace(" ", "") for cell in row]
            # Check if the row is not empty after removing spaces
            if any(cell for cell in processed_row):
                rows.append(processed_row)

    # Write the processed content back to the same file
    with open(file_path, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows)

def main():
    csv_file = 'locations.csv'
    remove_spaces_from_csv_in_place(csv_file)

if __name__ == '__main__':
    main()
