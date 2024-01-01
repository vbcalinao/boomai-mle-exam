from transformers import AutoModel, AutoTokenizer

def get_model(model_name):
    model = AutoModel.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer
  
model, tokenizer = get_model(model_name="sentence-transformers/paraphrase-MiniLM-L6-v2")