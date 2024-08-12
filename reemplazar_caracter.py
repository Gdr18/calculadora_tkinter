import os

modified_files = []


def replace_character(directory, replacement, *original):
    files = [
        f
        for f in os.listdir(directory)
        if not f.startswith(".") and not ".ini" in f and not ".md" in f
    ]
    for file in files:
        file_path = os.path.join(directory, file)
        if os.path.isdir(file_path):
            replace_character(file_path, replacement, *original)
        new_file = file.lower()
        os.rename(os.path.join(directory, file), os.path.join(directory, new_file))
        for arg in original:
            if arg in new_file:
                new_file = new_file.replace(arg, replacement)
                os.rename(
                    os.path.join(directory, file), os.path.join(directory, new_file)
                )
                modified_files.append(new_file)
    return modified_files


if __name__ == "__main__":
    changes = replace_character(
        "C:\\Users\\Gádor\\Desktop\\Gádor\\work_hard",
        "-",
        " ",
        "_",
    )
    print(changes)
