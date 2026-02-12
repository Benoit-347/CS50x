import os
import requests
import json

# AI generated code via gemmini

# 1. SETUP: Define your API Key and Endpoint
# Ideally, retrieve this from environment variables for security.
# You can also paste it directly here as a string, but be careful sharing the code.
API_KEY = os.environ.get("GROQ_API_KEY") 
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "qwen-2.5-coder-32b"  # Change this to "qwen-3-coder" if/when available

def run_qwen_coder(user_prompt):
    """
    Sends a prompt to the Groq API and prints the response.
    """
    
    # 2. HEADERS: The 'ID Card' for your request
    # This tells Groq who you are (Authorization) and what you are sending (JSON).
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # 3. PAYLOAD: The data package we are sending
    # We structure this exactly how the API expects it (OpenAI-compatible format).
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system", 
                "content": "You are an expert Python programmer. Write clean, efficient code."
            },
            {
                "role": "user", 
                "content": user_prompt
            }
        ],
        "temperature": 0.1,  # Low temperature = more precise/deterministic for coding
        "max_tokens": 1024   # Limits the response size to save efficiency
    }

    # 4. REQUEST: Sending the letter
    # We use 'POST' because we are sending data to the server.
    try:
        response = requests.post(
            API_URL, 
            headers=headers, 
            json=payload
        )
        
        # 5. HANDLING RESPONSE: Check if it worked
        response.raise_for_status()  # Raises an error if the status code is bad (like 401 or 500)
        
        # Parse the JSON response to get the actual text
        data = response.json()
        content = data['choices'][0]['message']['content']
        
        return content

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# --- Main Execution ---
if __name__ == "__main__":
    # Check if key is present
    if not API_KEY:
        print("Error: GROQ_API_KEY not found in environment variables.")
    else:
        # Example Prompt
        my_request = "Write a Python function to calculate the Fibonacci sequence."
        print(f"Asking {MODEL}...\n")
        
        result = run_qwen_coder(my_request)
        
        print("--- Response ---")
        print(result)