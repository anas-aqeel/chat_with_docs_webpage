from read_webpage import read_webpage
from createFile import create_file
from filterLinks import filterLinks
from savedata import save_text_to_md_file
from get_vectorstore import get_vectorstore
from dataSplitter import split_file_data

links = set()
markdowns = []
html_url = input("Enter the path to your HTML file or provide a URL: ")
output_filename = input("Enter the output filename: ")

print("Reading HTMl Files...")
read_webpage(html_url, links, markdowns)

print(f"Creating '{output_filename}'...")
create_file(output_filename)

print("Filtering links...")
validLinks = filterLinks(links)

print(f"Saving data to '{output_filename}'...")
save_text_to_md_file("""
""".join(markdowns), output_filename)

print("Splitting data into chunks...")
chunks = split_file_data(output_filename)

vectorStore = get_vectorstore(chunks=chunks)

