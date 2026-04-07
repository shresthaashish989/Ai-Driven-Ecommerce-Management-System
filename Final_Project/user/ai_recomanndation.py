from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from product.models import *

def recommend_products(product_id, top_n=4):
    products = Product.objects.all()

    if products.count() < 2:
        return []

    corpus = []
    ids = []

    for p in products:
        text = f"{p.name} {p.description} {p.category.category_name} {p.gender}"
        corpus.append(text)
        ids.append(p.id)

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(corpus)

    # Get index of the selected product
    if product_id not in ids:
        return []

    idx = ids.index(product_id)

    cosine_sim = linear_kernel(tfidf_matrix[idx:idx+1], tfidf_matrix).flatten()

    # Sort by similarity
    similar_indices = cosine_sim.argsort()[::-1][1:top_n+1]
    recommended_ids = [ids[i] for i in similar_indices]

    return Product.objects.filter(id__in=recommended_ids)
