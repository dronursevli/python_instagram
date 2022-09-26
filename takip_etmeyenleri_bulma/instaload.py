!pip install instaloader

#%%
import instaloader

L = instaloader.Instaloader()

username = "hesapadi"
password = "sifre"
L.login(username, password)  # (login)

profile = instaloader.Profile.from_username(L.context, username)

#%%
#takipçileri al    
    
for followers in profile.get_followers():
    with open("takipci.txt","a+") as f:
        file = f.write(followers.username+'\n')
        
    print("Takipçiler yazılıyor...")
    print(file)
    
#%%  
#takip edilenleri al

for followees in profile.get_followees():
    with open("takipedilen.txt","a+") as f:
        file = f.write(followees.username+'\n')
         
    print("Takip edilenler yazılıyor...")
    print(file)
    
#%%
#takip etmeyenleri bul. takip edilenelerde olup takipçilerde olmayanlar takip etmeyenler

followers_file = set(open("takipci.txt").readlines())
followees_file = set(open("takipedilen.txt").readlines())

unfollowers_set = followees_file.difference(followers_file)
        
for unfollowers in unfollowers_set:
    print(unfollowers)