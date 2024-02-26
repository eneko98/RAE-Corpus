import json
import re

#You will need to add your own paths

file_path = ''

with open(file_path, 'r', encoding='utf-8') as file:
    dictionary_text = file.read()

def parse_rae_dictionary(text):
    text = re.sub(r'^[A-Z]\n+\w+\s*—\s*\w+\n+', '', text, flags=re.MULTILINE)

    entry_pattern = re.compile(r'->(.*?)(?=->|\Z)', re.DOTALL)

    entries = entry_pattern.findall(text)

    processed_entries = []
    for entry in entries:
        parts = re.split(r'\.\s*\(\d+\)\.', entry)
        entry_data = []

        for part in parts:
            word_metadata_section, *definition_section = re.split(r'\.\s*\d+\.\s*', part.strip(), maxsplit=1)
            word, *metadata = re.split(r'\s*\(|\)\s*', word_metadata_section.strip())

            definition_section = '.'.join(definition_section)
            cleaned_definitions = [d.strip() for d in re.split(r'\.\s*\d+\.\s*', definition_section) if d.strip()]

            if not cleaned_definitions and any("V." in md for md in metadata):
                cleaned_definitions = [md for md in metadata if "V." in md]
                metadata = [md for md in metadata if "V." not in md]

            if word or metadata or cleaned_definitions:
                entry_data.append({
                    'word': word,
                    'metadata': metadata,
                    'definitions': cleaned_definitions
                })

        if entry_data:
            processed_entries.append(entry_data)

    return processed_entries

parsed_data = parse_rae_dictionary(dictionary_text)

with open('', 'w', encoding='utf-8') as json_file:
    json.dump(parsed_data, json_file, ensure_ascii=False, indent=4)