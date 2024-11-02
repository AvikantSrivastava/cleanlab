import pandas as pd
import spacy

class GrammarChecker:
    def __init__(self) -> None:
        # Load the English language model
        self.nlp = spacy.load("en_core_web_sm")

    def score(self, texts: list) -> float:
        """Evaluate the grammar of the given texts and return a grammar score between 0 and 1."""
        total_score = 0
        total_texts = len(texts)

        for text in texts:
            doc = self.nlp(text)

            errors = 0
            # Check for common errors
            if text and not text[0].isupper():
                errors += 1  # Sentence should start with a capital letter

            if not text.endswith('.'):
                errors += 1  # Sentence should end with a period

            # Identify grammatical issues based on dependency parsing
            for token in doc:
                if token.dep_ == "punct" and token.text == ',':
                    # Check for misplaced commas (very simplistic check)
                    if token.i > 0 and doc[token.i - 1].dep_ not in ["conj", "cc"]:
                        errors += 1

            # Calculate a score based on the number of errors
            score = 1 - (errors / max(2, len(doc)))  # Maximum 2 basic errors, avoid division by zero
            total_score += score

        # Return the average score for all texts
        return total_score / total_texts if total_texts > 0 else 0.0

    def assess_dataframe(self, dataframe: pd.DataFrame, text_column: str) -> pd.DataFrame:
        """Evaluate grammar for each text in the DataFrame and return an overall score."""
        overall_score = self.score(dataframe[text_column].tolist())

        # Add overall score as a new column
        dataframe['grammar_score'] = overall_score
        return dataframe
