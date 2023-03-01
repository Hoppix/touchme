import logging
import src.py.template as python_template
import src.sh.template as shell_template


def get_template(filename: str):
    split = filename.split(".")
    file_type = split[len(split) - 1]
    logging.debug(f"File type is {file_type}")

    template = shell_template

    if file_type == "py":
        logging.debug("Recognized python file type")
        template = python_template
    elif file_type == "sh":
        logging.debug("Recognized shell file type")
        template = shell_template
    else:
        logging.warn("No recognized file format, falling back to shell script type")
        template = shell_template
    
    return template.content