# PyBhai - A Hindi style programming layer built on Python
# Created by Anand

import sys

# Dictionary of Hindi words to Python equivalents
replacements = {
    "likho": "print",
    "agar": "if",
    "nahi_to": "else",
    "jab_tak": "while",
    "ke_liye": "for",
    "mein": "in",
    "range_tak": "range",
    "def_kar": "def",
    "wapas": "return",
    "sach": "True",
    "jhoot": "False",
    "aur": "and",
    "ya": "or",
    "barabar": "==",
    "bada": ">",
    "chhota": "<"
}


def translate_line(line):
    """Replace Hindi words with Python equivalents, preserving strings"""
    import re

    strings = []
    placeholder_template = '___STRING_PLACEHOLDER_{}___'

    def save_string(match):
        strings.append(match.group(0))
        return placeholder_template.format(len(strings) - 1)

    string_pattern = r'(["\'])(?:(?=(\\?))\2.)*?\1'
    line = re.sub(string_pattern, save_string, line)

    for hindi, py in replacements.items():
        pattern = r'\b' + re.escape(hindi) + r'\b'
        line = re.sub(pattern, py, line)

    for i, string in enumerate(strings):
        line = line.replace(placeholder_template.format(i), string)

    return line


def run_pybhai_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            code = f.readlines()

        translated = [translate_line(line) for line in code]
        exec("".join(translated))
    except FileNotFoundError:
        print("❌ File nahi mili bhai:", file_name)
    except Exception as e:
        print("⚠️ Error aaya bhai:", e)


# ========================
# Replit Auto Run Version
# ========================
if __name__ == "__main__":
    print("════════════════════════════════════════════════════════════")
    print("🧠 PyBhai Interpreter (Replit Auto-Run Mode)")
    print("════════════════════════════════════════════════════════════")
    print("⚙️ Running 'example.pybhai' automatically (no input required)\n")

    run_pybhai_file("example.pybhai")
