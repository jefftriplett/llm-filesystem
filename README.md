# llm-filesystem

[![PyPI](https://img.shields.io/pypi/v/llm-filesystem.svg)](https://pypi.org/project/llm-filesystem/)
[![Changelog](https://img.shields.io/github/v/release/jefftriplett/llm-filesystem?include_prereleases&label=changelog)](https://github.com/jefftriplett/llm-filesystem/releases)
[![Tests](https://github.com/jefftriplett/llm-filesystem/actions/workflows/test.yml/badge.svg)](https://github.com/jefftriplett/llm-filesystem/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/jefftriplett/llm-filesystem/blob/main/LICENSE)

Load LLM templates from the local filesystem

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/).
```bash
llm install llm-filesystem
```

## Usage

To use a template from the local filesystem:

```bash
llm -t file:/path/to/template.yaml
```

The plugin supports using `~` for home directory paths:

```bash
llm -t file:~/templates/my-template.yaml
```

Templates should be in YAML format, either as:
- A simple string (which becomes the prompt)
- A structured YAML with additional template properties

Example template:
```yaml
# Simple example - just the prompt
"Summarize the following text in three bullet points: {{input}}"
```

Or with more options:
```yaml
system: You are a helpful AI assistant.
prompt: |
  Summarize the following text:
  
  {{input}}
model: gpt-4
temperature: 0.7
```

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd llm-filesystem
python -m venv venv
source venv/bin/activate
```

Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```

To run the tests:
```bash
python -m pytest
```

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.