import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

data = {
    'User': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'D', 'D'],
    'Movie': ['Matrix', 'StarWars', 'Titanic', 'Matrix', 'StarWars', 'Avatar', 
              'Titanic', 'Avatar', 'NottingHill', 'Matrix', 'Titanic'],
    'Rating': [5, 4, 1, 5, 5, 2, 2, 5, 4, 4, 1]
}

df = pd.DataFrame(data)
print("Original Dataset:\n", df)

user_movie_matrix = df.pivot_table(index='User', columns='Movie', values='Rating').fillna(0)
print("\nUser-Item Matrix:\n", user_movie_matrix)

movie_similarity = cosine_similarity(user_movie_matrix.T)
movie_similarity_df = pd.DataFrame(movie_similarity, 
                                   index=user_movie_matrix.columns, 
                                   columns=user_movie_matrix.columns)
print("\nMovie Similarity Matrix:\n", movie_similarity_df)

def get_recommendations(movie_name, similarity_matrix):
    similarity_scores = similarity_matrix[movie_name]
    
    recommendations = similarity_scores.sort_values(ascending=False).iloc[1:]
    return recommendations

target_movie = 'Matrix'
recommendations = get_recommendations(target_movie, movie_similarity_df)

print(f"\nBecause you watched '{target_movie}':")
print(recommendations.head(3))