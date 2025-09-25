# InsightAI 

Transform any topic into engaging LinkedIn content with the power of AI. InsightAI automatically fetches the latest news and creates professional, LinkedIn-ready posts that drive engagement.

## Features

- **Smart Content Generation**: Convert any topic into professional LinkedIn posts
- **Real-time News Integration**: Automatically fetches the latest articles and news
- **Visual Recommendations**: Get curated image suggestions for your posts
- **Developer-Friendly**: Full REST API with interactive Swagger documentation
- **Fast & Reliable**: Built on modern FastAPI architecture

## Tech Stack

- **Backend**: FastAPI
- **AI Engine**: Google Gemini API with LangChain agents
- **Deployment**: Vercel
- **Language**: Python 3.11+

## Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/InsightAI.git
   cd InsightAI
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   # .venv\Scripts\activate    # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Create a `.env` file in the root directory:
   ```env
   GOOGLE_API_KEY="add here"
   TAVILY_API_KEY = "add here"
   ```

5. **Start the development server**
   ```bash
   uvicorn api.generate_post:app --reload
   ```

6. **Test your installation**
   ```bash
    curl -X POST "http://127.0.0.1:8000/generate_post" \
      -H "Content-Type: application/json" \
      -d '{"topic": "Artificial Intelligence"}'
   ```

## API Documentation

Once your server is running, explore the interactive API documentation:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## Live API

Use our deployed version for instant access:
- **Swagger UI**: https://insight-ai-virid.vercel.app/docs
- **ReDoc**: https://insight-ai-virid.vercel.app/redoc

```bash
curl -X POST "https://insight-ai-virid.vercel.app/generate_post" -H "Content-Type: application/json" -d '{"topic": "Artificial Intelligence"}'
```

##  API Usage

### Generate LinkedIn Post

**Endpoint**: `POST /generate_post`

**Request Body**:
```json
{
  "topic": "cognitive impact of ChatGPT"
}
```

**Response**:
```json
{
  "topic": "Cognitive impact of ChatGPT",
  "news_sources": [
    "https://www.wired.com/story/the-age-of-autocomplete-has-already-dented-our-minds/",
    "https://www.telegraph.co.uk/news/2024/02/03/artificial-intelligence-making-people-stupid/",
    "https://www.linkedin.com/pulse/chatgpt-making-us-dumber-abdullah-siddiqui/",
    "https://www.linkedin.com/pulse/we-using-ai-too-much-hurting-our-brains-dr-sergio-lucchini-md-phd/"
  ],
  "linkedin_post": "Is ChatGPT making us dumber?\n\nIt's a question on many minds.\n\nAre we outsourcing our thinking?\n\nSome experts worry about a decline in cognitive skills.\nEspecially problem-solving and critical thinking.\n\nBut AI can also augment our abilities.\n\nHow do we strike the right balance?\n\nWhat are your thoughts on AI and cognitive function?\n\n#AI #ChatGPT #CognitiveSkills #FutureofWork #Technology",
  "image_suggestion": [
    "https://images.unsplash.com/photo-1555952517-2e8e7297adca?q=80&w=2070&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1507838153414-b4b79886a337?q=80&w=2070&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1667374042106-5880b5485405?q=80&w=2070&auto=format&fit=crop"
  ]
}
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
