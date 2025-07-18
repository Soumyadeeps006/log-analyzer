def analyze_log_file(log_file_path, output_file_path):
    try:
        with open(log_file_path, 'r') as log_file:
            lines = log_file.readlines()

        error_lines = [line for line in lines if 'ERROR' in line.upper()]
        error_count = len(error_lines)

        with open(output_file_path, 'w') as output_file:
            output_file.write(f"Total ERROR entries: {error_count}\n")
            output_file.write("List of ERROR lines:\n")
            for line in error_lines:
                output_file.write(line)

        print(f"Analysis complete. {error_count} errors found.")
        print(f"Results written to {output_file_path}")

    except FileNotFoundError:
        print(f"Error: The file {log_file_path} was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    log_file = "app.log"
    output_file = "error_report.txt"
    analyze_log_file(log_file, output_file)