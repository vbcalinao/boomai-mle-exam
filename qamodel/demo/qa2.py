import json

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

print ("Number of available questions: {}".format(len(questions)))