
import pandas as pd
import spotify
import sys
import os
import spotipy 
from spotipy.oauth2 import SpotifyOAuth
import tkinter as tk
from tkinter import Tk, Label, Button, Checkbutton, messagebox, IntVar 
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from PIL import Image, ImageTk, ImageSequence
from tkinter.messagebox import showinfo, showwarning, showerror
from tkcalendar import Calendar

spotify_df = pd.read_csv('C:/Users/USER/Desktop/info/genres_v2.csv')
spotify_df['song_id'] = range(1, len(spotify_df) + 1)

spotify_df = spotify_df.dropna()
spotify_df.info()




# Variables globales pour les sélections utilisateur
selected_genres = []
selected_music = []
music_choisi = None
frames=[]

def clear_window():
    for widget in fenetre.winfo_children():
        widget.destroy() 

def go_to_main():
    clear_window()
    fenetre.title("Connexion")
    img_tune(r'C:\Users\USER\Documents\Python Scripts\tune.png')
    tk.Label(text="", width="300", height="7", font=("Calibri", 13)).pack()
    tk.Label(text="").pack()
    tk.Label(text="Bienvenue sur notre plateforme ! Veuillez choisir une option pour continuer", width="300", height="1", font=("Sans-serif", 14)).pack()
    tk.Label(text="").pack()
    tk.Label(text="", width="300", height="4", font=("Calibri", 13)).pack()
    tk.Label(text="").pack()
    tk.Button(text="Connexion à votre compte", height="2", bg="pink", width="30", command=login).pack()
    tk.Label(text="").pack()
    tk.Button(text="Créer un nouveau compte", bg='pink', height="2", width="30", command=register).pack() 
    
def register():
    clear_window()
    fenetre.title("Inscription - Créez votre compte")
    img_tune(r'C:\Users\USER\Documents\Python Scripts\tune.png')
    global first_name
    global second_name
    global username
    global password
    global confirm_password  
    global first_name_entry
    global second_name_entry
    global username_entry
    global password_entry
    global confirm_password_entry   
    global dob
    first_name = tk.StringVar()
    second_name = tk.StringVar()
    username = tk.StringVar()
    password = tk.StringVar()
    confirm_password = tk.StringVar()
    dob = tk.StringVar()
    tk.Label(fenetre, text="Merci de renseigner les informations suivantes pour vous inscrire.", font=("Sans-serif", 14)).pack()
    # tk.Label(fenetre, text="").pack()
    first_name_label = tk.Label(fenetre, text="Prénom * ")
    first_name_label.pack()
    first_name_entry = tk.Entry(fenetre, textvariable=first_name)
    first_name_entry.pack()
    second_name_label = tk.Label(fenetre, text="Nom * ")
    second_name_label.pack()
    second_name_entry = tk.Entry(fenetre, textvariable=second_name)
    second_name_entry.pack() 
    username_label = tk.Label(fenetre, text="Nom d'utilisateur * ")
    username_label.pack()
    username_entry = tk.Entry(fenetre, textvariable=username)
    username_entry.pack()  
    password_label = tk.Label(fenetre, text="Mot de passe * ")
    password_label.pack()
    password_entry = tk.Entry(fenetre, textvariable=password, show='*')
    password_entry.pack()
    confirm_password_label = tk.Label(fenetre, text="Confirmer le mot de passe * ")
    confirm_password_label.pack()
    confirm_password_entry = tk.Entry(fenetre, textvariable=confirm_password, show='*')
    confirm_password_entry.pack()
    tk.Label(fenetre, text="Date de naissance * ").pack()
    cal = Calendar(fenetre, selectmode='day', year=2000, month=1, day=1, date_pattern='dd/mm/yyyy')
    cal.pack(pady=10)
    def select_date():
        dob.set(cal.get_date())
    tk.Button(fenetre, text="Sélectionner une date", bg='pink', command=select_date).pack()
    tk.Label(fenetre, text="").pack()
    tk.Button(fenetre, text="Valider l'inscription", width=20, height=1, bg="pink", command=register_user).pack()
    tk.Button(fenetre, text="Retour à l'accueil", width=20, height=1, bg="pink", command=go_to_main).pack()

def login():
    clear_window()
    fenetre.title("Connexion à votre compte")
    img_tune(r'C:\Users\USER\Documents\Python Scripts\tune.png')
    tk.Label(fenetre, text="", width="300", height="7", font=("Calibri", 13)).pack()
    tk.Label(fenetre, text="").pack()
    tk.Label(fenetre, text="Veuillez entrer vos identifiants pour vous connecter", font=("Sans-serif", 14)).pack()
    tk.Label(fenetre, text="").pack() 
    global username_verify
    global password_verify
    username_verify = tk.StringVar()
    password_verify = tk.StringVar()
    global username_login_entry
    global password_login_entry
    tk.Label(fenetre, text="Nom d'utilisateur * ").pack()
    username_login_entry = tk.Entry(fenetre, textvariable=username_verify)
    username_login_entry.pack()
    tk.Label(fenetre, text="").pack()
    tk.Label(fenetre, text="Mot de passe * ").pack()
    password_login_entry = tk.Entry(fenetre, textvariable=password_verify, show='*')
    password_login_entry.pack()
    tk.Label(fenetre, text="").pack()
    tk.Button(fenetre, text="Se connecter", bg='pink', width=20, height=1, command=login_verify).pack()
    tk.Button(fenetre, text="Retour à l'accueil", width=20, height=1, bg="pink", command=go_to_main).pack()
     
