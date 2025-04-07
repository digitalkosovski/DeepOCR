# DeepOCR
A Python app that uses Deepseek API to improve OCR.

## About
This Python script builds on Tesseract to OCR image files and it uses the Deepseek API to correct mistakes coming from imperfect OCR-ization. It also has the option to provide a translation in English or French.

The app is especially meant for historians using image files of their archival or press sources, who are in need of quick previews and translations to check whether these sources contain relevant information for their research and are therefore worth a more detailed exploration. The OCR is still imperfect, but it does the trick. The downside is you need to have a Deepseek API key to run it.

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

### Running the app

Option a) You can run the script on the terminal to launch a web interface (in that case, the link will last 72hs) <br /> 
Option b) You can host the app on Hugging Face's Spaces to have permanent access.


