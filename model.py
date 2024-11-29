import ollama

def recommend_hashtags(content, num_tags=5):
    """
    Generate hashtags based on the given content using Ollama's Python library.
    
    Args:
        content (str): The input text for which hashtags are to be generated.
        num_tags (int): The number of hashtags to generate.

    Returns:
        list: A list of generated hashtags.
    """
    # Define the prompt for hashtag generation
    prompt = f"Generate {num_tags} relevant hashtags for the following text:\n\n{content}\n\nHashtags:"

    try:
        # Call the Ollama model with generate() method
        response = ollama.generate(model="llama3", prompt=prompt)
        
        # Check if the response is valid and parse the response for hashtags
        if response and "response" in response:
            hashtags = [tag.strip() for tag in response["response"].split(",") if tag.strip()]
            return hashtags[:num_tags]
        else:
            print("Error: Failed to get a response from Ollama.")
            return []
    except Exception as e:
        print(f"Error: {e}")
        return []

# Test the function
if __name__ == "__main__":
    # Example input
    content = "Learn Python programming for AI and Data Science."
    
    # Generate hashtags
    hashtags = recommend_hashtags(content)
    
    # Print the generated hashtags
    print("Generated Hashtags:", hashtags)
