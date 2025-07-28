# OpenAI Function Calling: Standard vs BAML Approach

This guide explains the conceptual differences between standard OpenAI function calling and the BAML (Boundary AI Markup Language) approach, along with examples of how to use both methods.

## Table of Contents
- [Standard OpenAI Function Calling](#standard-openai-function-calling)
- [BAML Approach](#baml-approach)
- [Key Differences](#key-differences)
- [How to Run Examples](#how-to-run-examples)

## Standard OpenAI Function Calling

### Concept

Standard OpenAI function calling involves:

1. **Manual Schema Definition**: You define JSON schemas for functions directly in your code
2. **Manual Execution**: You intercept function calls and execute them yourself
3. **Manual Response Handling**: You parse and process the results manually
4. **No Type Safety**: No compile-time checking of parameters or return types

### Example

```python
# From openai_function_calling.py
functions = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "The temperature unit to use"
                    }
                },
                "required": ["location"]
            }
        }
    }
]

# Make API call with function definitions
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[...],
    tools=functions,
    tool_choice="auto"
)
```

## BAML Approach

### Concept

BAML's approach involves:

1. **Declarative Schema Definition**: You define schemas in BAML files (separate from code)
2. **Type-Safe Code Generation**: BAML generates Pydantic models for type safety
3. **Automated Execution**: BAML handles function execution and response parsing
4. **Separation of Concerns**: Clear distinction between configuration and business logic

### Example

```baml
// From weather_functions.baml
class WeatherRequest {
  query string
}

class WeatherData {
  location Location
  temperature float
  unit string
  forecast string[]
}

function GetWeather(request: WeatherRequest) -> WeatherData {
  client Gpt4o
  
  tools #"
    [
      {
        "type": "function",
        "function": {
          "name": "get_current_weather",
          "description": "Get the current weather in a location",
          "parameters": {
            // Schema definition
          }
        }
      }
    ]
  "#
  
  prompt #"{{ request.query }}"#
  tool_choice "auto"
}
```

## Key Differences

| Aspect | Standard OpenAI | BAML |
|--------|----------------|------|
| **Type Safety** | None (runtime errors) | Full (compile-time checking) |
| **Code Organization** | Mixed with business logic | Separate configuration files |
| **Maintenance** | Update code in multiple places | Central schema definitions |
| **Verbosity** | Higher (JSON in Python) | Lower (dedicated schema language) |
| **Learning Curve** | Lower (standard Python) | Higher (learn BAML syntax) |
| **Consistency** | Varies by developer | Enforced by schema |
| **Refactoring** | Manual updates everywhere | Automatic propagation |

## How to Run Examples

### Running Standard OpenAI Example

1. Ensure dependencies are installed:
```bash
uv add openai python-dotenv
```

2. Run the example script:
```bash
python openai_function_calling.py
```

This script demonstrates:
- Traditional function calling with tool definitions
- Handling function calls from the model
- JSON mode for structured outputs

### Running BAML Example

1. Generate BAML client code:
```bash
npx @boundaryml/baml generate
```

2. Create a Python script to use the BAML client:
```python
from baml_client.sync_client import b
from baml_client.types import WeatherRequest, WeatherData

# Create a request
request = WeatherRequest(query="What's the weather like in Boston?")

# Call the BAML function
response = b.GetWeather(request)

# Access typed response
print(f"Temperature in {response.location.city}: {response.temperature}°{response.unit}")
print(f"Forecast: {', '.join(response.forecast)}")
```

3. Run your script:

```bash
python your_script_name.py
```