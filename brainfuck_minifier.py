import sys
if len(sys.argv) < 2:
    print("Usage: python brainfuck_minifier.py <input_file> [output_file]")
    sys.exit(1)
file_path = sys.argv[1]
valid_chars = set(['>', '<', '+', '-', '.', ',', '[', ']','?'])
with open(file_path, 'r') as f:
    code = f.read()
minified_code = ""
for c in code:
    if c in valid_chars:
        minified_code += c

if len(sys.argv) > 2:
    output_path = sys.argv[2]
    with open(output_path, 'w') as f:
        f.write(minified_code)
else:
    print(minified_code)
