#find <input_folder> -type f -exec md5sum {} + > <output.txt>
import argparse

parser = argparse.ArgumentParser(description="Remove the second column from each record in a text file.")
parser.add_argument('-i', '--input', type=str, required=True, help="Input file path")
parser.add_argument('-o', '--output', type=str, required=True, help="Output file path")
args = parser.parse_args()

with open(args.input, 'r') as input_file, open(args.output, 'w') as output_file:
    for line in input_file:
        parts = line.split()
        if len(parts) > 0:
            output_file.write(parts[0] + '\n')

print(f"Removed path to each file and saved as {args.output}")
