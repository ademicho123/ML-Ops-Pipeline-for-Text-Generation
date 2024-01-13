import nltk
from nltk.translate.bleu_score import sentence_bleu

def calculate_bleu_score(candidate, reference):
    # Tokenize the sentences into lists of words
    candidate_tokens = nltk.word_tokenize(candidate.lower())
    reference_tokens = [nltk.word_tokenize(sentence.lower()) for sentence in reference]

    # Calculate BLEU score
    bleu_score = sentence_bleu(reference_tokens, candidate_tokens)

    return bleu_score

def evaluate_performance(model_output, baseline_model_output):
    # print the results
    print("Baseline GPT Output:", baseline_model_output)
    print("Your Model Output:", model_output)

    # Calculate BLEU score
    bleu_score = calculate_bleu_score(model_output, [baseline_model_output])
    print("\nBLEU Score:", bleu_score)

if __name__ == "__main__":
    # model output text here (replace with your LLM model output)
    model_output = "output text here..."                                    # Update with the right info

    # Baseline GPT output (replace with the actual baseline output)
    baseline_model_output = "baseline text here..."                         # Update with the right info

    # Evaluate the performance using BLEU score
    evaluate_performance(model_output, baseline_model_output)
