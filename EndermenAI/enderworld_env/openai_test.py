from openai import OpenAI

client = OpenAI(
  api_key="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"
)

response = client.responses.create(
  model="gpt-4o-mini",
  input="Whats todays temperature in Mumbai, Maharashtra",
  store=True,
)

print(response.output_text) 