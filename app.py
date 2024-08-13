import streamlit as st

# Mind map structure with AI tools categorized and descriptions
mind_map = {
    "AI Platforms": {
        "Local LM (Language Models)": [
            {"name": "Ollama", "url": "https://ollama.com/", "description": "Ollama is a language model platform offering various capabilities for text generation and understanding."},
            {"name": "LM Studio", "url": "https://lmstudio.ai/", "description": "LM Studio provides a user-friendly interface for working with large language models in a collaborative environment."},
            {"name": "Nomic GPT4All", "url": "https://www.nomic.ai/gpt4all", "description": "Nomic GPT4All is a versatile language model designed for developers and researchers with robust capabilities."},
        ],
        "AI Chat & Interaction": [
            {"name": "FlowGPT", "url": "https://flowgpt.com/", "description": "FlowGPT is a chat-based AI platform that helps users create conversational AI models quickly and easily."},
            {"name": "Poe", "url": "https://poe.com/", "description": "Poe is an interactive AI chat platform that allows users to engage with AI in natural language."},
            {"name": "Pi.ai", "url": "https://pi.ai/", "description": "Pi.ai offers a conversational AI experience for personal and professional use cases."},
        ],
        "AI Image Generation": [
            {"name": "Leonardo.ai", "url": "https://leonardo.ai/", "description": "Leonardo.ai is a powerful tool for generating high-quality AI images."},
            {"name": "Bing Image Creator", "url": "https://www.bing.com/images/create", "description": "Bing Image Creator allows users to generate images using AI directly from prompts."},
            {"name": "Craiyon", "url": "https://www.craiyon.com/", "description": "Craiyon is a free AI image generator that produces images from text prompts."},
            {"name": "Artbreeder", "url": "https://www.artbreeder.com/create", "description": "Artbreeder allows users to create and modify images using AI-powered tools."},
        ],
    },
    "AI Tools for Developers": {
        "AI Code Assistants": [
            {"name": "Codeium", "url": "https://codeium.com/", "description": "Codeium helps developers write code faster with AI-powered autocomplete and suggestions."},
            {"name": "OpenInterpreter", "url": "https://www.openinterpreter.com/", "description": "OpenInterpreter allows developers to control their PC using AI commands."},
            {"name": "Perplexity AI", "url": "https://www.perplexity.ai/", "description": "Perplexity AI is a coding assistant with real-time internet access for research."},
        ],
        "Code Commenting Tools": [
            {"name": "Sourcegraph", "url": "https://sourcegraph.com/", "description": "Sourcegraph provides AI-powered code search and commenting."},
            {"name": "Readable.so", "url": "https://readable.so/", "description": "Readable.so makes code more understandable with AI-generated comments."},
        ],
        "Task Automation": [
            {"name": "Keyflow.space", "url": "https://www.keyflow.space/", "description": "Keyflow.space automates workflows using AI, improving efficiency."},
            {"name": "Respell", "url": "https://www.respell.ai/", "description": "Respell is a platform for automating tasks with AI-driven tools."},
            {"name": "MultiOn", "url": "https://www.multion.ai/", "description": "MultiOn automates tasks with AI and API integration for various applications."},
        ],
    },
    "AI Tools for Creatives": {
        "AI Video Creation": [
            {"name": "Pixverse.ai", "url": "https://pixverse.ai/", "description": "Pixverse.ai allows users to create videos from text prompts using AI."},
            {"name": "Pika.art", "url": "https://pika.art/login", "description": "Pika.art helps creators generate AI-powered videos with ease."},
            {"name": "Arcade.Studio", "url": "https://arcade.studio/", "description": "Arcade.Studio offers tools for creating AI-generated videos from scripts."},
            {"name": "Vidyo.ai", "url": "https://vidyo.ai/", "description": "Vidyo.ai converts long videos into short, engaging clips using AI."},
        ],
        "AI Image Editing": [
            {"name": "DeWatermark.ai", "url": "https://dewatermark.ai/it", "description": "DeWatermark.ai removes watermarks from images quickly and efficiently."},
            {"name": "MagicStudio", "url": "https://magicstudio.com/it/magiceraser/", "description": "MagicStudio offers AI tools for removing objects and backgrounds from images."},
            {"name": "Deep-Image.ai", "url": "https://deep-image.ai/", "description": "Deep-Image.ai provides AI-driven image upscaling and enhancement."},
        ],
        "AI Music Creation": [
            {"name": "Soundraw.io", "url": "https://soundraw.io/", "description": "Soundraw.io enables users to create original soundtracks using AI."},
            {"name": "Suno.ai", "url": "https://www.suno.ai/", "description": "Suno.ai generates music and lyrics with the help of AI."},
            {"name": "Udio.com", "url": "https://udio.com/", "description": "Udio.com allows for the creation of AI-generated songs with vocals."},
        ],
    },
    "AI Tools for Marketing": {
        "AI for Social Media": [
            {"name": "Aiter.io", "url": "https://aiter.io/", "description": "Aiter.io specializes in creating AI-powered social media ads."},
            {"name": "Predis.ai", "url": "https://predis.ai/", "description": "Predis.ai generates social media posts and content within seconds."},
            {"name": "ContentStudio.io", "url": "https://contentstudio.io/", "description": "ContentStudio.io helps manage and create content for various social media platforms."},
            {"name": "Lately.ai", "url": "https://www.lately.ai/", "description": "Lately.ai automates the creation and management of social media content using AI."},
        ],
        "AI for Content Creation": [
            {"name": "Beautiful.ai", "url": "https://www.beautiful.ai/", "description": "Beautiful.ai creates stunning presentations and slides using AI."},
            {"name": "Simplified.com", "url": "https://simplified.com/", "description": "Simplified.com offers various AI tools for content creation and marketing."},
            {"name": "Fliki.ai", "url": "https://fliki.ai/", "description": "Fliki.ai converts text into engaging videos with AI-generated voiceovers."},
        ],
    },
}

# Streamlit UI
st.set_page_config(layout="wide")
st.title("AI Tools Explorer")

# Sidebar for navigation
st.sidebar.title("Categories")
category_selected = st.sidebar.selectbox("Select a category", list(mind_map.keys()))
subcategory_selected = st.sidebar.selectbox("Select a subcategory", list(mind_map[category_selected].keys()))

# Display tools in the selected category and subcategory
st.subheader(f"{subcategory_selected} - {category_selected}")
tools = mind_map[category_selected][subcategory_selected]

# Two-column layout: Left for descriptions, right for embedded iframe
col1, col2 = st.columns([1, 2])

with col1:
    st.write("### Tools")
    for tool in tools:
        if st.button(tool['name']):
            st.session_state['selected_tool'] = tool

# Check if a tool is selected and display its information
if 'selected_tool' in st.session_state:
    selected_tool = st.session_state['selected_tool']
    with col1:
        st.write(f"**{selected_tool['name']}**")
        st.write(selected_tool['description'])

    with col2:
        st.write(f"### {selected_tool['name']} Website")
        st.components.v1.iframe(selected_tool['url'], height=600, scrolling=True)
else:
    with col2:
        st.write("Select a tool to view more information and visit its website.")
