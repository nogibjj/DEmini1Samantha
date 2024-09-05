# DEmini1Samantha, from Xiangyu(Sam) Wang DE assignment, 2024

This is the assignments for DE 706, a Python-based project also filled with some python coding iisues in NLP coursces. 


Files required:

    Makefile: Automates common tasks and tests.

    Dockerfile within .devcontainer/

    requirements.txt: all Python dependencies required to run the project.

    CI/CD Pipeline: github actions in .github/workflows/: Contains CI workflow files tasks on Github

    .devcontainer/: Contains configuration for setting up a consistent development environment

    README.md: The main documentation file for the project.

Besides: 
    # env and IDE
    .venv/: Virtual environment folder for isolating Python dependencies.
    .vscode/: Contains VS Code-specific configuration files.
       
    # main and test
    main.py: The main entry point for running the project.
    test_main.py: Contains test cases for testing the main.py script.
    mylib.py: Contains helper functions and utilities for the project.

    # NLP issues
    bigram.py: Python script for implementing Bigram model logic.
    train_bigram_model.py: Script to train the Bigram language model.
    Unigram.py: Python script for implementing Unigram model logic.



## Installation

To install the project dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/DEmini1Samantha.git
   cd DEMini1Samantha

 2. **To set up a virtual environments**:  
    python -m venv .venv
    source .venv/bin/activate   # On Windows use `.venv\Scripts\activate`

 3. **install denpencey**:  
    pip install --upgrade pip
    pip install -r requirements.txt