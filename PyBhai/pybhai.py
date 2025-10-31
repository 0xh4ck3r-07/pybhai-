# ============================================================
# 💻 PyBhai - Hindi Style Programming Layer for Python
# Created by Anand Jaiswal
# ============================================================

import sys
import re

# 🔤 Hindi to Python replacements dictionary
replacements = {
    "bol": "print",               # for speaking/output
    "likho": "print",             # synonym for print
    "sun": "input",               # for taking string input
    "sun_int": "int(input())",    # for numeric input
    "agar": "if",                 # condition start
    "warna": "else",              # else condition
    "nahi_to": "else",            # alternate else
    "jab_tak": "while",           # while loop
    "ke_liye": "for",             # for loop
    "mein": "in",                 # in keyword
    "range_tak": "range",         # range()
    "def_kar": "def",             # define function
    "wapas": "return",            # return keyword
    "sach": "True",               # True
    "jhoot": "False",             # False
    "aur": "and",                 # and
    "ya": "or",                   # or
    "barabar": "==",              # ==
    "bada": ">",                  # greater than
    "chhota": "<"                 # less than
}

# 🔄 Translate Hindi-style line into Python
def translate_line(line):
    strings = []
    placeholder_template = '___STRING_PLACEHOLDER_{}___'

    def save_string(match):
        strings.append(match.group(0))
        return placeholder_template.format(len(strings) - 1)

    # Ignore replacements inside quotes
    string_pattern = r'(["\'])(?:(?=(\\?))\2.)*?\1'
    line = re.sub(string_pattern, save_string, line)

    # Replace Hindi keywords
    for hindi, py in replacements.items():
        pattern = r'\b' + re.escape(hindi) + r'\b'
        line = re.sub(pattern, py, line)

    # Put back string literals
    for i, string in enumerate(strings):
        line = line.replace(placeholder_template.format(i), string)

    return line

# 🧩 Run any .pybhai file
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

# 🚀 Auto-run on Replit
if __name__ == "__main__":
    print("════════════════════════════════════════════════════════════")
    print("🧠 PyBhai Interpreter (Replit Auto-Run Mode)")
    print("════════════════════════════════════════════════════════════")
    print("⚙️ Running 'example.pybhai' automatically (no input required)\n")

    run_pybhai_file("example.pybhai")
