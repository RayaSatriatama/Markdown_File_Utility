import json
import os
from markdown_combiner import combine_markdown_files
from word_cleaner import process_markdown_files
from file_remover import load_removal_filter, remove_files_by_filter


# Function to load the JSON file with target and replacer words
def load_replacements(json_file):
    """
    Load the replacement words from a JSON file.

    :param json_file: Path to the JSON file containing 'target_word' and 'replacer_word'.
    :return: Two lists - target words and replacer words.
    """
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            target_word = data['target_word']
            replacer_word = data['replacer_word']
        return target_word, replacer_word, data
    except FileNotFoundError:
        print(f"Error: The file {json_file} was not found.")
        return None, None
    except json.JSONDecodeError:
        print(f"Error: The JSON file {json_file} is incorrectly formatted.")
        return None, None
    except Exception as e:
        print(f"An unexpected error occurred while loading replacements: {e}")
        return None, None


if __name__ == "__main__":
    try:
        # Define the input folder containing the markdown files
        input_folder = r'Your_Path'
        output_folder = r'Your_Path'
        output_file = 'combined_result.md'
        separator = "\n\n---\n\n"
        sort_order = 'asc'

        # Ensure input and output directories exist
        if not os.path.exists(input_folder):
            raise FileNotFoundError(f"Input folder {input_folder} does not exist.")
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)  # Create output folder if it doesn't exist

        # Combine markdown files
        combine_markdown_files(input_folder, output_folder, output_file, separator, sort_order)
        print("Markdown files have been combined successfully!")

        # Load replacement words from JSON file
        json_file = r'D:\Projects\Programming_Projects\Markdown_File_Merging\config.json'
        target_words, replacer_words = load_replacements(json_file)

        if target_words is None or replacer_words is None:
            raise Exception("Failed to load replacement words.")

        # Process the markdown files in the output folder to replace/remove words
        process_markdown_files(output_folder, target_words, replacer_words)
        print("Words have been replaced in the combined markdown files.")

        # Load file removal filter from the JSON file
        removal_filter = load_removal_filter(json_file)

        if removal_filter is None:
            raise Exception("Failed to load file removal filter.")

        # Call the file removal function to clean up temporary files
        remove_files_by_filter(input_folder, removal_filter)
        print("File cleanup completed!")

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
