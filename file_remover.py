import os
import json


def load_removal_filter(json_file):
    """
    Load the file removal filter array from a JSON configuration file.

    :param json_file: Path to the JSON file containing 'removal_filter'.
    :return: List of file patterns or names to be removed.
    """
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            removal_filter = data.get('removal_filter', [])  # Default to empty list if key is not present
        return removal_filter
    except FileNotFoundError:
        print(f"Error: The file '{json_file}' was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The JSON file '{json_file}' is not correctly formatted.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred while loading the removal filter: {e}")
        return []


def remove_files_by_filter(folder_path, filter_array):
    """
    Remove files in the specified folder that match any of the patterns in filter_array.

    :param folder_path: The folder where files will be removed.
    :param filter_array: List of file names or patterns to be removed.
    """
    try:
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")

        # Get all files in the folder
        files_in_folder = os.listdir(folder_path)

        # Iterate through the files and remove those that match the filter_array
        for file_name in files_in_folder:
            for filter_item in filter_array:
                if filter_item in file_name:  # Matching by substring, can be changed to exact match if needed
                    file_path = os.path.join(folder_path, file_name)
                    try:
                        os.remove(file_path)
                        print(f"Removed file: {file_path}")
                    except FileNotFoundError:
                        print(f"Error: The file '{file_path}' was not found.")
                    except PermissionError:
                        print(f"Error: Permission denied while trying to remove '{file_path}'.")
                    except Exception as e:
                        print(f"Failed to remove '{file_path}': {e}")

        print("File removal process completed.")
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as e:
        print(f"An unexpected error occurred during file removal: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Folder where files will be removed
        folder_path = r'Temporary_files'

        # Load the removal filter from the config.json file
        json_file = r'config.json'
        removal_filter = load_removal_filter(json_file)

        if removal_filter:
            # Call the function to remove files
            remove_files_by_filter(folder_path, removal_filter)
        else:
            print("No files to remove. The removal filter is empty or invalid.")

    except Exception as e:
        print(f"An error occurred in the main script: {e}")
