
import markdown2
import sys
import os

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Markdown Preview</title>
	<style>
		body {{ font-family: 'Segoe UI', 'Helvetica Neue', Arial, 'Liberation Sans', sans-serif; background: #f8f8f8; color: #222; margin: 0; padding: 2em; }}
		.markdown-body {{
			background: #fff;
			max-width: 794px; /* A4 width in px at 96dpi */
			margin: 2em auto;
			padding: 2em 2.5em;
			box-shadow: 0 2px 16px rgba(0,0,0,0.08);
			border-radius: 8px;
		}}
		h1, h2, h3, h4, h5, h6 {{ color: #2c3e50; }}
		pre, code {{ background: #f4f4f4; border-radius: 4px; padding: 2px 6px; font-size: 1em; }}
		pre {{ padding: 1em; overflow-x: auto; }}
		blockquote {{ border-left: 4px solid #b4b4b4; margin: 1em 0; padding: 0.5em 1em; color: #555; background: #fafafa; }}
		table {{
			border-collapse: collapse;
			
			width: 100%;
			overflow-x: auto;
			max-width: 100%;
			margin: auto;
		}}
		th, td {{
			border: 1px solid #ddd;
			padding: 0.5em 1em;
			box-sizing: border-box;
			word-break: break-word;
		}}
		th {{ background: #eee; }}
		iframe {{
			max-width: 100%;
			width: 100%;
			display: block;
		}}
		a {{ color: #007acc; text-decoration: none; }}
		a:hover {{ text-decoration: underline; }}
		ul, ol {{ margin: 1em 0 1em 2em; }}
		img {{ max-width: 100%; height: auto; }}
		@media print {{
			body {{ background: #fff !important; padding: 0; }}
			.markdown-body {{
				box-shadow: none !important;
				border-radius: 0 !important;
				margin: 0 auto !important;
				padding: 0.5in 0.7in !important;
				max-width: 100% !important;
				width: 210mm !important; /* A4 width */
				min-height: 297mm !important; /* A4 height */
			}}
			@page {{
				size: A4;
				margin: 0;
			}}
		}}
	</style>
</head>
<body>
	<div class="markdown-body">
		{content}
	</div>
</body>
</html>
'''

def md_to_html(md_file_path, html_file_path):
	with open(md_file_path, 'r', encoding='utf-8') as md_file:
		md_content = md_file.read()
	html_content = markdown2.markdown(md_content, extras=["fenced-code-blocks", "tables", "cuddled-lists", "metadata", "code-friendly", "footnotes"])
	full_html = HTML_TEMPLATE.format(content=html_content)
	with open(html_file_path, 'w', encoding='utf-8') as html_file:
		html_file.write(full_html)

def convert_all_md_in_dir(directory):
	# Ensure output directory exists
	output_dir = os.path.join(directory, 'pages')
	os.makedirs(output_dir, exist_ok=True)
	for filename in os.listdir(directory):
		if filename.lower().endswith('.md'):
			base = os.path.splitext(filename)[0]
			html_file = base + '.html'
			html_path = os.path.join(output_dir, html_file)
			print(f"Converting {filename} -> pages/{html_file}")
			md_to_html(os.path.join(directory, filename), html_path)

if __name__ == "__main__":
	if len(sys.argv) == 3:
		md_to_html(sys.argv[1], sys.argv[2])
	elif len(sys.argv) == 2:
		arg = sys.argv[1]
		if os.path.isdir(arg):
			convert_all_md_in_dir(arg)
		elif os.path.isfile(arg) and arg.lower().endswith('.md'):
			base = os.path.splitext(arg)[0]
			html_file = base + '.html'
			md_to_html(arg, html_file)
		else:
			print(f"Error: {arg} is not a directory or a .md file.")
	else:
		convert_all_md_in_dir(os.getcwd())
