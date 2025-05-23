import gradio as gr
from openai import OpenAI
from PIL import Image
import pytesseract

# Initialize the DeepSeek client
client = OpenAI(
    api_key="YOUR API KEY",
    base_url="https://api.deepseek.com/v1",
)

# Map display names to Tesseract language codes
language_map = {
    "English": "eng",
    "Serbian": "srp",
    "Croatian": "hrv",
    "Greek": "ell",
    "Romanian": "ron"
}

# OCR the image with selected language
def ocr_image(image, lang_code):
    text = pytesseract.image_to_string(image, lang=lang_code)
    return text

# Correct the OCR with DeepSeek
def correct_OCR(text):
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for a researcher working on the contemporary history of Southeast Europe. Considering the history of the region, you check and correct spelling mistakes in defective OCR text that comes from old newspapers. Please do not rewrite, nor summarize, nor reorganize the text."},
                {"role": "user", "content": f"Content:\n{text}"}
            ],
            temperature=0.7,
        )
        ds_text = response.choices[0].message.content.strip()
        return ds_text
    except Exception as e:
        print(f"Error while correcting OCR: {e}")
        return text

# Translate into English or French
def translate(text, target_language="English"):
    lang_prompt = "Translate this text into English." if target_language == "English" else "Translate this text into French."
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": lang_prompt},
                {"role": "user", "content": f"{text}"}
            ],
            temperature=0.7,
        )
        ds_text = response.choices[0].message.content.strip()
        return ds_text
    except Exception as e:
        print(f"Error while translating text: {e}")
        return text

# Recognize places and names

def entity_recog(text):
    lang_prompt = "You are a historian of contemporary Southeast European history. With your knowledge of the context, now go through this text and identify all places and people. Provide them respectively in two lists with their corresponding count in absolute numbers. Do not add any supplementary information."
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": lang_prompt},
                {"role": "user", "content": f"{text}"}
            ],
            temperature=0.7,
        )
        ds_text = response.choices[0].message.content.strip()
        return ds_text
    except Exception as e:
        print(f"Error while recognizing entities: {e}")
        return text



# Main logic
def process_image(image, language_label, translate_text=False, target_language="English"):
    lang_code = language_map.get(language_label, "eng")
    text = ocr_image(image, lang_code)
    corrected_text = correct_OCR(text)
    entities = entity_recog(text)
    if translate_text:
        translated_text = translate(corrected_text, target_language)
    else:
        translated_text = ""

    return text, corrected_text, translated_text, entities

# Gradio interface
iface = gr.Interface(
    fn=process_image,
    inputs=[
        gr.Image(type="pil"),
        gr.Dropdown(choices=list(language_map.keys()), label="OCR Language", value="English"),
        gr.Checkbox(label="Translate"),
        gr.Dropdown(choices=["English", "French"], label="Target Translation Language", value="English")
    ],
    outputs=[
        gr.Textbox(label="Original OCR"),
        gr.Textbox(label="Corrected OCR"),
        gr.Textbox(label="Translated Corrected OCR (if selected)"),
        gr.Textbox(label="Entities")
    ],
    title="OCR, Translation, and NER for Archival Sources",
    description="Upload an image, select OCR language, correct the OCR text, and optionally translate it to English or French."
)

if __name__ == '__main__':
    iface.launch(share=True)
