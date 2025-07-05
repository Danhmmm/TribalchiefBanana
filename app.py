from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load model
tokenizer = AutoTokenizer.from_pretrained("tarudesu/ViHateT5-base-HSD")
model = AutoModelForSeq2SeqLM.from_pretrained("tarudesu/ViHateT5-base-HSD")

app = FastAPI()

class TextRequest(BaseModel):
    text: str

def clean_text(text):
    if not isinstance(text, str):
        text = str(text)
    return text.encode("utf-8", "ignore").decode("utf-8").strip()

@app.post("/check-toxicity")
def check_toxicity(req: TextRequest):
    text = clean_text(req.text)
    prefix = "toxic-speech-detection"
    input_text = f"{prefix}: {text}"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output_ids = model.generate(input_ids, max_length=256)
    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return {"result": output_text}
