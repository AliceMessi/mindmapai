import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

# Set page configuration
st.set_page_config(layout="wide", page_title="AI Tools Explorer by Hoken Tech", page_icon="🧠")

# Hide default Streamlit UI elements
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Mind map structure with AI tools categorized and descriptions
mind_map = {
    "🚀 AI Platforms": {
        "🗣️ Local LM (Language Models)": [
            {"name": "Ollama", "url": "https://ollama.com/", "description": "Ollama is a language model platform offering various capabilities for text generation and understanding."},
            {"name": "LM Studio", "url": "https://lmstudio.ai/", "description": "LM Studio provides a user-friendly interface for working with large language models in a collaborative environment."},
            {"name": "Nomic GPT4All", "url": "https://www.nomic.ai/gpt4all", "description": "Nomic GPT4All is a versatile language model designed for developers and researchers with robust capabilities."},
            # Added tool
            {"name": "CodeGeeX4", "url": "https://github.com/THUDM/CodeGeeX4?tab=readme-ov-file", "description": "LLM for developers (can be used with LMStudio)"},
        ],
        "💬 AI Chat & Interaction": [
            {"name": "FlowGPT", "url": "https://flowgpt.com/", "description": "FlowGPT is a chat-based AI platform that helps users create conversational AI models quickly and easily."},
            {"name": "Poe", "url": "https://poe.com/", "description": "Poe is an interactive AI chat platform that allows users to engage with AI in natural language."},
            {"name": "Pi.ai", "url": "https://pi.ai/", "description": "Pi.ai offers a conversational AI experience for personal and professional use cases."},
            # Added tools
            {"name": "You.com", "url": "https://you.com/", "description": "Similar to ChatGPT"},
            {"name": "FlowGPT", "url": "https://flowgpt.com/", "description": "Similar to GPT"}, # Duplicate, already present
            {"name": "Chat LLM by Abacus.ai", "url": "https://chatllm.abacus.ai/", "description": "Similar to Merlin, costs $10 per month"},
            {"name": "Platform 01.ai", "url": "https://platform.01.ai/profile", "description": "Similar to ChatGPT, free"},
            {"name": "Hugging Face Chat", "url": "https://huggingface.co/chat", "description": "Chat with different LLMs"},
            {"name": "Kyutai.org", "url": "https://kyutai.org/", "description": "Real-time dialogue chat with AI"},
            {"name": "Character.ai", "url": "https://beta.character.ai/", "description": "Chat with AI figures"},
        ],
        "🎨 AI Image Generation": [
            {"name": "Leonardo.ai", "url": "https://leonardo.ai/", "description": "Leonardo.ai is a powerful tool for generating high-quality AI images."},
            {"name": "Bing Image Creator", "url": "https://www.bing.com/images/create", "description": "Bing Image Creator allows users to generate images using AI directly from prompts."},
            {"name": "Craiyon", "url": "https://www.craiyon.com/", "description": "Craiyon is a free AI image generator that produces images from text prompts."},
            {"name": "Artbreeder", "url": "https://www.artbreeder.com/create", "description": "Artbreeder allows users to create and modify images using AI-powered tools."},
            # Added tools
            {"name": "ZMO.AI Image Creator", "url": "https://imgcreator.zmo.ai/", "description": "Create AI images"},
            {"name": "Ideogram.ai", "url": "https://ideogram.ai/", "description": "Generates AI images for free (100/day)"},
            {"name": "Facet.ai", "url": "https://facet.ai", "description": "Generate images using AI"},
            {"name": "Jeda.ai", "url": "https://www.jeda.ai/", "description": "Create images and icons"},
            {"name": "Krea.ai", "url": "https://www.krea.ai/home", "description": "Create images with AI"},
            {"name": "Yodayo", "url": "https://yodayo.com/", "description": "Create images with AI"},
            {"name": "Visual Electric", "url": "https://visualelectric.com/", "description": "Generate images for free"},
            {"name": "Pretty AI", "url": "https://perchance.org/pretty-ai", "description": "Generate AI images, including NSFW"},
            {"name": "Based Labs Flux1", "url": "https://www.basedlabs.ai/tools/flux1", "description": "Generate AI images"},
        ],
        "🕰️ AI Authentication": [
            {"name": "TrustWatch", "url": "https://www.hokentech.tech/trustwatch", "description": "TrustWatch is the leading AI-driven mobile application for luxury watch authentication."},
        ],
        # Added subcategory
        "🎬 AI Video Editing and Creation": [
            {"name": "BigRoom.TV", "url": "https://www.bigroom.tv/", "description": "Convert rectangular videos to vertical"},
            {"name": "Opus.pro", "url": "https://www.opus.pro/", "description": "Extract clips from videos"},
            {"name": "2short.ai", "url": "https://2short.ai/#", "description": "Create shorts from videos"},
            {"name": "Clip.fm", "url": "https://www.clip.fm/", "description": "Create shorts from videos"},
            {"name": "Vidyo.ai", "url": "https://vidyo.ai/", "description": "Similar to Opus Clip"},
            {"name": "LumaLabs Dream Machine", "url": "https://lumalabs.ai/dream-machine", "description": "Create videos with AI (free)"},
            {"name": "Vidu.studio", "url": "https://www.vidu.studio/", "description": "Create videos with AI"},
        ],
    },
    "💻 AI Tools for Developers": {
        "💡 AI Code Assistants": [
            {"name": "Codeium", "url": "https://codeium.com/", "description": "Codeium helps developers write code faster with AI-powered autocomplete and suggestions."},
            {"name": "OpenInterpreter", "url": "https://www.openinterpreter.com/", "description": "OpenInterpreter allows developers to control their PC using AI commands."},
            {"name": "Perplexity AI", "url": "https://www.perplexity.ai/", "description": "Perplexity AI is a coding assistant with real-time internet access for research."},
            # Added tools
            {"name": "Devin.ai", "url": "https://preview.devin.ai/", "description": "Write code with AI"},
            {"name": "AutoCoder", "url": "https://github.com/bin123apple/AutoCoder", "description": "Specific model for code development"},
            {"name": "Tabby", "url": "https://tabby.tabbyml.com/", "description": "Code assistant"},
            {"name": "Cosine.sh", "url": "https://cosine.sh/", "description": "LLM for coding"},
            {"name": "LlamaCoder", "url": "https://llamacoder.together.ai/", "description": "Create full-stack apps for free"},
        ],
        "📝 Code Commenting Tools": [
            {"name": "Sourcegraph", "url": "https://sourcegraph.com/", "description": "Sourcegraph provides AI-powered code search and commenting."},
            {"name": "Readable.so", "url": "https://readable.so/", "description": "Readable.so makes code more understandable with AI-generated comments."},
        ],
        "🤖 Task Automation": [
            {"name": "Keyflow.space", "url": "https://www.keyflow.space/", "description": "Keyflow.space automates workflows using AI, improving efficiency."},
            {"name": "Respell", "url": "https://www.respell.ai/", "description": "Respell is a platform for automating tasks with AI-driven tools."},
            {"name": "MultiOn", "url": "https://www.multion.ai/", "description": "MultiOn automates tasks with AI and API integration for various applications."},
            # Added tools
            {"name": "Autotab.com", "url": "https://autotab.com/", "description": "Automate tasks with an AI-guided bot"},
            {"name": "Make.com", "url": "https://www.make.com/en", "description": "Automate workflows"},
            {"name": "Relay.app", "url": "https://www.relay.app/", "description": "Automate various tasks, similar to Zapier"},
        ],
        # Added subcategory
        "🐞 Code Analysis and Debugging": [
            {"name": "Pieces.app", "url": "https://pieces.app/", "description": "Check code on IDE"},
        ],
    },
    "🎨 AI Tools for Creatives": {
        "🎥 AI Video Creation": [
            {"name": "Pixverse.ai", "url": "https://pixverse.ai/", "description": "Pixverse.ai allows users to create videos from text prompts using AI."},
            {"name": "Pika.art", "url": "https://pika.art/login", "description": "Pika.art helps creators generate AI-powered videos with ease."},
            {"name": "Arcade.Studio", "url": "https://arcade.studio/", "description": "Arcade.Studio offers tools for creating AI-generated videos from scripts."},
            {"name": "Vidyo.ai", "url": "https://vidyo.ai/", "description": "Vidyo.ai converts long videos into short, engaging clips using AI."},
            # Added tools
            {"name": "Fliki.ai", "url": "https://fliki.ai/", "description": "Convert text into engaging videos with AI-generated voiceovers."}, # Duplicate, moved to this category
            {"name": "InVideo.io", "url": "https://invideo.io/", "description": "Text to video"},
        ],
        "🖌️ AI Image Editing": [
            {"name": "DeWatermark.ai", "url": "https://dewatermark.ai/it", "description": "DeWatermark.ai removes watermarks from images quickly and efficiently."},
            {"name": "MagicStudio", "url": "https://magicstudio.com/it/magiceraser/", "description": "MagicStudio offers AI tools for removing objects and backgrounds from images."},
            {"name": "Deep-Image.ai", "url": "https://deep-image.ai/", "description": "Deep-Image.ai provides AI-driven image upscaling and enhancement."},
        ],
        "🎵 AI Music Creation": [
            {"name": "Soundraw.io", "url": "https://soundraw.io/", "description": "Soundraw.io enables users to create original soundtracks using AI."},
            {"name": "Suno.ai", "url": "https://www.suno.ai/", "description": "Suno.ai generates music and lyrics with the help of AI."},
            {"name": "Udio.com", "url": "https://udio.com/", "description": "Udio.com allows for the creation of AI-generated songs with vocals."},
            # Added tool
            {"name": "Boomy.com", "url": "https://boomy.com/", "description": "Generate songs"},
        ],
        # Added subcategory
        "🎤 AI Voice Generation and Modification": [
            {"name": "The MetaVoice", "url": "https://themetavoice.xyz/", "description": "Generate voice from text"},
            {"name": "Voice.ai", "url": "https://voice.ai/", "description": "Clone voice"},
            {"name": "ElevenLabs", "url": "https://elevenlabs.io/", "description": "Create audio from text, very powerful"},
            {"name": "Speechki", "url": "https://speechki.org/", "description": "Create audio from text, very powerful"},
            {"name": "OpenVoice", "url": "https://github.com/myshell-ai/OpenVoice", "description": "Clone voices"},
            {"name": "Speechify", "url": "https://speechify.com/", "description": "Generate audio from text"},
        ],
        # Added subcategory
        "✏️ AI Writing and Storytelling": [
            {"name": "Napkin.ai", "url": "https://napkin.ai", "description": "Generate text and more"},
            {"name": "Machined.ai", "url": "https://machined.ai/", "description": "Write better articles"},
            {"name": "Ghost the Writer", "url": "https://www.ghostthewriter.com/", "description": "Generate horror stories"},
            {"name": "Storm Project", "url": "https://storm-project.stanford.edu/", "description": "Generate articles from topics"},
        ],
        # Added subcategory
        "🖼️ AI Comic and Animation Generation": [
            {"name": "Glif.app", "url": "https://glif.app/glifs", "description": "Generate vignettes automatically"},
            {"name": "MagicHour.ai", "url": "https://magichour.ai/", "description": "Make animated videos"},
            {"name": "Hedra.com", "url": "https://www.hedra.com/", "description": "Animate images with voice"},
            {"name": "AI Comic Factory", "url": "https://huggingface.co/spaces/jbilcke-hf/ai-comic-factory", "description": "Generate comics with AI"},
            {"name": "MythGen", "url": "https://github.com/elder-plinius/MythGen", "description": "Text-to-comic"},
        ],
    },
    "📈 AI Tools for Marketing": {
        "📱 AI for Social Media": [
            {"name": "Aiter.io", "url": "https://aiter.io/", "description": "Aiter.io specializes in creating AI-powered social media ads."},
            {"name": "Predis.ai", "url": "https://predis.ai/", "description": "Predis.ai generates social media posts and content within seconds."},
            {"name": "ContentStudio.io", "url": "https://contentstudio.io/", "description": "ContentStudio.io helps manage and create content for various social media platforms."},
            {"name": "Lately.ai", "url": "https://www.lately.ai/", "description": "Lately.ai automates the creation and management of social media content using AI."},
            # Added tools
            {"name": "Emplifi.io", "url": "https://emplifi.io/", "description": "Social media data analysis"},
            {"name": "Smartly.io", "url": "https://www.smartly.io/", "description": "Manage social campaigns across multiple platforms"},
            {"name": "NeoReach", "url": "https://neoreach.com/", "description": "Influencer marketing"},
        ],
        "📝 AI for Content Creation": [
            {"name": "Beautiful.ai", "url": "https://www.beautiful.ai/", "description": "Beautiful.ai creates stunning presentations and slides using AI."},
            {"name": "Simplified.com", "url": "https://simplified.com/", "description": "Simplified.com offers various AI tools for content creation and marketing."},
            {"name": "Fliki.ai", "url": "https://fliki.ai/", "description": "Fliki.ai converts text into engaging videos with AI-generated voiceovers."}, # Duplicate, already present
        ],
        # Added subcategory
        "💡 AI for Business Ideas and Analysis": [
            {"name": "VenturusAI", "url": "https://venturusai.com/", "description": "Test business ideas"},
            {"name": "Askpot", "url": "https://askpot.com/lp-analysis", "description": "Analyze competitors"},
            {"name": "Julius.ai", "url": "https://julius.ai/", "description": "Analyze your data, 15 free requests per month"},
            {"name": "Akkio.com", "url": "https://akkio.com/", "description": "Data analysis, including financial statements"},
        ],
    },
    # Added category
    "🛠️ General Purpose AI Tools": {
        "🧰 Multi-Purpose AI Tools": [
            {"name": "Fireflies.ai", "url": "https://fireflies.ai/", "description": "Transcribe video calls"},
            {"name": "YouAI", "url": "https://youai.ai/", "description": "Create AI apps"},
            {"name": "Max Browser", "url": "https://arc.net/max", "description": "Browser with built-in AI"},
            {"name": "Pickaxe Project", "url": "https://beta.pickaxeproject.com/", "description": "Create AI apps"},
            {"name": "TunnHQ", "url": "https://tunehq.ai/", "description": "Create AI applications"},
            {"name": "Databutton", "url": "https://databutton.com/", "description": "Create SaaS products with AI"},
            {"name": "Pickaxe Project", "url": "https://beta.pickaxeproject.com/", "description": "Create professional chatbots in seconds and sell them"},
            {"name": "SuperMemory.ai", "url": "https://supermemory.ai/", "description": "Memory for AI to store all your information"},
        ],
        "📚 Document and PDF Analysis": [
            {"name": "ChatDOC", "url": "https://chatdoc.com/", "description": "Query documents"},
            {"name": "PDF.ai", "url": "https://pdf.ai/tools", "description": "Query documents"},
            {"name": "PDF.ai", "url": "https://pdf.ai/", "description": "Query documents"},
            {"name": "Humata.ai", "url": "https://www.humata.ai/", "description": "Summarize PDFs and documents"},
        ],
        "🖼️ Image Upscaling and Enhancement": [
            {"name": "Upscayl", "url": "https://www.upscayl.org/", "description": "Upscale for free with AI"},
        ],
        "🌐 Website and App Creation": [
            {"name": "10Web", "url": "https://10web.io/", "description": "Create websites with AI"},
            {"name": "UIzard", "url": "https://uizard.io/", "description": "Create user interfaces"},
            {"name": "Framer", "url": "https://www.framer.com/features/ai/", "description": "Create websites with AI"},
            {"name": "Stunning.so", "url": "https://stunning.so/", "description": "Create websites"},
            {"name": "UI Magic", "url": "https://www.uimagic.io/", "description": "Create websites"},
            {"name": "BuildShip", "url": "https://buildship.com/", "description": "Create backends with AI"},
        ],
        "🤖 AI Chatbot Creation": [
            {"name": "ChatPersona.ai", "url": "https://chatpersona.ai/", "description": "Integrate chatbots for spicy profiles"},
            {"name": "FlirtFlow.ai", "url": "https://www.flirtflow.ai/", "description": "Chatbot for OnlyFans"},
            {"name": "CustomGPT", "url": "https://customgpt.ai/", "description": "Create chatbots with your own data"},
            {"name": "Chatbot Builder", "url": "https://www.chatbotbuilder.ai/", "description": "Create chatbots"},
            {"name": "DHTMLX Chatbot", "url": "https://dhtmlx.com/docs/products/dhtmlxChatbot/", "description": "Create chatbots"},
            {"name": "DeepChat.dev", "url": "https://deepchat.dev/", "description": "Create chatbots"},
            {"name": "NLUX", "url": "https://docs.nlkit.com/nlux", "description": "Create chatbots"},
            {"name": "ChatbotUI", "url": "https://www.chatbotui.com/", "description": "Create chatbots"},
            {"name": "Hugging Face Chat UI", "url": "https://github.com/huggingface/chat-ui", "description": "Create chatbots"},
            {"name": "Coze", "url": "https://www.coze.com/", "description": "Create RAG chatbots and more, no-code"},
        ],
        "🔬 AI Research and Experimentation": [
            {"name": "Replicate", "url": "https://replicate.com/explore", "description": "AI experiment platform"},
            {"name": "Playbrary.ai", "url": "https://playbrary.ai", "description": "Play with AI based on famous books"},
            {"name": "Civitai", "url": "https://civitai.com/", "description": "Train AI models"},
        ],
        "🔎 AI Search and Information Retrieval": [
            {"name": "Perplexica", "url": "https://github.com/ItzCrazyKns/Perplexica", "description": "Similar to Perplexity"},
            {"name": "OpenSearch AI", "url": "https://opensearch-ai.pages.dev/", "description": "Search the internet with AI"},
        ],
        "🎤 Audio and Video Transcription": [
            {"name": "TurboScribe.ai", "url": "https://turboscribe.ai/dashboard", "description": "Transcribe videos for free (3 per day, no length limits)"},
            {"name": "Replicate", "url": "replicate.com", "description": "Audio to text"},
            {"name": "Whisper for YouTube", "url": "https://www.youtube.com/", "description": "YouTube plugin that creates subtitles"}, # This needs a specific URL for the plugin
            {"name": "OpenAI Whisper", "url": "https://github.com/openai/whisper", "description": "Transcribe text from video and audio, free"},
        ],
        "🚓 AI Content Detection and Verification": [
            {"name": "NoPlagio", "url": "https://www.noplagio.it/", "description": "Check if text was created by AI"},
            {"name": "GenieAI", "url": "https://us.genieai.co/", "description": "Check legal documents"},
            {"name": "Hive Moderation", "url": "https://hivemoderation.com/ai-generated-content-detection", "description": "Check AI-generated content, including images"},
            {"name": "Originality.ai", "url": "https://originality.ai/", "description": "Detect if text was created by AI"},
            {"name": "VGlnt.ai", "url": "https://vglnt.ai/", "description": "Check fake news"},
        ],
        "🛠️ Other Useful AI Tools": [
            {"name": "Adobe Podcast", "url": "https://podcast.adobe.com/", "description": "Edit audio"},
            {"name": "SopCreator", "url": "https://www.sopcreator.com/", "description": "Create good intentions with AI"},
            {"name": "Feedly", "url": "https://feedly.com/", "description": "Finds news for you"},
            {"name": "HeyGen", "url": "https://www.heygen.com/", "description": "Translate videos into other languages"},
            {"name": "ElevenLabs Voice Isolator", "url": "https://elevenlabs.io/voice-isolator", "description": "Isolate noise and other problems from audio with voice"},
            {"name": "Graswald.ai", "url": "https://www.graswald.ai/", "description": "Generate 3D models of products (from video to 3D)"},
        ],
        # Removed subcategory
        # "⌨️ AI Keyboard Shortcuts and Commands": [],
    },
    # Added category
    "📚 AI Learning Resources": {
        "🧠 AI Prompt Libraries and Marketplaces": [
            {"name": "Semrush AI Prompt Library", "url": "https://www.semrush.com/goodcontent/ai-prompt-library/", "description": "Library of prompts"},
            {"name": "Content at Scale AI Prompt Library", "url": "https://contentatscale.ai/ai-prompt-library/", "description": "Library of prompts"},
            {"name": "AI for Work", "url": "https://www.aiforwork.co/", "description": "Prompt library"},
            {"name": "PromptHero", "url": "https://prompthero.com/", "description": "Prompt library"},
            {"name": "PromptIdeas", "url": "https://promptsideas.com/", "description": "Prompt marketplace"},
            {"name": "PromptBase", "url": "https://promptbase.com/", "description": "Prompt marketplace"},
            {"name": "Playground", "url": "https://playground.com/", "description": "Search for image prompts"},
        ],
        "🔬 AI Frameworks and Tools": [
            {"name": "Fabric AI Framework", "url": "https://github.com/danielmiessler/fabric?tab=readme-ov-file", "description": "AI framework"},
            {"name": "Continue.dev", "url": "https://www.continue.dev/", "description": "Tool for help on VSCode"},
            {"name": "Copilot Kit", "url": "https://www.copilotkit.ai/", "description": "Integrate AI into apps easily"},
            {"name": "Tribe", "url": "https://github.com/StreetLamb/tribe", "description": "Create multi-agents"},
            {"name": "LangFlow", "url": "https://github.com/langflow-ai/langflow", "description": "Create RAG (like Flowise)"},
            {"name": "AgentScope", "url": "https://agentscope.io/", "description": "Create agents"},
            {"name": "EDA-GPT", "url": "https://github.com/shaunthecomputerscientist/EDA-GPT", "description": "Analyze different types of data"},
            {"name": "L1B3RT45", "url": "https://github.com/elder-plinius/L1B3RT45", "description": "Jailbreak LLM"},
            {"name": "LangGraph Studio", "url": "https://github.com/langchain-ai/langgraph-studio", "description": "Agent IDE"},
            {"name": "LAgent", "url": "https://github.com/InternLM/lagent", "description": "Framework for agents"},
            {"name": "Agent Zero", "url": "https://github.com/frdel/agent-zero", "description": "Framework for creating agents"},
            {"name": "Claude Dev", "url": "https://github.com/saoudrizwan/claude-dev", "description": "IDE extension with Claude"},
            {"name": "Taipy", "url": "https://taipy.io/", "description": "Create full-stack apps"},
            {"name": "Deep Live Cam", "url": "https://github.com/hacksider/Deep-Live-Cam", "description": "Deep fake live cam"},
            {"name": "AI Artifacts", "url": "https://github.com/e2b-dev/ai-artifacts", "description": "Generate AI artifacts"},
            {"name": "ModelScope AgentScope", "url": "https://github.com/modelscope/agentscope", "description": "Create multi-agents"},
        ],
        "🎓 AI Tutorials and Courses": [
            # Add links to relevant tutorials and courses here
        ],
    },
    # Added category
    "🎨 AI Art and Design": {
        "🖼️ AI Image Generation and Manipulation": [
            {"name": "ArtFlow.ai", "url": "https://artflow.ai/", "description": "Create characters with the same features"},
            {"name": "BetterWaifu", "url": "https://betterwaifu.com/", "description": "NSFW AI"},
        ],
        "🖌️ AI Design and Mockup Generation": [
            {"name": "Flair.ai", "url": "https://flair.ai/", "description": "Generate mockups with your product"},
            {"name": "Gamma.app", "url": "https://gamma.app/", "description": "Create PowerPoints"},
            {"name": "Call to Inspiration", "url": "https://calltoinspiration.com/", "description": "Design models for various interfaces for websites and more"},
        ],
        "✏️ AI Drawing and Illustration": [
            {"name": "Excalidraw", "url": "https://excalidraw.com/", "description": "Create flowcharts"},
        ],
        "✒️ AI Font Generation": [
            {"name": "Fontjoy", "url": "https://fontjoy.com/", "description": "Create fonts for free"},
            {"name": "AICreate Font Generator", "url": "https://aicreate.com/font-generator/", "description": "Create fonts and other things"},
            {"name": "PageGPT AI Font Generator", "url": "https://pagegpt.pro/tools/ai-font-generator", "description": "Generate fonts"},
            {"name": "AI Font Generator", "url": "https://aifontgenerator.com/", "description": "Generate free fonts"},
            {"name": "Spinbot Font Generator", "url": "https://spinbot.com/font-generator", "description": "Generate free fonts"},
        ],
        "🖼️ AI Infographic Generation": [
            {"name": "AICreate Infographics Generator", "url": "https://aicreate.com/infographics-generator/", "description": "Generate infographics"},
        ],
        "💠 AI Logo Generation": [
            {"name": "PageGPT AI Logo Generator", "url": "https://pagegpt.pro/tools/ai-logo-generator", "description": "Generate logos"},
        ],
        "📱 AI UI and UX Design": [
            {"name": "Gemini UI to Code", "url": "https://github.com/Doriandarko/gemini-ui-to-code", "description": "Generate UI with Gemini's AI for free"},
            {"name": "Google Mesop", "url": "https://google.github.io/mesop/", "description": "Generate UI in Python"},
        ],
        "👓 AI Augmented Reality (AR)": [
            {"name": "RagApp", "url": "https://github.com/ragapp/ragapp", "description": "Create AR with your documents and also create the UI"},
        ],
        "🖼️ AI QR Code Generation": [
            {"name": "Illusion QR Code Generator", "url": "https://replicate.com/andreasjansson/illusion", "description": "Generate QR codes with beautiful images"},
        ],
    },
    # Added category
    "💼 AI for Business and Productivity": {
        "📈 AI Sales and Marketing": [
            {"name": "ExactBuyer", "url": "https://exactbuyer.com/", "description": "Checks if there are buyers I'm interested in and creates a profile for me"},
            {"name": "Growbots", "url": "https://growbots.com/", "description": "Checks if there are buyers I'm interested in and creates a profile for me"},
            {"name": "Clay", "url": "https://clay.com/", "description": "Outreach with AI"},
        ],
        "📊 AI Project Management": [
            {"name": "ItsDart", "url": "https://www.itsdart.com/", "description": "Project management with AI"},
            {"name": "Startup Business Model Generator", "url": "https://hokentech.gumroad.com/l/startup-business-model-generator", "description": "Creating a comprehensive business plan feels overwhelming and time-consuming for aspiring entrepreneurs"},
        ],
        "📝 AI Presentation and Document Creation": [
            {"name": "Guidde", "url": "https://www.guidde.com/", "description": "Create presentation videos or various documents"},
        ],
        "🧰 AI Workflow Automation": [
            {"name": "WordGenie2", "url": "https://go2.designrr.io/wordgenie2", "description": "Write ebooks from any source, lifetime plan costs $27 (08-04-2024)"},
        ],
        "🔢 AI Spreadsheet Automation": [
            {"name": "Numerous.ai", "url": "https://numerous.ai/", "description": "Google Sheets extension to write formulas and do things you don't know"},
        ],
        "🌐 AI Website Security": [
            {"name": "HostedScan", "url": "https://hostedscan.com/scans", "description": "Find vulnerabilities on web apps and websites"},
        ],
        "🐱 AI Pet Care": [
            {"name": "Carelogy Japan CPD", "url": "https://cpd.carelogy-japan.com/index/en", "description": "App that checks the physical condition of cats by photographing the cat's face (model with 6000 photos)"},
        ],
        "⚙️ AI Development Platforms": [
            {"name": "On-Demand.io", "url": "https://on-demand.io/", "description": "Platform for hosting models and RAG"},
        ],
    },
    # Added category
    "🚀 Advanced AI Concepts and Tools": {
        "🤖 AI Agents and Multi-Agent Systems": [
            {"name": "FlowiseAI", "url": "https://flowiseai.com/", "description": "Create apps with AI"},
            {"name": "FlowiseAI Github", "url": "https://github.com/FlowiseAI/Flowise", "description": "Create apps with AI"},
            {"name": "RagFlow", "url": "https://ragflow.io/", "description": "Create RAG"},
        ],
        "🧠 Large Language Model (LLM) Testing and Comparison": [
            {"name": "LMSYS Chat", "url": "https://chat.lmsys.org/", "description": "Allows you to test multiple chats together"},
            {"name": "LLM Testing", "url": "https://tide-freckle-52b.notion.site/1e0168e3481747ebaa365f77a3af3cc1?v=83e3d58d1c3c45ad879834981b8c2530", "description": "Allows you to test multiple chats together"},
       ],
        "🧠 Foundation Models and LLMs": [
            {"name": "Perplexity Labs", "url": "labs.perplexity.ai", "description": "Allows you to choose foundation models (LLMs)"},
            {"name": "GPTe.ai", "url": "https://gpte.ai/", "description": "Collection of AI tools"},
        ],
        "⛓️ AI Toolchains and Integrations": [
            {"name": "Vercel AI SDK", "url": "https://sdk.vercel.ai/", "description": "Use different AI chat models"},
        ],
        "🖥️ Local LLM Execution": [
            {"name": "Local LLM", "url": "https://ollama.com/", "description": "Run various LM models locally"}, # Duplicate, already present
        ],
        "🔌 AI Plugins and Extensions": [
            {"name": "Compose.ai", "url": "https://www.compose.ai/", "description": "Plugin to help write various things like emails"},
            {"name": "Sider.ai", "url": "https://sider.ai/en", "description": "AI assistant on every page with different chatbots"},
            {"name": "Engage AI", "url": "https://engage-ai.co/", "description": "Extension to write using AI on sites like comments and posts"},
        ],
        "🤖 AI-Powered Browsers": [
            {"name": "Arc Browser", "url": "https://arc.net/", "description": "Browser with AI features"}, # Duplicate, already present as "Max Browser"
        ],
        "🛠️ AI Development Tools and Frameworks": [
            {"name": "Pinokio", "url": "https://pinokio.computer/", "description": "Install various scripts and models with a single click"},
            {"name": "Changes to OpenInterpreter", "url": "https://changes.openinterpreter.com/log/local-iii", "description": "System for training with computer vision"},
        ],
        "💬 AI Chat and Conversational Interfaces": [
            {"name": "D-ID Chat", "url": "https://chat.d-id.com/", "description": "Talk to an AI avatar"},
        ],
        "📊 AI Data Analysis and Visualization": [
            {"name": "Mermaid Chart", "url": "https://www.mermaidchart.com/", "description": "Create mermaid diagrams"},
        ],
        "🖼️ AI-Powered Video Editing": [
            {"name": "Pitch", "url": "https://pitch.com/", "description": "Create pitch decks"},
        ],
        "💻 AI-Powered Code Editors and IDEs": [
            {"name": "CodePen", "url": "https://codepen.io/", "description": "Front-end development playground"},
        ],
        "📚 AI-Powered Learning Platforms": [
            {"name": "Wrtn.ai", "url": "https://wrtn.ai/", "description": "Use ChatGPT 4 for free (in Korean)"},
        ],
        "🚀 AI-Powered Template Libraries": [
            {"name": "TemplateMonster", "url": "https://www.templatemonster.com/monsterone/free-subscription/", "description": "Templates for every type of site"},
        ],
        "🛡️ AI-Powered Security Tools": [
            {"name": "BypassGPT", "url": "https://bypassgpt.ai/", "description": "Prevents analysis of text generated by AI"},
        ],
    },
}

