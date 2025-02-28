import sys

import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="eu-west-1")

# Set the model ID, e.g., Mistral Large.
model_id = "mistral.mistral-7b-instruct-v0:2"

inferenceConfig = {"maxTokens": 512, "temperature": 0.4, "topP": 0.9}

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

try:
    response = client.converse(
        modelId=model_id, messages=conversation, inferenceConfig=inferenceConfig
    )

    response_text = response["output"]["message"]["content"][0]["text"]
    print(response_text)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)
