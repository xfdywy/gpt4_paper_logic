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

with open('./demo/' + 'paper_1.txt','r') as g:
    demo_paper_1 = g.read()

with open('./demo/' + 'summary_1.txt','r') as g:
    demo_summary_1 = g.read()


payload_0 = {
    "messages": [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    
                    "text": "I will first give you a demo paper and a demo summary of the same paper. Your task is to carefully read both the paper and the summary, and then understand which information from the main body of the paper is extracted in the summary and according to what logic it is written. Based on the above example, I will then give you another new paper, and I will ask you to write a new summary for the new paper by following the example."     
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"The demo paper content is:\n{demo_paper_1}\n\nThe demo summary content is:\n{demo_summary_1}\n\nThe new paper content is:\n{paper}\n\n"
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
with open('./results/' + 'summary_oneshot.txt','w') as g:
    # json.dump(payload_0,g)
    g.write(res)
# payload_1 =  payload_0

# payload_1['messages'].append(
#     response.json()['choices'][0]['message']    
# )
# payload_1['messages'].append(
#     {
#         "role": "user",
#         "content": [
#             {
#                 "type": "text",
#                 "text": "You make a good point. Can you please help me to summarize a paragraph prompt that I can directly use according to you response before. "                             }
#         ]
#     }
# )


# response = requests.post(GPT4V_ENDPOINT, headers=headers, json=payload_1)
# pre = (response.json())['choices'][0]['message']['content']
# print(pre)

# with open('./demo/' + 'prompt_1_1.txt','w') as g:
#     g.write(pre)
