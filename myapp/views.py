
import os
os.environ['TF_USE_LEGACY_KERAS'] = '1'  # Force use of tf-keras

from django.shortcuts import render
from django.http import JsonResponse
from transformers import pipeline

# Load a pre-trained model (e.g., text generation)
generator = pipeline('text-generation', model='gpt2')

def ai_chat(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')

        # Generate a response using the AI model
        ai_response = generator(user_input, max_length=50, num_return_sequences=1)

        return JsonResponse({'response': ai_response[0]['generated_text']})
    return render(request, 'myapp/index.html')

def home(request):
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')