@echo off
REM Batch script to checkout gh-pages, convert .md to .html, and push to gh-pages branch

REM 1. Checkout or create gh-pages branch
git checkout gh-pages 2>NUL || git checkout -b gh-pages

REM 2. Activate venv and run main.py to convert .md files to .html
call venv\Scripts\activate
python main.py

REM 3. Add and commit generated .html files
REM Add all .html files from root and subdirectories
git add -f ./*.html */*.html

git commit -m "Update HTML files from Markdown" || echo No changes to commit

REM 4. Push to gh-pages branch
git push origin gh-pages

echo Done!