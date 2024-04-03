import re
import json

"""This is a new version of the code to match the structure of the English and Basque corpora.
The code extracts the POS tags from the definitions, 
taking into account each definition can have a different POS tag, 
then it deletes it from it."""

def parse_rae_dictionary(text):
    pos_tags = ['f', 'adv', 'prep', 'pref', 'suf', 'adj', 'interj', 'tr', 'prnl', 'm', 'v']
    pos_pattern = r'\b(' + '|'.join(pos_tags) + r')\.'

    entries = re.findall(r'->(.*?)(?=->|\Z)', text, re.DOTALL)
    processed_entries = []

    for entry in entries:
        parts = re.split(r'\.\s*\(\d+\)\.', entry)
        
        for part in parts:
            word_metadata_section, *definition_sections = re.split(r'\.\s*\d+\.\s*', part.strip(), maxsplit=1)
            word, *metadata = re.split(r'\s*\(|\)\s*', word_metadata_section.strip())
            definition_sections = '.'.join(definition_sections)
            definitions = [definition.strip() for definition in re.split(r'\.\s*\d+\.\s*', definition_sections) if definition.strip()]
            
            pos_tags_found = set()
            cleaned_definitions = []

            for definition in definitions:
                pos_matches = set(re.findall(pos_pattern, definition))
                pos_tags_found.update(pos_matches)

                for pos_tag in pos_matches:
                    definition = re.sub(r'\b' + re.escape(pos_tag) + r'\.\s*', '', definition)
                cleaned_definitions.append(definition.strip())

            pos = ", ".join(sorted(pos_tags_found)) if pos_tags_found else ""

            processed_entry = {
                'word': word,
                'metadata': metadata,
                'pos': pos,
                'definitions': cleaned_definitions
            }
            
            processed_entries.append(processed_entry)

    return processed_entries

# You may need to add your own paths
input_file_path = ''
output_file_path = ''

with open(input_file_path, 'r', encoding='utf-8') as file:
    dictionary_text = file.read()

parsed_data = parse_rae_dictionary(dictionary_text)

with open(output_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(parsed_data, json_file, ensure_ascii=False, indent=4)
