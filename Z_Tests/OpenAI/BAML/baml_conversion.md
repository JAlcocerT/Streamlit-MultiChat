# Converting Plan Enhancement Script to BAML

This document explains the reasoning behind converting the standard OpenAI script (`plan_enhancement.py`) to use BAML (`plan_enhancement_baml.py`).

## Why Convert to BAML?

### 1. Type Safety and Validation

The original script creates untyped API calls to OpenAI and then has to handle JSON parsing manually. With BAML:

- Input and output structures are clearly defined as BAML classes
- Pydantic models are auto-generated from these definitions
- JSON parsing is handled automatically
- Runtime type checking ensures data conforms to expected structure

### 2. Improved Maintainability

The BAML approach separates:

- **Schema definitions** (in `doc_enhancement.baml`)
- **Business logic** (in `plan_enhancement_baml.py`)
- **Prompt content** (in the separate prompt files)

This separation makes it easier to:
- Modify schemas without changing code
- Update prompts independently
- Evolve the business logic without touching prompts or schemas

### 3. Declarative API Handling

In the original script:
```python
# Manual model selection with different parameter handling
if model_name.startswith("o"):
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model_name,
    )
else:
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model_name,
        temperature=0.3,
    )
```

With BAML, this is handled declaratively:

```baml
client<llm> Gpt4oMini {
  provider openai
  options {
    model "gpt-4o-mini"
    api_key env.OPENAI_API_KEY
    temperature 0.2
  }
}
```

### 4. Consistent JSON Output Structure

The original script relies on the model to generate properly formatted JSON as directed by prompt text. With BAML:

- Output structure is enforced by BAML schema
- `response_format "json_object"` ensures consistent JSON responses
- Results are automatically parsed into strongly-typed objects

### 5. Easier Model Switching

Changing models in the original script requires modifying code logic. With BAML:

- Models are defined as separate clients
- Changing models requires only changing the client reference
- No conditional logic needed for parameter differences between models

## Implementation Details

### Schema Definition

```baml
class Recommendation {
  recommendation string
}

class EnhancementPlan {
  recommendations Recommendation[]
}
```

This matches the expected JSON structure:
```json
[
  {
    "recommendation": "Expand on advanced topics related to modules integrations."
  },
  {
    "recommendation": "Add more real-world use cases of the project under analysis."
  }
]
```

### Prompt Management

Both approaches load prompts from external files, but BAML integrates them more cleanly:

```baml
prompt #"
  {{ input.system_message }}
  
  {{ input.prompt }}
  
  Documentation content:
  {{ input.documentation }}
"#
```

### JSON Handling

Original script:
- Relies on model to format JSON correctly
- Manually parses JSON response
- No schema validation

BAML:
- Automatically parses responses into typed objects
- Validates against predefined schema
- Provides clean type-safe access to data

## BAML Project Structure

```
baml_src/
  ├── doc_enhancement.baml  # Schema and function definitions
  ├── generators.baml       # BAML code generation config
  └── ...

baml_client/               # Auto-generated code
  ├── types.py             # Generated Pydantic models
  ├── sync_client.py       # API client
  └── ...

plan_enhancement_baml.py   # Script using BAML client
```

## Conclusion

Converting to BAML provides significant advantages in type safety, code organization, and maintainability.

While it requires learning BAML syntax and adding a code generation step, the benefits outweigh these costs for any project that needs reliable, maintainable AI integrations.

The BAML approach is particularly valuable for:
- Projects with complex JSON schemas
- Teams where different people work on models vs. business logic
- Production systems where type safety and reliability are important
- Applications that need to evolve their schemas or prompts over time
