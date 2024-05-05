import textwrap
import markdown
import google.generativeai as genai


GEM_API_KEY = 'AIzaSyAduQFWwCkWciqw9HTqNhg-pW9PQqUnSjc'

user_input = input("Ask: ")

genai.configure(api_key=GEM_API_KEY)

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(user_input)

text_content = response.text

# Convert markdown to HTML
html_text = markdown.markdown(text_content)

# Write the HTML output to a file (optional)
with open("output.html", "w") as f:
    f.write(html_text)

# Print the HTML output (optional)
print(html_text)