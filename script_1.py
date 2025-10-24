
# Create directory structure placeholder files
import os

# Create .gitkeep files for empty directories
gitkeep_dirs = ['data/raw', 'data/processed', 'results', 'models', 'notebooks']

gitkeep_structure = {}

for dir_path in gitkeep_dirs:
    gitkeep_structure[f"{dir_path}/.gitkeep"] = "# This file ensures the directory is tracked by Git\n"

# Create LICENSE file (MIT License)
license_content = '''MIT License

Copyright (c) 2025 Rahul Singh Kushwah

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

with open('LICENSE', 'w') as f:
    f.write(license_content)

print("✅ LICENSE created successfully!")
print(f"\nDirectory structure that should be created:")
for dir_path in gitkeep_dirs:
    print(f"  📁 {dir_path}/")
