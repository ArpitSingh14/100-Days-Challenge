chunks = [
    {
        "text": "FastAPI is a Python web framework.",
        "score": 0.92
    },
    {
        "text": "Redis is an in-memory database.",
        "score": 0.87
    },
    {
        "text": "PostgreSQL is a relational database.",
        "score": 0.81
    }
]
print(chunks[0]["text"])
print(chunks[0]["score"])
print(chunks[1]["text"])
print(chunks[1]["score"])
print(chunks[2]["text"])
print(chunks[2]["score"])
def high_score(chunks):
    max_score = 0
    for chunk in chunks:
        if chunk["score"] > max_score:
            max_score = chunk["score"]
    return max_score
print(high_score(chunks))

def selected_score(chunks):
    selected_chunks = []
    for chunk in chunks:
        if chunk["score"] > 0.85:
            selected_chunks.append(chunk)
    return selected_chunks
print(selected_score(chunks))