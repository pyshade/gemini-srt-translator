import os
from dotenv import load_dotenv
import gemini_srt_translator as gst

def get_model_selection():
    AVAILABLE_MODELS = [
        "gemini-1.5-pro",
        "gemini-1.5-flash"
    ]
    
    print("\nAvailable Gemini models:")
    for i, model in enumerate(AVAILABLE_MODELS, 1):
        print(f"{i}. {model}")
    
    while True:
        try:
            choice = int(input("\nSelect model number (1-2): "))
            if 1 <= choice <= len(AVAILABLE_MODELS):
                return AVAILABLE_MODELS[choice - 1]
            print("Invalid selection. Please choose 1 or 2.")
        except ValueError:
            print("Please enter a valid number.")

def get_target_language():
    SUPPORTED_LANGUAGES = [
        "Russian", "German", "French", "English", "Italian", 
        "Spanish", "Polish", "Ukrainian", "Romanian", "Dutch",
        "Greek", "Hungarian", "Portuguese", "Czech", "Swedish"
    ]
    
    print("\nAvailable languages for translation:")
    for i, lang in enumerate(SUPPORTED_LANGUAGES, 1):
        print(f"{i}. {lang}")
    
    while True:
        try:
            choice = int(input("\nSelect language number (1-15): "))
            if 1 <= choice <= len(SUPPORTED_LANGUAGES):
                return SUPPORTED_LANGUAGES[choice - 1]
            print("Invalid selection. Please choose a number between 1 and 15.")
        except ValueError:
            print("Please enter a valid number.")

# Load environment variables
load_dotenv()

# Verify API key
api_key = os.getenv('GEMINI_API_KEY')
print(f"API Key found: {'Yes' if api_key else 'No'}")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

# Get model and language selections
model_name = get_model_selection()
target_language = get_target_language()

# Configure translator
gst.model_name = model_name
gst.target_language = target_language
gst.input_file = "test.srt"

# Execute translation
try:
    gst.translate()
    print(f"\nTranslation to {target_language} using {model_name} completed successfully!")
    print("Check the translated file in the same directory")
except Exception as e:
    print(f"Error during translation: {e}")