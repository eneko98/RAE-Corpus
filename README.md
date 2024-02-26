# RAE Spanish Dictionary Corpus

This repository houses a corpus derived from the Real Academia Española's "Diccionario de la Lengua Española", based on the comprehensive resources available at [https://dle.rae.es/](https://dle.rae.es/). It features the original text file of the dictionary, a Python script for parsing the text, and the resulting corpus in JSON format. Each entry in the corpus contains the word, various metadata that can be useful for fine-tuning, and one or more definitions, making this corpus a robust resource for various computational linguistics and machine learning tasks, especially for those focused on the Spanish language. With a total of 85,811 words, the corpus is extensive and detailed, facilitating a wide range of research and application possibilities.

## Contents

- `RealAcademiaEspanola-DiccionarioLlenguaEspanola.txt` - The original text file of the "Diccionario de la Lengua Española" by the Real Academia Española (RAE).
- `data_parser.py` - A Python script utilized to extract information from the original text file and format it into a structured JSON corpus. This script processes each entry to include the word, its relevant metadata, and definitions in the JSON format.
- `rae_dictionary.json` - The JSON format corpus generated from the original dictionary text, encapsulating the extensive vocabulary of the Spanish language as documented by the RAE. The corpus includes detailed entries for each word, incorporating metadata and definitions to support a variety of NLP tasks.

## Getting Started

To utilize this repository, Python is required. The provided `data_parser.py` script, written in Python, processes the original dictionary text file, generating a structured JSON corpus.

### Prerequisites

- Python 3.x
- Standard Python libraries (`json`, `re`) are used in the script. No external libraries are required.

### Usage

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/eneko98/RAE-Corpus.git
    ```

2. Navigate to the repository directory:
    ```
    cd RAE-Corpus
    ```

3. Modify the `data_parser.py` script to include the correct file paths for your system. This involves setting the path to the `RealAcademiaEspanola-DiccionarioLlenguaEspanola.txt` file and specifying the output path for the `rae_dictionary.json` file.
4. Run the `data_parser.py` script to parse the RAE dictionary text file and generate the JSON corpus:
    ```
    python data_parser.py
    ```

## Contributing

Contributions to the RAE Spanish Dictionary Corpus are welcome! Please feel free to fork the repository, make changes, and submit pull requests.

## Acknowledgments

- This project was inspired by the "Diccionario de la Lengua Española" by the Real Academia Española (RAE), available at [https://dle.rae.es/](https://dle.rae.es/).
