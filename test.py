from instagrapi import Client

cl = Client()
cl.login("alexei.pozdnyakov", "#Lexa1367452")

user_id = cl.user_id_from_username("nt_crckr")
medias = cl.user_medias(user_id, 20)
