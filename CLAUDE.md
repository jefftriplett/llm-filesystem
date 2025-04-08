# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build/Test Commands
- Install: `pip install -e '.[test]'`
- Run tests: `python -m pytest`
- Run a single test: `python -m pytest tests/test_file.py::test_function_name -v`
- Format code: `black llm_filesystem.py`
- Type check: `mypy llm_filesystem.py`

## Code Style Guidelines
- **Imports**: Standard library first, then third-party, then local imports
- **Formatting**: Follow PEP 8 conventions
- **Types**: Use type hints for function parameters and return values
- **Naming**: 
  - snake_case for functions, variables, and modules
  - CamelCase for classes
- **Error Handling**: Use specific exceptions with helpful error messages
- **Documentation**: Use docstrings for functions and classes
- **Hook Implementation**: Follow the llm plugin hook pattern for registrations

## Project Context
This is a plugin for the LLM CLI tool that enables loading templates from the filesystem.