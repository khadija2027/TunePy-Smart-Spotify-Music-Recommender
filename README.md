# 🎵 TunePy – Smart Spotify Music Recommender 🎶

**TunePy** is a personalized desktop app built with Python that allows users to discover music tailored to their taste using machine learning and Spotify integration.

---

## 🚀 Key Features

- 🔐 **User Authentication** – Register & log in securely  
- 🎧 **Genre-Based Filtering** – Select exactly **5 favorite genres**  
- 🎵 **Personalized Recommendations** – Suggested tracks based on your preferences  
- 🤖 **KMeans Clustering** – Intelligent song grouping based on audio features  
- 🎼 **Spotify Playback** – Instantly play songs via Spotify API  
- 🖼️ **Interactive GUI** – Built with **Tkinter**, featuring visuals & animations  

---

## 🧠 Tech Stack

| Category         | Tools / Libraries                               |
|------------------|-------------------------------------------------|
| **UI/UX**        | Tkinter, Pillow, tkcalendar                     |
| **ML & Analysis**| pandas, scikit-learn                            |
| **Spotify API**  | spotipy                                         |
| **Environment**  | os, dotenv, sys                                 |
| **Data**         | `genres_v2.csv` from Spotify                    |

---

## 📊 Dataset

TunePy uses the **Spotify `genres_v2.csv` dataset**, which contains key audio features such as:

- 🎵 danceability  
- ⚡ energy  
- 🎼 acousticness  
- 🎚️ tempo  
- 😊 valence  
- ...and more

These features are processed and clustered using the **KMeans algorithm** to find and suggest songs similar to the user's selections.

---

## 🎯 How It Works

1. 🔑 **Login/Register**
2. 🎶 **Select 5 Genres**
3. 💖 **Pick a Favorite Song**
4. 📈 **KMeans Clustering on Dataset**
5. 🤝 **Get Similar Song Recommendations**
6. ▶️ **Play Tracks via Spotify**

---

## 📍 Clustering Visualization

A sample KMeans clustering visualization of audio features:

![KMeans Clusters](kmeans_clusters.png) <!-- Replace with your actual image path -->

---
