import os
import openai
import nltk
nltk.download('punkt')

# Initialize the OpenAI GPT API (Replace with your own API key)
openai.api_key = "API_KEY"

# DDC (Dewey Decimal Classification) mapping with broader keywords
DDC_Mapping = {
    'Computer science, general works，information': ['Computer science', 'knowledge & systems', 'Magazines', 'journals & serials''Bibliography', 'data'],
    'Philosophy & Psychology': ['philosophy', 'mind', 'ethics'],
    'Religion': ['religion', 'theology', 'faith'],
    'Social Sciences': ['Statistics', 'economics', 'Economics','Public administration & military science', 'Commerce, communications, & transportation',' Customs, etiquette, & folklore', 'politics'],
    'Language': ['language', 'grammar', 'communication'],
    'Natural Sciences & Mathematics': ['math', 'astronomy', 'Physics', 'geology', 'biology', 'chemistry'],
    'Technology': ['Medicine & health', 'Agriculture', 'Management & public relations', 'Chemical engineering', 'Manufacturing', 'engineering', 'Building & construction',  'machinery'],
    'Arts': ['arts', 'music', 'sports'],
    'Literature': ['fiction', 'poetry', 'novel'],
    'History & Geography': ['history', 'geography', 'biography']
}

def get_ddc_category(text):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Summarize the following excerpt and identify its main subject:\n{text}"}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    summary = response['choices'][0]['message']['content'].strip()

    ddc_category = 'Unknown'
    ddc_keyword = 'Unknown'

    for category, keywords in DDC_Mapping.items():
        for keyword in keywords:
            if keyword.lower() in summary.lower():
                ddc_category = category
                ddc_keyword = keyword
                break

        if ddc_keyword != 'Unknown':
            break

    return summary, ddc_keyword  # Return the specific keyword instead of the master category



def get_important_sentences(text):
    paragraphs = text.strip().split('\n\n')
    first_paragraph = paragraphs[0]
    middle_paragraph = paragraphs[len(paragraphs) // 2]
    last_paragraph = paragraphs[-1]

    first_sentences = nltk.sent_tokenize(first_paragraph)[:3]
    middle_sentences = nltk.sent_tokenize(middle_paragraph)[:3]
    last_sentences = nltk.sent_tokenize(last_paragraph)[:3]

    return ' '.join(first_sentences + middle_sentences + last_sentences)

def find_subject(filepath):
    subject_keywords = [ "Computer science", "knowledge & systems", "Magazines", "journals", "serials", "Bibliography", "data",
    "Psychology", "philosophy", "religion", "theology", "faith", "Statistics", "economics", "Economics","Public administration",
    "military science", "Commerce", "communications", "transportation", "Customs", "etiquette", "folklore", "politics",
    "language", "grammar", "communication", "math", "astronomy", "Physics", "geology", "biology", "chemistry", "Medicine & health",
    "Agriculture", "Management", "public relations", "Chemical engineering", "Manufacturing", "engineering", "Building & construction",
    "machinery", "Architecture", "Sculpture", " Graphic arts", "Painting", "Photography", "computer art", "games", "entertainment",
    "music", "sports", "fiction", "poetry", "novel", "history", "geography", "biography", "autobiography"]
    subject = 'Unknown'
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip().lower()
            for keyword in subject_keywords:
                if keyword in line:
                    subject = keyword
                    return subject
    return subject

# in your main function

def read_selected_sentences(filepath):
    print(f"Reading from {filepath}")

def main():
    DIR = "YOUR_DIR"  # Set your directory path
    start_reading = False

    print("Inside main. Checking directory:", DIR)

    for filename in sorted(os.listdir(DIR)):
        print(f"Found file: {filename}")
        if filename == "full-bodied-wine-a-vintage-murder.epub.txt":
            print("Starting to read files.")
            start_reading = True

        if start_reading and filename.endswith('.txt'):
            filepath = os.path.join(DIR, filename)
            print(f"Reading {filepath}")

            subject = find_subject(filepath)
            selected_sentences = read_selected_sentences(filepath)
            summary, ddc_category = get_ddc_category(selected_sentences)

            print(f"File: {filename}")
            print(f"Identified Subject: {subject}")
            print(f"DDC Category: {ddc_category}")


if __name__ == '__main__':
    main()
