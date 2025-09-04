#!/usr/bin/env python3
import os
import sys
import argparse
from pathlib import Path
from config import EXCLUDE_DIRS


class CodeCounter:
    def __init__(self):
        self.project_types = [
            {"name":    "C++ Project",         "extensions": [".h", ".hpp", ".cpp", ".cc", ".cxx"]},
            {"name":    "TypeScript Project",  "extensions": [".ts", ".tsx"]},
            {"name":    "Python Project",      "extensions": [".py"]},
            {"name":    "JavaScript Project",  "extensions": [".js", ".jsx"]},
            {"name":    "Java Project",        "extensions": [".java"]},
            {"name":    "C# Project",          "extensions": [".cs"]},
            {"name":    "Go Project",          "extensions": [".go"]},
            {"name":    "Rust Project",        "extensions": [".rs"]},
        ]
        self.selected_index = 0

    def display_menu(self):
        print("\n" + "="*50)
        print("CODE PROJECT STATISTICS BUDDY")
        print("="*50)
        print("Select project type:")
        print()
        
        for i, project_type in enumerate(self.project_types, 1):
            extensions = ", ".join(project_type['extensions'])
            print(f"[{i}] {project_type['name']} (checks {extensions} files)")
        
        print(f"[{len(self.project_types) + 1}] Quit")
        print()

    def select_project_type(self):
        while True:
            self.display_menu()
            try:
                choice = input("Enter your choice (number): ").strip()
                
                if not choice.isdigit():
                    print("Please enter a valid number.")
                    continue
                
                choice_num = int(choice)
                
                if choice_num == len(self.project_types) + 1:
                    return None  # Quit
                elif 1 <= choice_num <= len(self.project_types):
                    selected = self.project_types[choice_num - 1]
                    self.selected_index = choice_num - 1
                    return selected
                else:
                    print(f"Please enter a number between 1 and {len(self.project_types) + 1}.")
                    
            except KeyboardInterrupt:
                print("\nGoodbye!")
                return None
            except ValueError:
                print("Please enter a valid number.")

    def get_directory_path(self, provided_path=None):
        if provided_path:
            # Validate provided path
            path = Path(provided_path.strip().strip('"\''))
            if path.exists() and path.is_dir():
                return path
            else:
                print(f"Error: Directory '{provided_path}' not found.")
                return None
        
        print("\nSelected project type:", self.project_types[self.selected_index]['name'])
        print("\nEnter the directory path to analyze:")
        print("(You can copy and paste the path)")
        
        while True:
            try:
                path = input("Directory path: ").strip()
                if not path:
                    print("Please enter a valid path.")
                    continue
                
                # Remove quotes if present (common when copying paths)
                path = path.strip('"\'')
                
                if os.path.exists(path) and os.path.isdir(path):
                    return Path(path)
                else:
                    print("Directory not found. Please enter a valid directory path.")
            except KeyboardInterrupt:
                print("\nOperation cancelled.")
                return None

    def count_files_and_lines(self, directory, extensions):
        total_files = 0
        total_lines = 0
        total_characters = 0

        print(f"\nAnalyzing directory: {directory}")
        print("Processing files...")
        
        try:
            for root, dirs, files in os.walk(directory):
                # Skip directories in EXCLUDE_DIRS and hidden directories
                dirs[:] = [d for d in dirs if not d.startswith('.') and d not in EXCLUDE_DIRS]
                
                for file in files:
                    if any(file.lower().endswith(ext.lower()) for ext in extensions):
                        file_path = Path(root) / file
                        try:
                            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                                content = f.read()
                                lines = content.count('\n') + (1 if content and not content.endswith('\n') else 0)
                                total_lines += lines
                                total_characters += len(content)
                                total_files += 1
                                
                        except (IOError, OSError) as e:
                            print(f"Warning: Could not read {file_path}: {e}")
                            
        except Exception as e:
            print(f"Error analyzing directory: {e}")
            return None, None, None
            
        return total_files, total_lines, total_characters

    def display_results(self, files, lines, characters, project_type):
        print("\n" + "="*50)
        print("PROJECT STATISTICS")
        print("="*50)
        print(f"Project type: {project_type['name']}")
        print(f"File extensions: {', '.join(project_type['extensions'])}")
        print(f"Code characters: {characters:,} characters")
        print(f"Code lines: {lines:,} lines")
        print(f"Code files: {files:,} files")
        print("="*50)
        
        if files > 0:
            avg_lines_per_file = lines / files
            avg_chars_per_line = characters / lines if lines > 0 else 0
            print(f"Average lines per file: {avg_lines_per_file:.1f}")
            print(f"Average characters per line: {avg_chars_per_line:.1f}")

    def run(self):
        # Parse command line arguments
        parser = argparse.ArgumentParser(description='Count lines and files in code projects')
        parser.add_argument('--src', type=str, help='Source directory path to analyze')
        args = parser.parse_args()
        
        try:
            # Select project type with numbered menu
            selected_project = self.select_project_type()
            
            if selected_project is None:
                print("Goodbye!")
                return
            
            # Get directory path (from argument or user input)
            directory = self.get_directory_path(args.src)
            if directory is None:
                return
            
            # Count files and lines
            files, lines, characters = self.count_files_and_lines(
                directory, selected_project['extensions']
            )
            
            if files is not None:
                self.display_results(files, lines, characters, selected_project)
            else:
                print("Analysis failed.")
                
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    counter = CodeCounter()
    counter.run()