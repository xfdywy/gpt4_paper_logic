import re
import argparse

def remove_comments(tex_content):
    """
    Remove comments from LaTeX content.
    
    :param tex_content: str, content of the LaTeX file
    :return: str, content with comments removed
    """
    # Regular expression to match comments
    pattern = re.compile(r'(?<!\\)%.*')
    
    # Remove comments
    cleaned_content = re.sub(pattern, '', tex_content)
    
    return cleaned_content

def remove_citations(tex_content):
    """
    Remove citations  from LaTeX content.
    
    :param tex_content: str, content of the LaTeX file
    :return: str, content with citations removed
    """
    # Regular expression to match citations
    pattern = re.compile(r'\\cite[tp]?{.*?}')
    
    # Remove citations
    cleaned_content = re.sub(pattern, '', tex_content)
    
    return cleaned_content

def limit_consecutive_newlines(tex_content, max_newlines=2):
    """
    Limit consecutive newlines in LaTeX content to a specified maximum.
    
    :param tex_content: str, content of the LaTeX file
    :param max_newlines: int, maximum number of consecutive newlines to keep
    :return: str, content with limited consecutive newlines
    """
    # Regular expression to match more than max_newlines consecutive newlines
    pattern = re.compile(r'\n{'+str(max_newlines+1)+',}')
    
    # Replace with max_newlines consecutive newlines
    limited_content = re.sub(pattern, '\n' * max_newlines, tex_content)
    
    return limited_content

def remove_appendix(tex_content):
    """
    Remove content after \appendix in LaTeX file.
    
    :param tex_content: str, content of the LaTeX file
    :return: str, content up to \appendix
    """
    # Regular expression to find \appendix
    pattern = re.compile(r'\\appendix')
    
    # Find the position of \appendix
    match = pattern.search(tex_content)
    if match:
        # Return content up to \appendix
        return tex_content[:match.start()]
    else:
        return tex_content

def process_tex_file(input_filename, output_filename):
    """
    Read a LaTeX file, remove comments, citations, limit consecutive newlines,
    and write the cleaned content to a new file.
    
    :param input_filename: str, name of the input LaTeX file
    :param output_filename: str, name of the output LaTeX file
    """
    # Read the content of the input file
    with open(input_filename, 'r', encoding='utf-8') as file:
        tex_content = file.read()
    
    # Remove comments from the content
    cleaned_content = remove_comments(tex_content)
    
    # Remove citations from the content
    cleaned_content = remove_citations(cleaned_content)
    
    # Limit consecutive newlines in the content
    limited_content = limit_consecutive_newlines(cleaned_content)
    
    # Remove content after \appendix
    final_content = remove_appendix(limited_content)
    
    # Write the cleaned content to the output file
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(final_content)

# Argument parser
argparser = argparse.ArgumentParser()
argparser.add_argument('--input', type=str, default='input.tex', help='Input LaTeX file')
argparser.add_argument('--output', type=str, default='output.tex', help='Output LaTeX file')

args = argparser.parse_args()

input_filename = args.input
output_filename =  args.output
process_tex_file(input_filename, output_filename)
