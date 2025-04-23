
def read_and_modify_file():
    filename = input("Enter the filename to read from (e.g., input.txt): ")

    try:
        with open(filename, 'r') as file:
            content = file.readlines()

        # Modify the content (Example: convert to uppercase)
        modified_content = [line.upper() for line in content]

        # Ask for output file name
        output_filename = input("Enter the filename to write to (e.g., output.txt): ")

        with open(output_filename, 'w') as file:
            file.writelines(modified_content)

        print(f"Success ✅! Modified content written to '{output_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read/write this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the program
read_and_modify_file()
