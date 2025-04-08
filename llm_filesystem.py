from llm import Template, hookimpl
import yaml
import os


@hookimpl
def register_template_loaders(register):
    register("file", file_template_loader)


def file_template_loader(template_path: str) -> Template:
    """
    Load a template from the local file system.

    Format: path/to/template
    Supports '~' for home directory paths.
    """
    expanded_path = os.path.expanduser(f"{template_path}")

    if not os.path.isfile(expanded_path):
        raise ValueError(f"Template file '{expanded_path}' does not exist.")

    try:
        with open(expanded_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except OSError as ex:
        raise ValueError(f"Failed to read template file: {ex}")

    try:
        loaded = yaml.safe_load(content)
        if isinstance(loaded, str):
            return Template(name=template_path, prompt=loaded)
        else:
            return Template(name=template_path, **loaded)
    except yaml.YAMLError as ex:
        raise ValueError(f"Invalid YAML in template file: {ex}")
