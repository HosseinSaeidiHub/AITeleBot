"""
Wrapper around GPT or other NLP models.
"""
class NLPModel:
    def __init__(self, model_path: str):
        self.model_path = model_path
        # load model…

    def generate(self, prompt: str) -> str:
        # TODO: implement generation
        return "Generated text"
