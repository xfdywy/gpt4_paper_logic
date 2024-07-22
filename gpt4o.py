import os
import requests
api_key=os.getenv("OPENAI_API_KEY")
headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}
pre = ""
name = "Rethinking_GNN"
with open('./papers/'+name+'_abs.txt','r') as g:
    abs = g.read()
    print(abs)
    payload_0 = {
        "messages": [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        
                        "text": "Here is an abstract of a paper. Your next task is to summarize this paper. So now ,based on this abstract you need to reason a basic chain of logic to guide you on how you should summarize this paper next. And, you also need to ask some questions about the unclear areas(for example, some specific data that can indicate some conclusion) described in the abstract and expect to find them in the body. "
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": abs
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
    pre = (response.json())['choices'][0]['message']['content']
print("done pre!")
# pre = "To summarize the paper effectively, I should establish a clear chain of logic based on the abstract:\n1. **Introduction of the Issue**: Start by explaining the emergence of SARS-CoV-2 and the resulting COVID-19 pandemic.\n2. **Problem Statement**: Highlight the challenges in developing new antiviral treatments and vaccines in a timely manner.\n3. **Solution Approach**: Discuss the strategy of drug repurposing as a means to accelerate the discovery of effective treatments.4. **Methodology**: Describe the large-scale screening of approximately 12,000 clinical-stage or FDA-approved small molecules to identify potential antiviral drugs.5. **Findings**: Summarize the identification of 100 molecules that inhibit viral replication, with a focus on the 21 drugs showing dose-response relationships and the 13 drugs with effective concentrations.     6. **Key Results**: Emphasize the specific drugs that showed promising results, particularly in human pneumocyte-like cells and a human lung explant model.7. **Implications**: Discuss the significance of these findings, particularly the potential for accelerated preclinical and clinical evaluation due to existing pharmacological and safety profiles.### Questions to Address in the Body1. **Screening Process**: How was the library of 12,000 compounds screened for antiviral activity against SARS-CoV-2?2. **Selection Criteria**: What criteria were used to determine the dose-response relationships and effective concentrations of the identified drugs?3. **Mechanisms of Action**: What are the mechanisms by which the identified drugs, such as apilimod and the cysteine protease inhibitors, inhibit viral replication?4. **Cell Models Used**: What are the characteristics of the human pneumocyte-like cells derived from H9 human embryonic stem cell lines?5. **Efficacy Testing**: How was the antiviral efficacy of apilimod and other drugs tested in the primary human lung explant model?6. **Clinical Potential**: What are the known pharmacological and safety profiles of the identified drugs, and how might these profiles facilitate their rapid deployment for COVID-19 treatment?"
with open("./papers/"+ name +".txt",'r', encoding='utf-8') as f:
    content = f.read()
    # Payload for the request
    payload = {
        "messages": [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "Here is a paper that you need to summarize. You only need to extract information from this paper, and please organize summary logically, with detailed evience and specific data from this paper that can support the result (for example if a conclusion says something shows some efficacy, then you need to provide specific data from paper to prove this. e.g. Percentage, time, ... ). You may try this logic chain, and try to answer these questions in your summary. I want your summary is a few paragraphs rather than a point-by-point conclusion. " + pre
                        # "text": "You are a scientist that is going to read some science paper. You need to give user a report about this paper. You should mainly focus on the entities appear in this paper, then you need to give an explanation about them, and the relation between these entities. Finally you need to tell the user what and how we can get conclusions with these entities and relations."
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": content
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
        response = requests.post(GPT4V_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.RequestException as e:
        raise SystemExit(f"Failed to make the request. Error: {e}")

    # Handle the response as needed (e.g., print or process)
    with open('./papers/' + name + '_summary.txt','w',encoding='utf-8') as fw:
        print((response.json())['choices'][0]['message']['content'],file=fw)