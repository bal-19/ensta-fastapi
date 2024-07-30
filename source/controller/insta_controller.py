from ..helper import mapping
from ..service.insta import Insta


class InstaController:
    def __init__(self) -> None:
        self.insta = Insta()
    
    def profile(self, username: str):
        profile = self.insta.profile(username)
        data = mapping.profile(profile)
        return data
    
    def followers(self, username: str):
        followers = self.insta.followers(username)
        raw = []
        for user in followers:
            data = mapping.followers(user)
            raw.append(data)

        return raw
    
    def followings(self, username: str):
        followings = self.insta.followings(username)
        raw = []
        for user in followings:
            data = mapping.followings(user)
            raw.append(data)
            
        return raw