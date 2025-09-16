# Quick API Validation Commands

## 🚀 One-liner curl test (replace YOUR_API_KEY):

```bash
curl -X POST "https://api.perplexity.ai/v1/chat/completions" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"sonar","messages":[{"role":"user","content":"Hello! What is 2+2?"}],"max_tokens":50}'
```

## 🔧 Using with .env file:

```bash
# Load API key from .env and test
source .env && curl -X POST "https://api.perplexity.ai/v1/chat/completions" \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"sonar","messages":[{"role":"user","content":"Hello! What is 2+2?"}],"max_tokens":50}'
```

## 📋 Expected successful response:
```json
{
  "id": "pplx-...",
  "object": "chat.completion",
  "created": 1234567890,
  "model": "sonar",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "2+2 equals 4."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 15,
    "completion_tokens": 5,
    "total_tokens": 20
  }
}
```

## ❌ Common error responses:

### Invalid API Key (401):
```json
{
  "error": {
    "message": "Invalid API key",
    "type": "invalid_request_error"
  }
}
```

### Rate Limit (429):
```json
{
  "error": {
    "message": "Rate limit exceeded",
    "type": "rate_limit_error"
  }
}
```

## 🎯 Quick validation script:
```bash
./test_curl.sh
```
