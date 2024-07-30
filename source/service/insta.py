from ensta import Web


class Insta:
    def __init__(self):
        self.web = Web("balzz1910", "Iqbaal100%")
        
    def profile(self, username: str):
        profile = self.web.profile(username)
        return profile
    
    def followings(self, username: str):
        followings = self.web.followings(username)
        return followings
    
    def followers(self, username: str):
        followers = self.web.followers(username)
        return followers