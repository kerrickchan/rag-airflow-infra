from transformers import AutoTokenizer, RagRetriever, RagSequenceForGeneration
import torch

tokenizer = AutoTokenizer.from_pretrained("facebook/rag-sequence-nq")
retriever = RagRetriever.from_pretrained(
    "facebook/rag-sequence-nq", index_name="exact", use_dummy_dataset=True
)
# initialize with RagRetriever to do everything in one forward call
model = RagSequenceForGeneration.from_pretrained("facebook/rag-token-nq", retriever=retriever)

inputs = tokenizer("How many people live in Paris?", return_tensors="pt")
targets = tokenizer(text_target="In Paris, there are 10 million people.", return_tensors="pt")
input_ids = inputs["input_ids"]
labels = targets["input_ids"]
outputs = model(input_ids=input_ids, labels=labels)

print(outputs)
