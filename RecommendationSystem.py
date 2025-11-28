from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# 1. Create a combined text feature (Cuisines)
# Handling missing values in cuisines
df['Cuisines'] = df['Cuisines'].fillna('')

# 2. TF-IDF Vectorization (Converting text to numbers)
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['Cuisines'])

# 3. Compute Cosine Similarity Matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# 4. Recommendation Function
def get_recommendations(title, cosine_sim=cosine_sim):
    idx = df.index[df['Restaurant Name'] == title].tolist()[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6] # Top 5 similar restaurants
    restaurant_indices = [i[0] for i in sim_scores]
    return df['Restaurant Name'].iloc[restaurant_indices]

# Test
print(get_recommendations('Barbeque Nation'))
