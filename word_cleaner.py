import os


def replace_words_in_file(file_path, target_word, replacer_word):
    """
    Replace or remove words from a markdown file based on the given arrays.

    :param file_path: Path to the markdown file.
    :param target_word: List of words to find in the file.
    :param replacer_word: List of replacement words (use an empty string to remove).
    """
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")

        # Read the file content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Check if target_word and replacer_word lengths match
        if len(target_word) != len(replacer_word):
            raise IndexError("The lengths of target_word and replacer_word do not match.")

        # Replace words based on target_word and replacer_word
        for i in range(len(target_word)):
            content = content.replace(target_word[i], replacer_word[i])

        # Write the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

        print(f"Replacements completed in file: {file_path}")

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except PermissionError:
        print(f"Permission denied: Unable to access or modify {file_path}.")
    except IndexError as index_error:
        print(f"Error: {index_error}")
    except Exception as e:
        print(f"An unexpected error occurred while processing the file '{file_path}': {e}")


def process_markdown_files(folder_path, target_word, replacer_word):
    """
    Process all markdown files in a folder, replacing or removing words.

    :param folder_path: Directory containing markdown files.
    :param target_word: List of words to find in the file.
    :param replacer_word: List of replacement words (use an empty string to remove).
    """
    try:
        # Check if the folder exists
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"The folder {folder_path} does not exist.")

        # Get all markdown files in the folder
        md_files = [f for f in os.listdir(folder_path) if f.endswith('.md')]

        if not md_files:
            print(f"No markdown files found in {folder_path}.")
            return

        # Process each markdown file
        for file_name in md_files:
            file_path = os.path.join(folder_path, file_name)
            replace_words_in_file(file_path, target_word, replacer_word)

        print("All markdown files processed successfully.")

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except PermissionError:
        print(f"Permission denied: Unable to access or modify files in {folder_path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    folder_path = r'Separate_files'  # Folder with markdown files

    # Words to be replaced
    target_word = ['old_word1', 'old_word2', 'word_to_remove']  # Words to replace/remove
    replacer_word = ['new_word1', 'new_word2', '']  # Replacement words ('' for removal)

    # Call the function to process the markdown files
    process_markdown_files(folder_path, target_word, replacer_word)
