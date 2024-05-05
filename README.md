# Mini-Generative AI Website with Django

This project is a mini-generative AI website built using Django framework. It utilizes the Gemini AI API for generating text-based content. The purpose of this project is for educational purposes, demonstrating how to integrate AI APIs into web applications.

## Features

- Generate text-based content using Gemini AI API.
- Simple and intuitive web interface.
- Easy to deploy and customize.

## Requirements

- Python 3.x
- Django
- Requests library (for API requests)
- Gemini AI API key (sign up [here](https://gemini.ai/))

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/lbryant-sss/Gemini-with-Django/.git
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Set up your Gemini AI API key:

   - Sign up for an account on [Gemini AI](https://gemini.ai/).
   - Copy your API key.
   - Create a `.env` file in the root directory of the project.
   - Add your API key to the `.env` file:

     ```
     GEMINI_API_KEY=your_api_key_here
     ```

## Usage

1. Run the Django server:

   ```
   python manage.py runserver
   ```

2. Access the website at `http://localhost:8000` in your web browser.

3. Enter the desired text prompt and click "Enter" to generate AI-generated text.

## It currently shows text. It will be updated to show code and other html content properly in future.

## License

This project is licensed under the [MIT License](LICENSE).

---


