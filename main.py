# Extract and organize data
genres = []
ratings = []

for movie in data:
    genre = movie["Genre"]
    rating = movie["Ratings"]["IMDB"]
    
    if genre and rating:
        genres.append(genre)
        ratings.append(rating)

# Convert to DataFrame
df = pd.DataFrame({"Genre": genres, "Rating": ratings})
grouped = df.groupby("Genre").mean().sort_values("Rating", ascending=False)

# Plot
plt.figure(figsize=(10,6))
grouped.plot(kind="bar", legend=False)
plt.title("Average IMDB Rating by Genre")
plt.ylabel("IMDB Rating")
plt.xlabel("Genre")
plt.tight_layout()
plt.show()
