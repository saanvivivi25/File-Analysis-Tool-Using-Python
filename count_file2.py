def count_file_details(file_path):

    try:
        with open(file_path, "r") as file:
            content = file.read()

        results = {
            "lines": len(content.splitlines()),
            "words": len(content.split()),
            "characters": len(content)
        }

        return results

    except FileNotFoundError:
        print("Error: File not found.")
        return None

    except PermissionError:
        print("Error: Permission denied. Cannot access the file.")
        return None


def display_report(results):
   
    if results:
        print("Number of Lines      :", results["lines"])
        print("Number of Words      :", results["words"])
        print("Number of Characters :", results["characters"])

# User Input
file_path = input("Enter the file path: ")

# Process File
report = count_file_details(file_path)

# Display Results
display_report(report)