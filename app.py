from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# 🔗 Replace this with your actual API URL later
API_URL = "https://asrcoddeploy-anime-recomm-api.hf.space/recommend"


def recommend_from_api(anime_name):
    try:
        response = requests.get(API_URL, params={"anime": anime_name})
        
        if response.status_code == 200:
            data = response.json()
            return data.get("recommendations", ["No results found"])
        
        return ["Error: API not responding"]
    
    except:
        return ["Error connecting to API"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def get_recommendations():
    anime_name = request.form.get("anime")

    # ✅ Validation (same as before)
    if not anime_name or len(anime_name.strip()) < 2:
        return render_template(
            "result.html",
            anime_name=anime_name,
            results=["❌ Please enter a valid anime name"]
        )

    results = recommend_from_api(anime_name)

    return render_template(
        "result.html",
        anime_name=anime_name,
        results=results
    )


if __name__ == "__main__":
    app.run(debug=True)
