#!/usr/bin/env python3
"""
Perplexity API Integration Script
================================

This script demonstrates various cool features you can build with the Perplexity API:
- Real-time web search and research
- News analysis and trending topics
- Academic research assistance
- Code debugging and technical help
- Market analysis and financial insights
- Travel planning and recommendations
- Creative writing assistance
- Fact-checking and verification

Requirements:
- pip install requests python-dotenv
- Get API key from: https://www.perplexity.ai/settings/api
"""

import os
import json
import requests
import time
from datetime import datetime
from typing import List, Dict, Optional, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class PerplexityAPI:
    """Perplexity API client with various cool features"""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the Perplexity API client"""
        self.api_key = api_key or os.getenv('PERPLEXITY_API_KEY')
        if not self.api_key:
            raise ValueError("Perplexity API key is required. Set PERPLEXITY_API_KEY environment variable or pass it directly.")
        
        self.base_url = "https://api.perplexity.ai/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def _make_request(self, messages: List[Dict], model: str = "sonar") -> Dict:
        """Make a request to the Perplexity API"""
        payload = {
            "model": model,
            "messages": messages,
            "max_tokens": 1000,
            "temperature": 0.2,
            "top_p": 0.9
        }
        
        try:
            response = requests.post(self.base_url, headers=self.headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error {e.response.status_code}: {e.response.text}")
            return {}
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            return {}
        except Exception as e:
            print(f"Unexpected error: {e}")
            return {}
    
    def search_and_answer(self, query: str, context: str = "") -> Dict:
        """Basic search and answer functionality"""
        messages = [
            {
                "role": "system",
                "content": "You are a helpful research assistant. Provide accurate, up-to-date information with citations."
            },
            {
                "role": "user",
                "content": f"{context}\n\nQuery: {query}"
            }
        ]
        
        return self._make_request(messages)
    
    def real_time_research(self, topic: str, depth: str = "comprehensive") -> Dict:
        """Real-time research on any topic with different depth levels"""
        depth_prompts = {
            "quick": "Provide a brief overview with key points",
            "comprehensive": "Provide a detailed analysis with multiple perspectives",
            "deep": "Provide an in-depth research report with historical context and future implications"
        }
        
        prompt = f"""
        Research Topic: {topic}
        
        Please provide a {depth_prompts.get(depth, depth_prompts['comprehensive'])} on this topic.
        Include:
        - Current status and recent developments
        - Key players and stakeholders
        - Potential implications
        - Recent news and trends
        - Citations and sources
        """
        
        return self.search_and_answer(prompt)
    
    def news_analysis(self, topic: str, timeframe: str = "week") -> Dict:
        """Analyze recent news and trends for a specific topic"""
        prompt = f"""
        Analyze the latest news and trends about: {topic}
        
        Timeframe: Last {timeframe}
        
        Please provide:
        1. Top news stories and their significance
        2. Key trends and patterns
        3. Market or public sentiment analysis
        4. Potential future developments
        5. Impact assessment
        
        Focus on the most recent and relevant information.
        """
        
        return self.search_and_answer(prompt)
    
    def academic_research_assistant(self, research_question: str, field: str = "") -> Dict:
        """Academic research assistance with citations"""
        prompt = f"""
        Research Question: {research_question}
        Field: {field if field else "General"}
        
        Please provide an academic-style research response including:
        1. Background and context
        2. Current state of research
        3. Key findings and methodologies
        4. Gaps in current research
        5. Recent publications and studies
        6. Future research directions
        
        Include proper citations and academic sources where possible.
        """
        
        return self.search_and_answer(prompt)
    
    def code_debugging_assistant(self, code: str, error_message: str = "", language: str = "python") -> Dict:
        """Help debug code and provide technical solutions"""
        prompt = f"""
        Programming Language: {language}
        Code:
        ```
        {code}
        ```
        
        Error Message: {error_message if error_message else "No specific error, general code review requested"}
        
        Please provide:
        1. Code analysis and potential issues
        2. Debugging suggestions
        3. Best practices recommendations
        4. Alternative approaches
        5. Performance optimizations if applicable
        6. Recent updates or changes in the language/framework
        
        Focus on practical, actionable solutions.
        """
        
        return self.search_and_answer(prompt)
    
    def market_analysis(self, company: str = "", industry: str = "", market: str = "") -> Dict:
        """Financial and market analysis"""
        if company:
            prompt = f"""
            Analyze the current market position and financial outlook for: {company}
            
            Please provide:
            1. Recent financial performance
            2. Stock price trends and analysis
            3. Market position and competitive landscape
            4. Recent news and developments
            5. Analyst opinions and forecasts
            6. Risk factors and opportunities
            """
        elif industry:
            prompt = f"""
            Provide a comprehensive market analysis for the {industry} industry:
            
            Include:
            1. Industry overview and size
            2. Key players and market share
            3. Recent trends and developments
            4. Growth prospects and challenges
            5. Regulatory environment
            6. Investment opportunities
            """
        else:
            prompt = f"""
            Provide a general market analysis for: {market}
            
            Focus on:
            1. Current market conditions
            2. Economic indicators
            3. Sector performance
            4. Investment trends
            5. Risk assessment
            """
        
        return self.search_and_answer(prompt)
    
    def travel_planner(self, destination: str, duration: str = "1 week", interests: str = "") -> Dict:
        """Travel planning and recommendations"""
        prompt = f"""
        Travel Planning Request:
        Destination: {destination}
        Duration: {duration}
        Interests: {interests if interests else "General sightseeing and local experiences"}
        
        Please provide:
        1. Best time to visit and weather conditions
        2. Top attractions and must-see places
        3. Local culture and customs
        4. Transportation options
        5. Accommodation recommendations
        6. Food and dining suggestions
        7. Safety tips and travel advisories
        8. Budget estimates
        9. Recent travel updates and restrictions
        10. Hidden gems and off-the-beaten-path experiences
        """
        
        return self.search_and_answer(prompt)
    
    def creative_writing_assistant(self, genre: str, prompt: str, style: str = "engaging") -> Dict:
        """Creative writing assistance and inspiration"""
        full_prompt = f"""
        Creative Writing Request:
        Genre: {genre}
        Style: {style}
        Prompt/Theme: {prompt}
        
        Please provide:
        1. Story ideas and plot suggestions
        2. Character development tips
        3. Setting and atmosphere ideas
        4. Dialogue examples
        5. Writing techniques specific to the genre
        6. Inspiration from recent works in the genre
        7. Common pitfalls to avoid
        8. Publishing and market insights
        """
        
        return self.search_and_answer(full_prompt)
    
    def fact_checker(self, claim: str, context: str = "") -> Dict:
        """Fact-checking and verification service"""
        prompt = f"""
        Fact-Checking Request:
        Claim: {claim}
        Context: {context if context else "No additional context provided"}
        
        Please provide:
        1. Verification of the claim's accuracy
        2. Sources and evidence
        3. Alternative perspectives or corrections
        4. Historical context if relevant
        5. Expert opinions or consensus
        6. Related information that might be relevant
        7. Confidence level in the assessment
        """
        
        return self.search_and_answer(prompt)
    
    def tech_trends_analyzer(self, technology: str = "", timeframe: str = "6 months") -> Dict:
        """Analyze technology trends and developments"""
        if technology:
            prompt = f"""
            Technology Trend Analysis: {technology}
            Timeframe: Last {timeframe}
            
            Please analyze:
            1. Recent developments and breakthroughs
            2. Market adoption and growth
            3. Key players and investments
            4. Technical challenges and solutions
            5. Future predictions and roadmap
            6. Impact on related industries
            7. Job market and career opportunities
            """
        else:
            prompt = f"""
            General Technology Trends Analysis
            Timeframe: Last {timeframe}
            
            Please provide:
            1. Emerging technologies and trends
            2. Hot topics in tech industry
            3. Major announcements and releases
            4. Investment and funding trends
            5. Regulatory developments
            6. Skills in demand
            7. Future predictions
            """
        
        return self.search_and_answer(prompt)
    
    def health_and_wellness_research(self, topic: str, focus: str = "general") -> Dict:
        """Health and wellness research (with medical disclaimer)"""
        prompt = f"""
        Health and Wellness Research: {topic}
        Focus: {focus}
        
        IMPORTANT: This is for informational purposes only and should not replace professional medical advice.
        
        Please provide:
        1. Current research and findings
        2. Expert opinions and consensus
        3. Recent studies and clinical trials
        4. Safety considerations
        5. Lifestyle and prevention tips
        6. When to consult healthcare professionals
        7. Reliable sources and references
        
        Always emphasize consulting healthcare professionals for medical decisions.
        """
        
        return self.search_and_answer(prompt)


def demo_perplexity_features():
    """Demonstrate various cool features of the Perplexity API"""
    
    # Initialize the API client
    try:
        api = PerplexityAPI()
        print("🚀 Perplexity API Client Initialized Successfully!")
        print("=" * 60)
    except ValueError as e:
        print(f"❌ Error: {e}")
        print("Please set your PERPLEXITY_API_KEY environment variable")
        return
    
    # Demo functions
    demos = [
        {
            "name": "Real-time Research",
            "function": lambda: api.real_time_research("artificial intelligence trends 2024", "comprehensive"),
            "description": "Get comprehensive research on AI trends"
        },
        {
            "name": "News Analysis",
            "function": lambda: api.news_analysis("cryptocurrency", "week"),
            "description": "Analyze recent crypto news and trends"
        },
        {
            "name": "Academic Research",
            "function": lambda: api.academic_research_assistant("impact of climate change on agriculture", "environmental science"),
            "description": "Academic research assistance with citations"
        },
        {
            "name": "Code Debugging",
            "function": lambda: api.code_debugging_assistant("def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)", "", "python"),
            "description": "Get help debugging and optimizing code"
        },
        {
            "name": "Market Analysis",
            "function": lambda: api.market_analysis(company="Tesla"),
            "description": "Analyze Tesla's market position and outlook"
        },
        {
            "name": "Travel Planning",
            "function": lambda: api.travel_planner("Japan", "2 weeks", "technology, culture, food"),
            "description": "Get comprehensive travel recommendations"
        },
        {
            "name": "Creative Writing",
            "function": lambda: api.creative_writing_assistant("sci-fi", "time travel paradox", "thought-provoking"),
            "description": "Get creative writing assistance and inspiration"
        },
        {
            "name": "Fact Checking",
            "function": lambda: api.fact_checker("The Great Wall of China is visible from space"),
            "description": "Verify facts and get accurate information"
        },
        {
            "name": "Tech Trends",
            "function": lambda: api.tech_trends_analyzer("quantum computing", "3 months"),
            "description": "Analyze quantum computing trends and developments"
        },
        {
            "name": "Health Research",
            "function": lambda: api.health_and_wellness_research("meditation benefits", "mental health"),
            "description": "Research health and wellness topics (informational only)"
        }
    ]
    
    print("🎯 Available Demo Features:")
    for i, demo in enumerate(demos, 1):
        print(f"{i:2d}. {demo['name']}: {demo['description']}")
    
    print("\n" + "=" * 60)
    print("💡 To run a specific demo, modify the demo_perplexity_features() function")
    print("💡 Or use the API client directly in your own scripts!")
    
    # Example: Run the first demo
    print(f"\n🔍 Running Demo: {demos[0]['name']}")
    print("-" * 40)
    
    result = demos[0]['function']()
    if result and 'choices' in result:
        print("Response:")
        print(result['choices'][0]['message']['content'])
        
        if 'citations' in result:
            print("\n📚 Citations:")
            for citation in result['citations']:
                print(f"- {citation}")
    else:
        print("❌ No response received")


def interactive_mode():
    """Interactive mode for testing different features"""
    try:
        api = PerplexityAPI()
        print("🎮 Interactive Perplexity API Mode")
        print("Type 'quit' to exit, 'help' for commands")
        print("=" * 50)
        
        while True:
            query = input("\n🔍 Enter your query: ").strip()
            
            if query.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            elif query.lower() == 'help':
                print_help()
                continue
            elif not query:
                continue
            
            print("🤔 Thinking...")
            result = api.search_and_answer(query)
            
            if result and 'choices' in result:
                print("\n📝 Response:")
                print(result['choices'][0]['message']['content'])
                
                if 'citations' in result:
                    print("\n📚 Sources:")
                    for citation in result['citations']:
                        print(f"- {citation}")
            else:
                print("❌ No response received")
    
    except ValueError as e:
        print(f"❌ Error: {e}")
        print("Please set your PERPLEXITY_API_KEY environment variable")


def print_help():
    """Print help information"""
    print("""
