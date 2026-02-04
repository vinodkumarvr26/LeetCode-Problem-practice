""".handle_comment(data)
This method is called when a comment is encountered (e.g. <!--comment-->).
The data argument is the content inside the comment tag:
from html.parser import HTMLParserr
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
          print("Comment  :", data)
.handle_data(data)
This method is called to process arbitrary data (e.g. text nodes and the content of <script>...</script> and <style>...</style>).
The data argument is the text content of HTML.
from html.parser import HTMLParserr
class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        print("Data     :", data)
Task
You are given an HTML code snippet of  lines.
Your task is to print the single-line comments, multi-line comments and the data."""
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if data.strip().startswith('[if]') or '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)
    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)
parser=MyHTMLParser()       
n=int(input())
html=""   
for _ in range(n):
    html += input()+"\n"
parser.feed(html)