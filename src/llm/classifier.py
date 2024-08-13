from llm import llm


def classify(text: str, categories: list[str]) -> str:
    result = llm(text, categories)
    return result.labels, result.scores