🆘 Available Commands:
- help: Show this help message
- quit/exit/q: Exit the program

💡 Query Examples:
- "What are the latest developments in AI?"
- "Explain quantum computing in simple terms"
- "What's happening with Tesla stock?"
- "Best restaurants in Paris for vegetarians"
- "How to optimize Python code performance?"
- "Recent news about climate change"
- "Travel tips for Japan in spring"
- "Fact check: Is the Earth flat?"

🎯 The API can help with:
- Real-time research and fact-checking
- News analysis and trending topics
- Academic research with citations
- Code debugging and technical help
- Market and financial analysis
- Travel planning and recommendations
- Creative writing assistance
- Health and wellness research (informational)
- Technology trends analysis
""")


if __name__ == "__main__":
    print("🌟 Perplexity API Integration Script")
    print("=" * 50)
    
    # Check if API key is available
    if not os.getenv('PERPLEXITY_API_KEY'):
        print("⚠️  PERPLEXITY_API_KEY not found in environment variables")
        print("Please set your API key:")
        print("export PERPLEXITY_API_KEY='your_api_key_here'")
        print("\nOr create a .env file with:")
        print("PERPLEXITY_API_KEY=your_api_key_here")
        print("\nGet your API key from: https://www.perplexity.ai/pplx-api")
        print("\nTo test your API key, run: python test_api.py")
        print("\nRunning demo mode without API calls...")
        demo_perplexity_features()
    else:
        # Run demos
        demo_perplexity_features()
        
        # Ask if user wants interactive mode
        print("\n" + "=" * 60)
        choice = input("🎮 Would you like to try interactive mode? (y/n): ").strip().lower()
        if choice in ['y', 'yes']:
            interactive_mode()
