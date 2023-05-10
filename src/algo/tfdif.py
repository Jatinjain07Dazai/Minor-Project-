import os
from numpy import vectorize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Text1 = """A flower, sometimes known as a bloom or blossom, is the reproductive structure found in flowering plants (plants of the division Angiospermae). Flowers produce gametophytes, which in flowering plants consist of a few haploid cells which produce gametes. The "male" gametophyte, which produces non-motile sperm, is enclosed within pollen grains; the "female" gametophyte is contained within the ovule. When pollen from the anther of a flower is deposited on the stigma, this is called pollination. Some flowers may self-pollinate, producing seed using pollen from the same flower or a different flower of the same plant, but others have mechanisms to prevent self-pollination and rely on cross-pollination, when pollen is transferred from the anther of one flower to the stigma of another flower on a different individual of the same species.
# Self-pollination happens in flowers where the stamen and carpel mature at the same time, and are positioned so that the pollen can land on the flower's stigma. This pollination does not require an investment from the plant to provide nectar and pollen as food for pollinators.["""
# Text2 = """A flower, sometimes known as a bloom or blossom, is the reproductive structure found in flowering plants (plants of the division Angiospermae). Flowers produce gametophytes, which in flowering plants consist of a few haploid cells which produce gametes. The "male" gametophyte, which produces non-motile sperm, is enclosed within pollen grains; the "female" gametophyte is contained within the ovule. When pollen from the anther of a flower is deposited on the stigma, this is called pollination. Some flowers may self-pollinate, producing seed using pollen from the same flower or a different flower of the same plant, but others have mechanisms to prevent self-pollination and rely on cross-pollination, when pollen is transferred from the anther of one flower to the stigma of another flower on a different individual of the same species.
# Self-pollination h"""


# sample_files = [doc for doc in os.listdir() if doc.endswith('.txt')]
# sample_contents = [open(File).read() for File in sample_files]

# sample_files = ["text1", "text2"]
# sample_contents = [Text1, Text2]
# vectorize = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()
# simmilarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])

# vectors = vectorize(sample_contents)
# s_vectors = list(zip(sample_files, vectors))

def check_plagiarism(target, candidate):
	sample_files = ['target', 'candidate']
	sample_contents = [target, candidate]
	vectorize = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()
	simmilarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])
	vectors = vectorize(sample_contents)
	s_vectors = list(zip(sample_files, vectors))
	results = set()
	for sample_a, text_vector_a in s_vectors:
		new_vectors = s_vectors.copy()
		current_index = new_vectors.index((sample_a, text_vector_a))
		del new_vectors[current_index]
		for sample_b, text_vector_b in new_vectors:
			sim_score = simmilarity(text_vector_a, text_vector_b)[0][1]
			sample_pair = sorted((sample_a, sample_b))
			score = sample_pair[0], sample_pair[1], sim_score
			results.add(score)
	return results


