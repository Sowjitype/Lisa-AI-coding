import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from textblob import TextBlob
from colorama import init, Fore
import time

# Initialize colorama
init(autoreset=True)

def load_data():
    try:
        df = pd.read_csv(r"C:\Users\DIY\Desktop\lisa study\CODING\Lisa AI coding\L06\imdb_top_1000.csv")
        # Clean and prepare data
        df['combined_features'] = df['Genre'].fillna('') + ' ' + df['Overview'].fillna('')
        df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')  # Clean decade data
        df['Runtime'] = df['Runtime'].str.extract(r'(\d+)').astype(float)  # Extract minutes (e.g., 120 min → 120)
        return df
    
    except FileNotFoundError:
        print(Fore.RED + f"Error: The file 'imdb_top_1000.csv' was not found.")
        exit()

movies_df = load_data()

# Vectorize (unused in current code but kept for future use)
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies_df['combined_features'])

# List all unique genres (sorted for consistent numbering)
def list_genres(df):
    unique_genres = set(genre.strip() for sublist in df['Genre'].dropna().str.split(', ') for genre in sublist)
    return sorted(unique_genres)

genres = list_genres(movies_df)

# Get unique decades for user input
def list_decades(df):
    valid_years = df['Released_Year'].dropna()
    decades = sorted(set((year // 10) * 10 for year in valid_years if year >= 1900))
    return [f"{decade}s" for decade in decades]

decades = list_decades(movies_df)

# Recommend movies with enhanced filters
def recommend_movies(
    genre=None, mood=None, rating=None, actor=None, 
    decade=None, duration=None, award_winning=None, top_n=5
):
    filtered_df = movies_df.copy()
    
    # Apply core filters
    if genre:
        filtered_df = filtered_df[filtered_df['Genre'].str.contains(genre, case=False, na=False)]
    if rating:
        filtered_df = filtered_df[filtered_df['IMDB_Rating'] >= rating]
    
    # New: Actor/Actress filter
    if actor:
        filtered_df = filtered_df[
            filtered_df['Star1'].str.contains(actor, case=False, na=False) |
            filtered_df['Star2'].str.contains(actor, case=False, na=False) |
            filtered_df['Star3'].str.contains(actor, case=False, na=False) |
            filtered_df['Star4'].str.contains(actor, case=False, na=False)
        ]
    
    # New: Decade filter
    if decade:
        decade_num = int(decade.replace('s', ''))  # "1990s" → 1990
        filtered_df = filtered_df[
            (filtered_df['Released_Year'] >= decade_num) & 
            (filtered_df['Released_Year'] < decade_num + 10)
        ]
    
    # New: Duration filter (short: <100min, medium: 100-140min, long: >140min)
    if duration:
        if duration == 'short':
            filtered_df = filtered_df[filtered_df['Runtime'] < 100]
        elif duration == 'medium':
            filtered_df = filtered_df[(filtered_df['Runtime'] >= 100) & (filtered_df['Runtime'] <= 140)]
        elif duration == 'long':
            filtered_df = filtered_df[filtered_df['Runtime'] > 140]
    
    # New: Award-winning filter (based on Meta_score or Awards column if available)
    if award_winning:
        # Use Meta_score as proxy for award-winning (adjust if your CSV has an "Awards" column)
        filtered_df = filtered_df[filtered_df['Meta_score'] >= 80]
    
    # Early exit if no movies match filters
    if filtered_df.empty:
        return "No suitable movie recommendations found."
    
    filtered_df = filtered_df.sample(frac=1)  # Randomize order
    recommendations = []
    user_polarity = TextBlob(mood).sentiment.polarity if mood else 0

    for idx, row in filtered_df.iterrows():
        overview = row['Overview']
        if pd.isna(overview):
            continue
        polarity = TextBlob(overview).sentiment.polarity

        # Match mood (if provided)
        if (mood and abs(polarity - user_polarity) <= 0.5) or not mood:
            recommendations.append((row['Series_Title'], polarity))
            if len(recommendations) == top_n:
                break

    return recommendations if recommendations else "No suitable movie recommendations found."

# Display recommendations
def display_recommendations(recs, name):
    print(Fore.YELLOW + f"\n🍿 AI-Analyzed Movie Recommendations for {name}:")
    for idx, (title, polarity) in enumerate(recs, 1):
        sentiment = "Positive 😊" if polarity > 0 else "Negative 😞" if polarity < 0 else "Neutral 😐"
        print(f"{Fore.CYAN}{idx}. 🎥 {title} (Polarity: {polarity:.2f}, {sentiment})")

# Small processing animation
def processing_animation():
    for _ in range(3):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)

# Handle AI recommendation flow with more questions
def handle_ai(name):
    print(Fore.BLUE + "\n🔍 Let's find the PERFECT movie for you! Answer a few quick questions...\n")

    # 1. Genre (existing logic, improved)
    genre_list = [f"{idx}. {genre}" for idx, genre in enumerate(genres, 1)]
    print(Fore.GREEN + "Available Genres: " + Fore.CYAN + ", ".join(genre_list))  
    print()
    while True:
        genre_input = input(Fore.YELLOW + "1. Enter genre number or name: ").strip()
        if genre_input.isdigit():
            genre_idx = int(genre_input) - 1
            if 0 <= genre_idx < len(genres):
                genre = genres[genre_idx]
                break
        elif any(genre_input.lower() == g.lower() for g in genres):
            genre = next(g for g in genres if g.lower() == genre_input.lower())
            break
        print(Fore.RED + "Invalid input. Try again.\n")

    # 2. Mood (existing logic)
    mood = input(Fore.YELLOW + "\n2. How do you feel today? (e.g., happy, sad, adventurous): ").strip()
    print(Fore.BLUE + "\nAnalyzing mood", end="", flush=True)
    processing_animation()
    polarity = TextBlob(mood).sentiment.polarity if mood else 0
    mood_desc = "positive 😊" if polarity > 0 else "negative 😞" if polarity < 0 else "neutral 😐"
    print(f"\n{Fore.GREEN}Your mood is {mood_desc} (Polarity: {polarity:.2f}).\n")

    # 3. Favorite Actor/Actress (NEW)
    actor = input(Fore.YELLOW + "3. Any favorite actor/actress? (e.g., Tom Hanks, Scarlett Johansson) or 'skip': ").strip()
    actor = None if actor.lower() == 'skip' else actor

    # 4. Preferred Decade (NEW)
    print(Fore.GREEN + f"\nAvailable Decades: {Fore.CYAN}{', '.join(decades)}")
    while True:
        decade_input = input(Fore.YELLOW + "4. Preferred movie decade (e.g., 1990s) or 'skip': ").strip()
        if decade_input.lower() == 'skip':
            decade = None
            break
        elif decade_input in decades:
            decade = decade_input
            break
        print(Fore.RED + f"Invalid decade. Choose from: {', '.join(decades)}\n")

    # 5. Movie Duration (NEW)
    while True:
        duration_input = input(Fore.YELLOW + "\n5. Preferred duration? (short: <100min, medium: 100-140min, long: >140min) or 'skip': ").strip().lower()
        if duration_input == 'skip':
            duration = None
            break
        elif duration_input in ['short', 'medium', 'long']:
            duration = duration_input
            break
        print(Fore.RED + "Invalid input. Choose 'short', 'medium', 'long', or 'skip'.\n")

    # 6. Award-Winning Movies (NEW)
    while True:
        award_input = input(Fore.YELLOW + "\n6. Want award-winning movies? (yes/no): ").strip().lower()
        if award_input in ['yes', 'no']:
            award_winning = (award_input == 'yes')
            break
        print(Fore.RED + "Invalid input. Choose 'yes' or 'no'.\n")

    # 7. Minimum IMDB Rating (existing logic)
    while True:
        rating_input = input(Fore.YELLOW + "\n7. Enter minimum IMDB rating (7.6-9.3) or 'skip': ").strip()
        if rating_input.lower() == 'skip':
            rating = None
            break
        try:
            rating = float(rating_input)
            if 7.6 <= rating <= 9.3:
                break
            print(Fore.RED + "Rating out of range. Try again.\n")
        except ValueError:
            print(Fore.RED + "Invalid input. Try again.\n")

    # Find recommendations
    print(f"{Fore.BLUE}\nFinding your perfect movies, {name}", end="", flush=True)
    processing_animation()

    # Helper function to get/display recommendations
    def get_and_show_recs():
        recs = recommend_movies(
            genre=genre, mood=mood, rating=rating,
            actor=actor, decade=decade, duration=duration,
            award_winning=award_winning, top_n=5
        )
        if isinstance(recs, str):
            print(Fore.RED + recs + "\n")
        else:
            display_recommendations(recs, name)
        return recs

    # Show initial recommendations
    get_and_show_recs()

    # Ask for more recommendations
    while True:
        action = input(Fore.YELLOW + "\nWould you like more recommendations? (yes/no): ").strip().lower()
        if action == 'no':
            print(Fore.GREEN + f"\nEnjoy your movie picks, {name}! Don't forget your popcorn! 🎬🍿\n")
            break
        elif action == 'yes':
            get_and_show_recs()
        else:
            print(Fore.RED + "Invalid choice. Try again.\n")

# Main program
def main():
    print(Fore.BLUE + "🎥 Welcome to your Ultra-Personalized Movie Recommendation Assistant! 🎥\n")
    name = input(Fore.YELLOW + "What's your name? ").strip()
    print(f"\n{Fore.GREEN}Great to meet you, {name}! Let's tailor some movie recommendations just for you.\n")
    handle_ai(name)

if __name__ == "__main__":
    main()