# Streamlit UI
st.title("🔍 AI Tools Explorer by Hoken Tech")

# Sidebar with categories
st.sidebar.title("🗂️ Categories")

# Select category and subcategory
category_selected = st.sidebar.selectbox("Select a category", sorted(mind_map.keys()))
subcategory_selected = st.sidebar.selectbox("Select a subcategory", sorted(mind_map[category_selected].keys()))

# Display tools
st.subheader(f"{subcategory_selected} - {category_selected}")
tools = mind_map[category_selected][subcategory_selected]

# Two-column layout
col1, col2 = st.columns([1, 2])

with col1:
    st.write("### 📋 Tools List")
    for tool in tools:
        if st.button(f"🔗 {tool['name']}", key=tool['name']):
            st.session_state['selected_tool'] = tool

# Check if a tool is selected
if 'selected_tool' in st.session_state:
    selected_tool = st.session_state['selected_tool']
    with col1:
        st.write(f"**{selected_tool['name']}**")
        st.write(selected_tool['description'])
    with col2:
        st.write(f"### 🌐 {selected_tool['name']} Website")
        st.components.v1.iframe(selected_tool['url'], height=600, scrolling=True)
        # Adding a button to open the link in a new tab
        st.markdown(
            f'<a href="{selected_tool["url"]}" target="_blank" rel="noopener noreferrer">🔗 Open in New Tab</a>',
            unsafe_allow_html=True
        )
else:
    with col2:
        st.write("🔍 Select a tool to view more information and visit its website.")

# Adding vertical space for better UI
add_vertical_space(2)
