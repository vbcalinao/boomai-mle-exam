import torch
import json
from transformers import AutoModel, AutoTokenizer

def get_model(model_name):
    model = AutoModel.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer
  
model, tokenizer = get_model(model_name="sentence-transformers/paraphrase-MiniLM-L6-v2")

with open(r"C:\Users\victo\Git\vbcalinao\boomai-mle\1-qapytorch\train-v2.0.json") as f:
    data = json.load(f)

# Get the available questions and answers for a given topic
def get_qa(topic,data):
    q = []
    a = []
    for d in data['data']:
        if d['title']==topic:
            for paragraph in d['paragraphs']:
                for qa in paragraph['qas']:
                    if not qa ['is_impossible']:
                        q.append(qa['question'])
                        a.append(qa['answers'][0]['text'])
            return q,a
    
questions, answers = get_qa(topic='Premier_League', data=data)

# Mean Pooling - Take attention mask into account for correct averaging
# source: https://huggingface.co/sentence-transformers/paraphrase-MiniLM-L6-v2
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0]
    
    input_mask_expanded = (
      attention_mask
      .unsqueeze(-1)
      .expand(token_embeddings.size())
      .float()
    )
    
    pool_emb = (
      torch.sum(token_embeddings * input_mask_expanded, 1) 
      / torch.clamp(input_mask_expanded.sum(1), min=1e-9)
    )
    
    return pool_emb

def get_embeddings(questions, tokenizer, model):
  # Tokenize sentences
  encoded_input = tokenizer(questions, padding=True, truncation=True, return_tensors='pt')

  # Compute token embeddings
  with torch.no_grad():
      model_output = model(**encoded_input)

  # Average pooling
  embeddings = mean_pooling(model_output, encoded_input['attention_mask']) 
  
  return embeddings

embeddings = get_embeddings(questions[:3], tokenizer, model)

new_question = 'Which days have the most events played at?'
new_embedding = get_embeddings([new_question], tokenizer, model)

# squared Euclidean distance between sample questions and new_question
new_embeddings = ((embeddings - new_embedding)**2).sum(axis=1)
print(new_embeddings)