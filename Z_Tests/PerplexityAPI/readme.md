# Perplexity API Integration

A comprehensive Python script that demonstrates the power of the Perplexity API with various cool features and use cases.

## 🚀 Features

### Core Capabilities
- **Real-time Web Search**: Get up-to-date information with citations
- **Research Assistant**: Comprehensive research on any topic
- **News Analysis**: Analyze trending topics and recent developments
- **Academic Research**: Get scholarly information with proper citations
- **Code Debugging**: Technical assistance for programming problems
- **Market Analysis**: Financial and business insights
- **Travel Planning**: Comprehensive travel recommendations
- **Creative Writing**: Assistance with creative projects
- **Fact Checking**: Verify information and get accurate sources
- **Tech Trends**: Analyze technology developments
- **Health Research**: Wellness and health information (informational only)

## 🛠️ Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Get API Key**:
   - Visit [Perplexity AI Settings](https://www.perplexity.ai/settings/api)
   - Create an account and generate your API key

3. **Set Environment Variable**:
   ```bash
   export PERPLEXITY_API_KEY='your_api_key_here'
   ```
   
   Or create a `.env` file:
   ```
   PERPLEXITY_API_KEY=your_api_key_here
   ```

## 🎯 Cool Things You Can Do

### 1. Real-Time Research
```python
api = PerplexityAPI()
result = api.real_time_research("artificial intelligence trends 2024", "comprehensive")
```

### 2. News Analysis
```python
result = api.news_analysis("cryptocurrency", "week")
```

### 3. Academic Research
```python
result = api.academic_research_assistant("climate change impact on agriculture", "environmental science")
```

### 4. Code Debugging
```python
result = api.code_debugging_assistant("""
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
""", "", "python")
```

### 5. Market Analysis
```python
result = api.market_analysis(company="Tesla")
```

### 6. Travel Planning
```python
result = api.travel_planner("Japan", "2 weeks", "technology, culture, food")
```

### 7. Creative Writing
```python
result = api.creative_writing_assistant("sci-fi", "time travel paradox", "thought-provoking")
```

### 8. Fact Checking
```python
result = api.fact_checker("The Great Wall of China is visible from space")
```

### 9. Tech Trends
```python
result = api.tech_trends_analyzer("quantum computing", "3 months")
```

### 10. Health Research
```python
result = api.health_and_wellness_research("meditation benefits", "mental health")
```

## 🎮 Usage

### Run Demos
```bash
python perplexity-api.py
```

### Interactive Mode
The script includes an interactive mode where you can ask questions directly:
```bash
python perplexity-api.py
# Then choose interactive mode when prompted
```

### Use in Your Own Code
```python
from perplexity_api import PerplexityAPI

api = PerplexityAPI()
result = api.search_and_answer("What are the latest AI developments?")
print(result['choices'][0]['message']['content'])
```

## 🌟 Advanced Features

### Custom Search Parameters
- **Model Selection**: Choose from different Perplexity models
- **Temperature Control**: Adjust response creativity
- **Citation Requirements**: Get sources with every response
- **Domain Filtering**: Focus on specific domains
- **Recency Filtering**: Get recent information only

### Response Format
All responses include:
- **Content**: The main response
- **Citations**: Source links and references
- **Metadata**: Additional context and information

## 🔧 API Models Available

- `sonar` (default)
- `sonar-pro`
- `sonar-medium`
- `sonar-large`

## 📚 Use Cases

### For Developers
- Debug code and get technical solutions
- Research new technologies and frameworks
- Get help with best practices
- Stay updated with tech trends

### For Researchers
- Academic research with citations
- Fact-checking and verification
- Literature reviews
- Data analysis insights

### For Business
- Market analysis and competitor research
- Industry trend analysis
- Financial insights
- Business intelligence

### For Content Creators
- Research for articles and blogs
- Fact-checking content
- Creative writing assistance
- Trend analysis for content strategy

### For Travelers
- Destination research
- Travel planning and recommendations
- Local insights and tips
- Safety and travel advisories

## ⚠️ Important Notes

- **Rate Limits**: Be mindful of API rate limits
- **Costs**: Perplexity API has usage-based pricing
- **Accuracy**: Always verify critical information from multiple sources
- **Medical Disclaimer**: Health information is for educational purposes only

## 🔗 Links

- [Perplexity AI](https://www.perplexity.ai/)
- [API Documentation](https://docs.perplexity.ai/)
- [API Settings](https://www.perplexity.ai/settings/api)

## 📄 License

This script is provided as-is for educational and development purposes.