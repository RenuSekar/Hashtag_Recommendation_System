from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import ollama

# Initialize FastAPI app
app = FastAPI()

# Mount static files (for serving CSS and other static assets)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Pydantic model for the input content
class Content(BaseModel):
    content: str

# HTML route
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("templates/index.html", "r") as f:
        return f.read()

# API to generate hashtags
@app.post("/generate_hashtags/")
async def generate_hashtags(content: Content):
    try:
        # Call the Ollama API to generate hashtags
        prompt = f"Generate 5 relevant hashtags for the following text:\n\n{content.content}\n\nHashtags:"
        response = ollama.generate(model="llama3", prompt=prompt)
        
        if response and "response" in response:
            hashtags = [tag.strip() for tag in response["response"].split(",") if tag.strip()]
            return {"hashtags": hashtags[:5]}
        else:
            raise HTTPException(status_code=400, detail="Failed to generate hashtags")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")
