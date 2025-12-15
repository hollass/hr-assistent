from app.matching.similarity import cosine_sim


def test_cosine_similarity_identity():
    v = [1.0, 0.0, 0.0]
    assert cosine_sim(v, v) == 1.0

print(test_cosine_similarity_identity())
