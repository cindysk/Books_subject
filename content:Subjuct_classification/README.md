
*DDC Text Classification and Summarization Utility*

*Description*

This Python script aims to read and classify text files into different categories according to the Dewey Decimal Classification (DDC) system. It performs the following tasks:

Scan a directory for .txt files.
Identify the main subject of each file.
Select specific sentences from the text for analysis.
Summarize the text using OpenAI's GPT-3.5 Turbo model.
Map the summary to one of the predefined DDC categories.

*Dependencies*

Python 3.x
OpenAI Python package
NLTK (Natural Language Toolkit)
Setup

*API Key*
Make sure you replace the openai.api_key variable value with your own OpenAI API key.


*How to Use*

Clone the repository or download the script.
Place your .txt files in a directory.
Modify the DIR variable in the main() function to point to your directory containing .txt files.
Run the script.
bash
Copy code
python your_script_name.py

*Output*

The script will read each .txt file in the specified directory and perform the following:

Print the filename it is currently reading.
Identify and print the main subject of the file.
Print the DDC category inferred from the summary.

*Functions*

get_ddc_category(text)
Takes a text excerpt, summarizes it using GPT-3.5 Turbo, and identifies its DDC category.

get_important_sentences(text)
Selects and returns specific sentences from the text for summarization and analysis.

find_subject(filepath)
Identifies the main subject keyword in the given file.

read_selected_sentences(filepath)
Prints that it is reading from the specified filepath. (Note: The function currently doesn't perform reading.)

*main()*
The main function that ties all other functions together.


*License*

This project is licensed under the MIT License.