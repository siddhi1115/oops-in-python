class FileMissingError(Exception):
    "Custom exception for missing file"
    pass

def check_file():
    try:
        try:
            file = open("missing.txt", "r")
            file.close()
        except FileNotFoundError:
            raise FileMissingError("Required file not found!")

    except FileMissingError as error:
        print(f"Error: {error}")

    else:
        print("File opened successfully.")

    finally:
        print("Execution completed.")

check_file()