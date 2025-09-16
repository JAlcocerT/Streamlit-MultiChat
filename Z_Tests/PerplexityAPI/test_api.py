#!/usr/bin/env python3
"""
Simple test script for Perplexity API
This helps debug API connection issues
"""

import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_perplexity_api():
    """Test basic Perplexity API connection"""
    
    api_key = os.getenv('PERPLEXITY_API_KEY')
    if not api_key:
        print("❌ PERPLEXITY_API_KEY not found in environment variables")
        print("Please set your API key:")
        print("export PERPLEXITY_API_KEY='your_api_key_here'")
        return False
    
    print(f"✅ API Key found: {api_key[:10]}...")
    
    # Test API endpoint
    url = "https://api.perplexity.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Simple test payload
    payload = {
        "model": "sonar",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Hello! Can you tell me what 2+2 equals?"
            }
        ],
        "max_tokens": 100
    }
    
    print("🔄 Testing API connection...")
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        print(f"📊 Response Status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("✅ API connection successful!")
            print(f"📝 Response: {result['choices'][0]['message']['content']}")
            return True
        else:
            print(f"❌ API Error: {response.status_code}")
            print(f"📄 Error details: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Perplexity API Test")
    print("=" * 30)
    test_perplexity_api()
