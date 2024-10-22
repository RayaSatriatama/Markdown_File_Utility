import os


def get_markdown_files(folder_path, sort_order="asc"):
    """
    Get all .md files from the specified folder with optional sorting in ascending or descending order.

    :param folder_path: Directory to search for .md files.
    :param sort_order: Sorting order ('asc' for ascending, 'dsc' for descending, or None to disable sorting).
    :return: List of .md files, sorted based on the sort_order.
    """
    try:
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"Input folder '{folder_path}' does not exist.")

        md_files = [f for f in os.listdir(folder_path) if f.endswith('.md')]

        # Apply sorting if sort_order is specified
        if sort_order == "asc":
            md_files.sort()  # Sort in ascending order
        elif sort_order == "dsc":
            md_files.sort(reverse=True)  # Sort in descending order

        return md_files

    except FileNotFoundError as fnf_error:
        print(fnf_error)
        return []
    except PermissionError as perm_error:
        print(f"Permission error while accessing folder '{folder_path}': {perm_error}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred while getting markdown files: {e}")
        return []


def combine_files(input_folder, files, output_file_path, separator="\n\n---\n\n"):
    """
    Combine content of markdown files and write to an output file.

    :param input_folder: Directory containing the .md files.
    :param files: List of .md file names to combine.
    :param output_file_path: Output file path where combined content will be saved.
    :param separator: Separator to use between files (default is "---" with newlines).
    """
    try:
        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            for file_name in files:
                file_path = os.path.join(input_folder, file_name)
                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        outfile.write(content)
                        outfile.write(separator)
                except FileNotFoundError:
                    print(f"Error: File '{file_path}' not found.")
                except PermissionError:
                    print(f"Permission denied when reading the file '{file_path}'.")
                except Exception as e:
                    print(f"An unexpected error occurred while reading the file '{file_path}': {e}")
    except PermissionError:
        print(f"Permission denied when writing to the output file '{output_file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred while writing the combined file: {e}")


def combine_markdown_files(input_folder, output_folder, output_file, separator="\n\n---\n\n", sort_order="asc"):
    """
    Combine all markdown files in a folder and output them into a single file, with optional sorting.

    :param input_folder: Directory containing markdown files to combine.
    :param output_folder: Directory to save the combined file.
    :param output_file: The name of the combined output file.
    :param separator: The separator to insert between files (default is "---" with newlines).
    :param sort_order: Sorting order ('asc' for ascending, 'dsc' for descending, or None to disable sorting).
    """
    try:
        # Get markdown files, with sorting based on the sort_order flag
        md_files = get_markdown_files(input_folder, sort_order)

        if not md_files:
            raise Exception("No markdown files found to combine.")

        # Ensure output folder exists, create it if necessary
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Define output file path
        output_file_path = os.path.join(output_folder, output_file)

        # Combine markdown files into one file
        combine_files(input_folder, md_files, output_file_path, separator)

        print(f"Markdown files combined successfully into: {output_file_path}")

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except PermissionError as perm_error:
        print(f"Permission error: {perm_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage in another file or project:
if __name__ == "__main__":
    input_folder = 'path_to_markdown_folder'  # Folder containing .md files
    output_folder = 'path_to_output_folder'  # Folder where the output file will be saved
    output_file = 'combined_markdown.md'  # Name of the output file
    separator = "\n\n---\n\n"  # Separator between the files
    sort_order = "asc"  # Options: "asc" for ascending, "dsc" for descending, None for no sorting

    # Combine markdown files with sorting in ascending order
    combine_markdown_files(input_folder, output_folder, output_file, separator, sort_order)
