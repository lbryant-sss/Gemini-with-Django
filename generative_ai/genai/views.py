from django.shortcuts import render
import requests
# Create your views here.
#Gemini dependencies
import markdown
import textwrap
import google.generativeai as genai
#Process the api
GEMINI_API_KEY = SECRET_API_KEY
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def index(request):
        response_text = None 
        processed_text = None   
        context = {} 
        if request.method == 'POST':
                user_input = request.POST.get('user_input')

                if user_input:
                        response = model.generate_content(user_input)
                        response_text = response.text
                        processed_text = markdown.markdown(response_text)
                else:
                        response_text = "Please enter a question."
                
                context = {
                        'processed_text':processed_text,
                        'user_prompt': user_input,
                }
        return render(request, 'index.html', context=context)

