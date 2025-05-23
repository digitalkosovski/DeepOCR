# DeepOCR
A Python app that leverages Deepseek API for post-OCR correction.

## About
This experimental Python script builds on Tesseract to OCR image files and leverages the Deepseek API to correct mistakes coming from imperfect OCR-ization. It also has the option to provide a translation in English or French. Additionnally, it offers basic named-entity recognition by identifying the most common occurences of places and names in the text.

This experimental app is especially meant for historians who are using image files of their sources who need to improve defective OCR-ization, whether because the image is low-quality or because OCR-ization their respective language is particularly faulty. It is also practical for those who are in need of quick previews and translations to check whether these sources contain relevant information for their research and are therefore worth a more detailed exploration. 

The result is still imperfect and often inconsistent, but it does the trick. 

The downside is you need to have a Deepseek API key to run it. If you want to run the app on a [Hugging Face Space](https://huggingface.co/spaces), you need to have some basic coding skills. 

## Instructions 

### API key 

Remember to add your API key on the script:

<pre> client = OpenAI(
    api_key="YOUR API KEY",  # Replace with your DeepSeek API key
    base_url="https://api.deepseek.com/v1",
) </pre>

### Languages 
The languages for OCR are currently Serbian, Croatian, Greek, and Romanian, but that can easily be tuned in the script here:

<pre> language_map = {
    "English": "eng",
    "Serbian": "srp",
    "Croatian": "hrv",
    "Greek": "ell",
    "Romanian": "ron"
}
</pre>

### NER

The prompt for NER is tuned for documents concerning Southeast European history. Tune the prompt according to your need.

<pre> 
def entity_recog(text):
    lang_prompt = "TUNE YOUR PROMPT HERE"
</pre>

### Running the app

Option a) You can run the script on the command line to launch a web interface (in that case, the link will last 72hs). <br /> 
Option b) You can host the app on Hugging Face's Spaces to have permanent access.<br />

For both, having some understanding of the command line and Python will be of help.


