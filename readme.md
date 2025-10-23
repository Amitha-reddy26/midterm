# Project Documentation for the Calculator

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
  - [Design Patterns](#design-patterns)
  - [Logging Strategy](#logging-strategy)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [License](#license)

## Overview

This calculator project is an advanced Python application designed to perform various mathematical operations. It features dynamic plugin integration, allowing for extensibility and flexibility in adding new operations without modifying the core code.

## Features

- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Dynamic plugin system for adding new operations
- Comprehensive logging for debugging and tracking operations

## Architecture

### Design Patterns

The project implements several design patterns to enhance maintainability and scalability:

1. **Strategy Pattern**: 
   - This pattern is used for defining a family of algorithms (operations in this case), encapsulating each one, and making them interchangeable. The calculator can easily switch between different operations without changing its core functionality.
   - **Impact**: This allows for the addition of new operations (plugins) without modifying existing code, thus adhering to the Open/Closed Principle.

2. **Singleton Pattern**: 
   - Used for the logger class, ensuring that only one instance of the logger is created and used throughout the application.
   - **Impact**: This reduces memory usage and centralizes logging functionality, making it easier to manage and maintain logs.

### Logging Strategy

The logging strategy employs Python's built-in logging module to provide insights into the application’s operation. 

- **Implementation**:
  - The logger is configured to log messages at various levels (DEBUG, INFO, WARNING, ERROR, CRITICAL).
  - Logs are written to a file for persistence, allowing for historical tracking of calculations and potential issues.

- **Impact**:
  - This provides a clear audit trail for debugging and analysis, improving the maintainability of the code and the user experience.

## Setup Instructions

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Amitha-reddy26/midterm.git
   cd Midterm-Project
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```


## Usage
Once the application is running, use the calculator as follows:

### Basic Operations:
- The calculator supports basic operations: addition, subtraction, multiplication, and division.
- Input numbers and choose the desired operation by following the prompts in the terminal.

### Using the Command-Line Interface:
- After launching the application, a menu of available operations will pop up. Follow the on-screen instructions to enter the numbers and select the desired operation.

### Adding New Operations via Plugins:
- If new plugins were developed and included, load them dynamically when the application starts now.
- For instance, if you have a plugin for calculating the power of a number, input the numbers and select the power operation from the menu.

### Example Usage:
Here’s a brief walkthrough of how to perform a calculation:
1. Start the application by running `python main.py`.
2. Enter `1` for addition.
3. Input `5` and `3` when prompted.
4. The calculator will return the result: `8`.

### Error Handling:
- If an invalid input is entered (e.g., letters instead of numbers), the calculator will prompt you to enter valid numbers, demonstrating its robust error handling.


## Design Patterns Implementation
In this project, I utilized the **Factory Design Pattern** to manage the creation of different operation classes (add, subtract, multiply, divide). This allows for easy scalability if more operations need to be added in the future.

**Link to Implementation**: [Factory Design Pattern Implementation](https://refactoring.guru/design-patterns/factory-method)


## Environment Variables Usage
I used environment variables to manage sensitive configurations such as API keys and database URLs. This helps in keeping the code clean and secure. The `dotenv` library was employed to load these variables during the application startup.

**Link to Code**: [Environment Variables Implementation](https://pypi.org/project/python-dotenv/)


## Logging
Logging is implemented using Python's built-in `logging` module. It captures important events and errors that occur during execution, which aids in debugging and monitoring the application’s performance.

**Link to Logging Implementation**: [Logging Implementation](https://docs.python.org/3/library/logging.html)


## Exception Handling
I implemented exception handling using both the "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP) paradigms:

- **LBYL**: Before performing operations that might fail (e.g., division), the code checks if the denominator is zero.
- **EAFP**: In other parts of the code, exceptions are caught and handled gracefully, allowing the program to continue running.

**Link to Exception Handling Implementation**: [Exception Handling Code](https://realpython.com/python-lbyl-vs-eafp/)


## Video Demonstration
A video demonstration of the calculator has been created to showcase its key features and functionalities. 

**Video Link**: [Calculator Demonstration Video](https://youtu.be/Yj-IkdG_cXs)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

