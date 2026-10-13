# Python - Async Comprehension

## Description

This project introduces asynchronous generators, asynchronous comprehensions, and type annotations for generators in Python.

It focuses on asynchronous programming and the use of `async` and `await` to handle operations without blocking the event loop.

## Learning Objectives

At the end of this project, you should be able to explain:

- How to write an asynchronous generator.
- How to use asynchronous comprehensions.
- How to type-annotate generators.
- How to use asynchronous iteration with `async for`.
- How to combine `await` and `yield` in an asynchronous generator.

## Requirements

- All files are interpreted and compiled using Python 3.8 on Ubuntu 20.04 LTS.
- All files must start with `#!/usr/bin/env python3`.
- All files must end with a new line.
- Code must follow the `pycodestyle` style guide, version 2.5.x.
- All modules and functions must include meaningful documentation.
- All functions and coroutines must have type annotations.
- A `README.md` file is required at the root of the project directory.

## Tasks

### 0. Async Generator

Create an asynchronous generator named `async_generator` that takes no arguments.

The generator must loop ten times, wait asynchronously for one second during each iteration, and yield a random number between 0 and 10 using the `random` module.

The generated values are collected using `async for` and stored in a list.

## Resources

- [PEP 530 — Asynchronous Comprehensions](https://peps.python.org/pep-0530/)
- [What's New in Python 3.6](https://docs.python.org/3.6/whatsnew/3.6.html)
- [Python 3.8 — typing module](https://docs.python.org/3.8/library/typing.html)

## Repository

- **GitHub repository:** `holbertonschool-web_back_end`
- **Directory:** `python_async_comprehension`
- **Language:** Python 3.8
