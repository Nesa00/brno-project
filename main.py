import markdown2
import sys
import os
from jinja2 import Environment, FileSystemLoader

class Converter:
    def __init__(self, template_name='template.html'):
        template_dir = os.path.join(os.path.dirname(__file__), 'templates')
        self.env = Environment(loader=FileSystemLoader(template_dir))
        self.template = self.env.get_template(template_name)

    def md_to_html(self, md_file_path, html_file_path):
        with open(md_file_path, 'r', encoding='utf-8') as md_file:
            md_content = md_file.read()
        html_content = markdown2.markdown(md_content, extras=["fenced-code-blocks", "tables", "cuddled-lists", "metadata", "code-friendly", "footnotes"])
        rendered = self.template.render(content=html_content)
        with open(html_file_path, 'w', encoding='utf-8') as html_file:
            html_file.write(rendered)

    def convert_all_md_in_dir(self, directory='.'):
        output_dir = os.path.join(directory, 'pages')
        os.makedirs(output_dir, exist_ok=True)
        for filename in os.listdir(directory):
            if filename.lower().endswith('.md'):
                base = os.path.splitext(filename)[0]
                html_file = base + '.html'
                html_path = os.path.join(output_dir, html_file)
                print(f"Converting {filename} -> pages/{html_file}")
                self.md_to_html(os.path.join(directory, filename), html_path)

if __name__ == "__main__":
    converter = Converter()
    if len(sys.argv) == 3:
        converter.md_to_html(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        arg = sys.argv[1]
        if os.path.isdir(arg):
            converter.convert_all_md_in_dir(arg)
        elif os.path.isfile(arg) and arg.lower().endswith('.md'):
            base = os.path.splitext(arg)[0]
            html_file = base + '.html'
            converter.md_to_html(arg, html_file)
        else:
            print(f"Error: {arg} is not a directory or a .md file.")
    else:
        converter.convert_all_md_in_dir()