def register_user():
    clear_window()
    img_tune(r'C:\Users\USER\Documents\Python Scripts\tune.png')
    username_info = username.get()
    password_info = password.get()
    confirm_password_info = confirm_password.get()
    second_name_info = second_name.get()
    first_name_info = first_name.get()
    dob_info = dob.get()
    
    if not username_info or not password_info or not confirm_password_info or not second_name_info or not first_name_info or not dob_info:
        messagebox.showerror("Erreur", "Tous les champs doivent être remplis")
        return
    
    if password_info != confirm_password_info:
        messagebox.showerror("Erreur", "Les mots de passe ne correspondent pas")
        return

    # Vérifier si le fichier existe déjà
    if os.path.exists(username_info):
        messagebox.showerror("Erreur", "Un compte avec ce nom d'utilisateur existe déjà")
        return

    # Écrire les informations dans le fichier
    with open(username_info, "w") as file:
        file.write(f"{first_name_info}\n")
        file.write(f"{second_name_info}\n")
        file.write(f"{username_info}\n")
        file.write(f"{password_info}\n")
        file.write(f"{dob_info}\n")
    messagebox.showinfo("Succès", "Inscription réussie ! Vous pouvez maintenant vous connecter")
    genre_selection()
    

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, tk.END)
    password_login_entry.delete(0, tk.END)
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            genre_selection()
        else:
            password_not_recognised()
    else:
        user_not_found()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = tk.Toplevel(fenetre)
    password_not_recog_screen.title("Erreur")
    password_not_recog_screen.geometry("250x100")
    tk.Label(password_not_recog_screen, text="Le mot de passe que vous avez saisi est incorrect").pack()
    tk.Button(password_not_recog_screen, text="OK", bg='pink', command=delete_password_not_recognised).pack()

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = tk.Toplevel(fenetre)
    user_not_found_screen.title("Erreur")
    user_not_found_screen.geometry("250x100")
    tk.Label(user_not_found_screen, text="Aucun utilisateur trouvé avec ce nom d'utilisateur").pack()
    tk.Button(user_not_found_screen, text="OK", bg='pink', command=delete_user_not_found_screen).pack()


# Fonction appelée lors de la sélection ou désélection d'une case à cocher
def on_checkbox_change(value, target_list):
    if value in target_list:
        target_list.remove(value)
    else:
        target_list.append(value)

# Fonction appelée lors de la validation des genres
def validate_genre_selection():
    if len(selected_genres) != 5:
        messagebox.showerror("Erreur", "Veuillez sélectionner exactement 5 genres.")
    else:
        messagebox.showinfo("Succès", f"Les genres sélectionnés sont validés : {selected_genres}")
        display_music_selection()

# Fonction appelée lors de la validation de la musique
def validate_music_selection():
    global music_choisi
    if len(selected_music) != 1:
        messagebox.showerror("Erreur", "Veuillez sélectionner uniquement une seule musique.")
    else:
        music_choisi = selected_music[0]
        messagebox.showinfo("Succès", f"La musique sélectionnée est : {music_choisi}")
        start_song(music_choisi)

# Fonction pour démarrer la lecture de la musique sélectionnée
def start_song(song_name):
    track_row = spotify_df[spotify_df['song_name'] == song_name]
    if track_row.empty:
        messagebox.showerror("Erreur", "La musique sélectionnée n'a pas été trouvée.")
        return

    track_uri = track_row.iloc[0]['uri']
    try:
        devices = sp.devices()
        if not devices['devices']:
            print("Aucun périphérique disponible pour la lecture")
            return

        device_id = devices['devices'][0]['id']
        sp.transfer_playback(device_id=device_id, force_play=True)
        sp.start_playback(device_id=device_id, uris=[track_uri])
        print("Lecture de la chanson démarrée")
        
        # Après le début de la chanson, afficher les recommandations
        start_songs()

    except spotipy.exceptions.SpotifyException as e:
        print(f"Erreur lors de la tentative de lecture de la chanson: {e}")

# Configuration des identifiants Spotify
client_id = os.getenv('SPOTIPY_CLIENT_ID', '5d7cc708ac0240e3bd9acd627f4c053c')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET', '3d8cb1df8b514a138259cbd126e80762')
redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI', 'http://localhost:8080/callback')

# Configuration de l'authentification Spotify
auth_manager = SpotifyOAuth(client_id=client_id,
                            client_secret=client_secret,
                            redirect_uri=redirect_uri,
                            scope='user-modify-playback-state user-read-playback-state')
