import re
import math
from collections import defaultdict

class NaiveBayesClassifier:
    def __init__(self):
        self.classes = defaultdict(int)
        self.class_word_counts = defaultdict(lambda: defaultdict(int))
        self.class_total_words = defaultdict(int)
        self.vocab = set()

    def preprocess_text(self, text):
        # Limpeza de texto: remover pontuação e converter em minúsculas
        text = re.sub(r'[^\w\s]', '', text)
        text = text.lower()
        return text

    def tokenize_text(self, text):
        # Dividir o texto em palavras
        return text.split()

    def train(self, documents, labels):
        for doc, label in zip(documents, labels):
            doc = self.preprocess_text(doc)
            words = self.tokenize_text(doc)

            self.classes[label] += 1
            self.class_total_words[label] += len(words)

            for word in words:
                self.vocab.add(word)
                self.class_word_counts[label][word] += 1

    def predict(self, document):
        document = self.preprocess_text(document)
        words = self.tokenize_text(document)

        scores = defaultdict(float)
        for label in self.classes:
            score = math.log(self.classes[label] / sum(self.classes.values()))

            for word in words:
                if word in self.vocab:
                    word_prob = (self.class_word_counts[label][word] + 1) / (self.class_total_words[label] + len(self.vocab))
                    score += math.log(word_prob)

            scores[label] = score

        return max(scores, key=scores.get)

# Exemplo de uso
documents = [
    "Este é um ótimo filme",
    "A câmera do smartphone é excelente",
    "Gostei muito do atendimento no restaurante",
    "O serviço de entrega foi horrível",
    "A qualidade da comida deixou a desejar"
]
labels = ["positivo", "positivo", "positivo", "negativo", "negativo"]

classifier = NaiveBayesClassifier()
classifier.train(documents, labels)

# Classificar novos documentos
test_document = "O filme foi ruim"
predicted_label = classifier.predict(test_document)
print(f"Previsão: {predicted_label}")
