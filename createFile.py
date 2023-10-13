import os

def create_file(filename):
    try:
        with open(filename, 'w'):
            pass  # This will create an empty file
        print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")




