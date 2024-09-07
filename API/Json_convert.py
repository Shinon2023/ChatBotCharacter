import json

def load_conversation_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    conversation = []
    
    for item in data:
        conversation.append(f"input: {item['input']}")
        conversation.append(f"output: {item['output']}")
    return conversation

conversation = load_conversation_from_json('Data/Mie Ai/conversation_data.json')

for line in conversation:
    print(line)