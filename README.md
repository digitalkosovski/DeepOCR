# DeepOCR
A Python app that uses Deepseek API to improve OCR. 

This Python script builds on Tesseract to OCR image files and it uses the Deepseek API to correct mistakes coming from imperfect OCR-ization. The web interface builds on Gradio.

The languages for OCR are currently Serbian, Croatian, Greek, and Romanian, but that can easily be tuned in the script. The same goes for the languages of translation, which are currently English and French.

The app is especially meant for historians using image files of their archival or press sources, who are in need of quick previews and translations to check whether these sources contain relevant information for their research and are therefore worth a more detailed exploration. The OCR is still imperfect, but it does the trick.

