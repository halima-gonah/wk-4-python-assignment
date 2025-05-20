def read_and_modify_file():
    # Ask the user for the input file name
    filename = input("Enter the filename to read from: ")

    try:
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Define a new output file name
        new_filename = "modified_" + filename

        # Write the modified content to a new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to: {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: Unable to read or write file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