sp = spotipy.Spotify(auth_manager=auth_manager)

def genre_selection() :
    clear_window()
    img_tune(r'C:\Users\USER\Documents\Python Scripts\tune.png')
    fenetre.title("Sélection de genres")
    label = Label(fenetre, text="Veuillez sélectionner 5 genres à partir de ces propositions:")
    label.pack()
    genre_value = spotify_df['genre'].unique()
    for value in genre_value:
        bouton = Checkbutton(fenetre, text=str(value), command=lambda v=value: on_checkbox_change(v, selected_genres))
        bouton.pack()
    bouton_validation = Button(fenetre, text="Valider", command=validate_genre_selection, bg='pink')
    bouton_validation.pack()

# Fonction pour afficher la sélection de musique
def display_music_selection():
    clear_window()
    fenetre.title("Sélection de musique")
    img_tune(r'C:\Users\USER\Documents\Python Scripts\tune.png')
    recommandations_globales = recommander_musiques(selected_genres)
    for genre, recommandations in recommandations_globales.items():
        Label(fenetre, text=f"Musiques pour le genre {genre}:",font=("Sans-serif", 14),fg="#C71585").pack()
        for recommandation in recommandations:
            bouton = Checkbutton(fenetre, text=recommandation, command=lambda v=recommandation: on_checkbox_change(v, selected_music))
            bouton.pack()

    bouton_validation2 = Button(fenetre, text="Valider", command=validate_music_selection, bg='pink')
    bouton_validation2.pack(side='right', padx=5, pady=5)

# Fonction pour démarrer les recommandations de musiques
def start_songs():
    global label_gif
    clear_window()
    fenetre.title("Recommandations de musiques")
    img_tune(r'C:\Users\USER\Documents\Python Scripts\tune.png')
    gif_path = r'C:\Users\USER\Desktop\info\tenor (1).gif'
    gif(gif_path)

    # Initialiser label_gif
    label_gif = Label(fenetre)
    label_gif.pack(side='right')
    fenetre.after(0, update_frame, 0) 
    recommandations_songs = recommand_songs(music_choisi, spotify_df)
    
    frame_gauche = tk.Frame(fenetre)
    frame_gauche.pack(side="left", fill="y", padx=10, pady=10)

    label = tk.Label(frame_gauche, text=f"Écoutez '{music_choisi}'. Recommandations :",font=("Sans-serif", 14),fg="#C71585")
    label.pack(anchor='w', pady=5)

    for song in recommandations_songs['song_name']:
        bouton = tk.Checkbutton(frame_gauche, text=song, command=lambda v=song: on_checkbox_change(v, selected_music))
        bouton.pack(anchor='w', padx=5, pady=2)
    
        selected_music.clear()
    bouton_validation2 = Button(fenetre, text="Valider", command=validate_music_selection, bg='pink')
    bouton_validation2.pack(side='right', padx=5, pady=5)

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def main_account_screen():
    global fenetre
    fenetre= tk.Tk()
    go_to_main()  # Initialise la fenêtre principale avec les choix
    fenetre.mainloop() 
    

# Fonction pour recommander des musiques en fonction des genres sélectionnés
def recommander_musiques(genres_prefere, nb_recommandations_par_genre=3):
    recommandations_globales = {}
    for genre in genres_prefere:
        filtre = spotify_df['genre'] == genre
        musiques_filtrees = spotify_df[filtre]
        recommandations = musiques_filtrees['song_name'].head(nb_recommandations_par_genre).tolist()
        recommandations_globales[genre] = recommandations
    return recommandations_globales

# Fonction pour recommander des musiques similaires
def recommand_songs(song_name, data, num_recommendations=15):
    scaler = StandardScaler()
    X = scaler.fit_transform(data[['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms']])
    kmeans = KMeans(n_clusters=5, random_state=40)
    kmeans.fit(X)
    data['cluster'] = kmeans.labels_
    if song_name not in data['song_name'].values:
        print("Song not found.")
        return pd.DataFrame()
    cluster_of_liked_song = data.loc[data['song_name'] == song_name, 'cluster'].iloc[0]
    recommendations = data[data['cluster'] == cluster_of_liked_song]
    recommendations = recommendations[recommendations['song_name'] != song_name]
    recommendations = recommendations.sample(frac=1).reset_index(drop=True)
    return recommendations[['song_name']].head(num_recommendations)
def img_tune(image_path):
    image = Image.open(image_path)
    resize_image = image.resize((150, 150))
    img = ImageTk.PhotoImage(resize_image)
    label_img = Label(fenetre, image=img)
    label_img.image = img
    label_img.pack() 
def update_frame(ind):
    global frames, label_gif
    frame = frames[ind]
    ind += 1
    if ind == len(frames):
        ind = 0
    label_gif.config(image=frame)
    fenetre.after(100, update_frame, ind)    
def gif(gif_path):
    global frames, label_gif
    gif_image = Image.open(gif_path)
    frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(gif_image)]    

main_account_screen()
