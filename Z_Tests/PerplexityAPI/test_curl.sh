#!/bin/bash

# Quick Perplexity API validation with curl
# Make sure your .env file has PERPLEXITY_API_KEY set

echo "🧪 Testing Perplexity API with curl"
echo "=================================="

# Load API key from .env file
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
    echo "✅ Loaded API key from .env file"
else
    echo "❌ .env file not found"
    echo "Please create a .env file with: PERPLEXITY_API_KEY=your_api_key_here"
    exit 1
fi

# Check if API key is set
if [ -z "$PERPLEXITY_API_KEY" ]; then
    echo "❌ PERPLEXITY_API_KEY not found in .env file"
    exit 1
fi

echo "🔑 API Key: ${PERPLEXITY_API_KEY:0:10}..."
echo ""

# Test API with curl
echo "🔄 Testing API connection..."

curl -X POST "https://api.perplexity.ai/v1/chat/completions" \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Hello! What is 2+2? Please keep your answer very brief."
      }
    ],
    "max_tokens": 50
  }' \
  --silent \
  --show-error \
  --fail \
  --write-out "\n📊 HTTP Status: %{http_code}\n⏱️  Response Time: %{time_total}s\n" \
  --output /tmp/perplexity_response.json

# Check if curl was successful
if [ $? -eq 0 ]; then
    echo "✅ API call successful!"
    echo "📝 Response:"
    cat /tmp/perplexity_response.json | python3 -m json.tool 2>/dev/null || cat /tmp/perplexity_response.json
    rm -f /tmp/perplexity_response.json
else
    echo "❌ API call failed"
    echo "Check your API key and internet connection"
fi
