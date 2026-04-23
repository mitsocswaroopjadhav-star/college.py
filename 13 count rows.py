import csv

def count_rows_in_csv(file_name):
    try:
        with open(file_name, mode='r', newline='') as file:
            reader = csv.reader(file)
            row_count = sum(1 for row in reader)  # Counts each row in the file
        return row_count
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

if __name__ == "__main__":
    file_name = input("Enter the CSV file name (with extension): ")
    total_rows = count_rows_in_csv(file_name)
    if total_rows > 0:
        print(f"The total number of rows in the CSV file is: {total_rows}")
    else:
        print("No rows were found in the CSV file.")