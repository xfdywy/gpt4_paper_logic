import os
import requests
api_key='78e997271b8844eea5f54a5ba6f9c941'
headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}
# pre = ""
# name = "Rethinking_GNN"
paper_file_name = 'making_better_decision_clean.tex'

with open('./papers/' + paper_file_name,'r') as g:
    paper = g.read()

with open('./demo/' + 'prompt_1_1.txt','r') as g:
    demo_prompt_1 = g.read()

with open('./demo/' + 'prompt_1_2.txt','r') as g:
    demo_prompt_2 = g.read()


payload_0 = {
    "messages": [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    
                    "text":   demo_prompt_1  ,
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"The  paper content is:\n{paper}\n\n"
                }
            ]
        }
    ],
    "temperature": 0.7,
    "top_p": 0.95,
    "max_tokens": 2000
}
GPT4V_ENDPOINT = "https://gcrgpt4aoai9c.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-02-15-preview"
# Send request
try:
    response = requests.post(GPT4V_ENDPOINT, headers=headers, json=payload_0)
    response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
except requests.RequestException as e:
    raise SystemExit(f"Failed to make the request. Error: {e}")
res = (response.json())['choices'][0]['message']['content']
print("done res!")
print(res)

import json

with open('./results/' + 'prompt_1_1_response.txt','w+') as g:
    # json.dump(payload_0,g)
    g.write(res)

payload_0 = {
    "messages": [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    
                    "text":   demo_prompt_2  ,
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"The  paper content is:\n{paper}\n\n"
                }
            ]
        }
    ],
    "temperature": 0.7,
    "top_p": 0.95,
    "max_tokens": 2000
}
GPT4V_ENDPOINT = "https://gcrgpt4aoai9c.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-02-15-preview"
# Send request
try:
    response = requests.post(GPT4V_ENDPOINT, headers=headers, json=payload_0)
    response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
except requests.RequestException as e:
    raise SystemExit(f"Failed to make the request. Error: {e}")
res = (response.json())['choices'][0]['message']['content']
print("done res!")
print(res)

import json

with open('./results/' + 'prompt_1_2_response.txt','w+') as g:
    # json.dump(payload_0,g)
    g.write(res)