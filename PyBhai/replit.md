# PyBhai - Hindi/Hinglish Programming Language

## Overview
PyBhai is a Python-based programming language that uses Hindi/Hinglish keywords instead of English. It transpiles PyBhai code to Python and executes it.

## Purpose
- Make programming more accessible to Hindi speakers
- Provide a fun, localized coding experience
- Learn programming concepts in a familiar language

## Current State
- Basic interpreter created that transpiles PyBhai to Python
- Supports common keywords like likho (print), agar (if), nahi_to (else), and comparison operators

## Project Structure
- `pybhai.py` - Main interpreter/transpiler
- `example.pybhai` - Example PyBhai program
- `.pybhai` files - PyBhai source code files

## How to Use

### Method 1: Interactive Mode (File Prompt)
Run in Shell to get interactive file input:
```bash
python pybhai.py
```
Then enter file names when prompted (e.g., `example.pybhai`). Type `nikal` or `exit` to quit.

### Method 2: Direct File Execution
Run with a specific file:
```bash
python pybhai.py example.pybhai
```

## Supported Keywords
- `likho()` → print()
- `agar` → if
- `nahi_to` → else
- `jab_tak` → while
- `ke_liye` → for
- `mein` → in
- `range_tak` → range
- `def_kar` → def
- `wapas` → return
- `sach` → True
- `jhoot` → False
- `aur` → and
- `ya` → or
- `barabar` → ==
- `bada` → >
- `chhota` → <

## Recent Changes
- Created PyBhai interpreter (October 31, 2025)
- Added support for basic control flow and operators
- Created example.pybhai with user's sample code
