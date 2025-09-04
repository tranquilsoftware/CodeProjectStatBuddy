# Code Project Line Counter

A Python tool that counts lines, characters, and files in code projects with an interactive terminal interface.

## What it does

- Counts code files, lines, and characters for different project types
- Supports C++, TypeScript, Python, JavaScript, Java, C#, Go, and Rust projects
- Interactive menu with arrow key navigation
- Smart filtering (skips build directories, cache folders, etc.)

## Usage

1. Run the program:
```bash
python main.py
```

2. Or specify the source directory directly:
```bash
python main.py --src C:/path/to/project_directory/src/
```

3. Enter the number corresponding to your project type
4. Press Enter to confirm selection
5. If no `--src` provided, paste your project directory path when prompted
6. View results

## Requirements

- Python 3.6+
- Works on Windows, macOS, and Linux

## Example Output

```
==================================================
PROJECT STATISTICS
==================================================
Project type: Python Project
File extensions: .py
Code characters: 15,432 characters
Code lines: 542 lines
Code files: 23 files
==================================================
Average lines per file: 23.6
Average characters per line: 28.5
```

## Supported Project Types

| Project Type | File Extensions |
|--------------|----------------|
| C++ | `.h`, `.hpp`, `.cpp`, `.cc`, `.cxx` |
| TypeScript | `.ts`, `.tsx` |
| Python | `.py` |
| JavaScript | `.js`, `.jsx` |
| Java | `.java` |
| C# | `.cs` |
| Go | `.go` |
| Rust | `.rs` |

## License

Tranquil Software; forever free. Feel free to use, modify, and distribute.