import google.generativeai as genai
genai.configure(api_key="AIzaSyCOVKm5Fy-7Xm8aDP7YWjjlGdCGYJLJ_BI")
  

def get_gemini_response(prompt):
    model=genai.GenerativeModel("gemini-2.0-flash")
    response=model.generate_content(prompt)
    return response.text


