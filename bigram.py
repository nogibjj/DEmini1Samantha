
import random

def predict_word():
    return "the"
def predict_bigram(previous_word: str) -> dict[str, float]:
    return {
        "dinosaur":{"the":0.3,"of": 0.6, "dinosaur": 0.1},
        "of":{"the":0.6,"of": 0.1, "dinosaur": 0.3},
        "the":{"the":0.1,"of": 0.3, "dinosaur": 0.6}

    }[previous_word]


def sample_from_distribution(dist:dict[str,float],k:int):
    """Sample from distribution"""
    population = list(dist.keys())
    weights = list(dist.values())
    print(population, weights)
    return random.choices(population, weights,k=k)
     


if __name__ == "__main__":
    print(predict_word())
    print(predict_bigram("the"))
    print(sample_from_distribution(predict_bigram("the"),20))

