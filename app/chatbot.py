from transformers import pipeline

class RAGChatbot:
    def __init__(self, knowledge_base):
        self.qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
        self.knowledge_base = knowledge_base

    def get_answer(self, query):
        return self.qa_pipeline(question=query, context=self.knowledge_base)
