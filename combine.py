import os
import yaml

def combine_markdown_files(input_dir, output_file, lines_to_strip=100):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for filename in sorted(os.listdir(input_dir)):
            if filename.endswith('.md'):
                filepath = os.path.join(input_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as infile:
                    lines = infile.readlines()
                    if len(lines) > lines_to_strip:
                        content_lines = lines[lines_to_strip:]
                        content = ''.join(content_lines)
                    else:
                        content = ''.join(lines) #if less than 100 lines, keep all.

                    frontmatter = {
                        'original_filename': filename,
                    }
                    outfile.write('---\n')
                    yaml.dump(frontmatter, outfile, default_flow_style=False)
                    outfile.write('---\n\n')
                    outfile.write(content)
                    outfile.write('\n\n')

input_directory = 'markdown_files'
output_filename = 'qb64-wiki.md'
lines_to_remove = 100 #set number of lines to remove.

combine_markdown_files(input_directory, output_filename, lines_to_remove)