import sys

import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

model_id = "amazon.nova-micro-v1:0"

inferenceConfig = {"maxTokens": 2048, "temperature": 0.4, "topP": 0.9}

prompt = ""
if len(sys.argv) == 2:
    prompt = sys.argv[1]
else:
    for line in sys.stdin:
        prompt += line

print(prompt)

conversation = [
    {
        "role": "user",
        "content": [{"text": prompt}],
    }
]


def invoke_model(conversation):
    try:
        response = client.converse(
            modelId=model_id, messages=conversation, inferenceConfig=inferenceConfig
        )

        return response["output"]["message"]["content"][-1]["text"]

    except (ClientError, Exception) as e:
        print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
        exit(1)


response_text = invoke_model(conversation)
print(response_text)

refinement_text = input("Provide refinement? ")

if refinement_text and refinement_text not in ["q", "quit"]:
    conversation.append(
        {
            "role": "user",
            "content": [{"text": refinement_text}],
        }
    )

    refinement_response = invoke_model(conversation)

    print(refinement_response)
