from ensta import Web


class Insta:
    def __init__(self):
        self.web = Web("balzz1910", "Iqbaal100%")
        
    def profile(self, username: str):
        """
        Get profile

        Args:
            username (str): Instagram username to get profile

        Returns:
            dict: profile data
        """
        profile = self.web.profile(username)
        return profile
    
    def followings(self, username: str):
        """
        Get followings

        Args:
            username (str): Instagram username to get followings

        Returns:
            generator: followings data
        """
        followings = self.web.followings(username)
        return followings
    
    def followers(self, username: str):
        """
        Get followers

        Args:
            username (str): Instagram username to get followers

        Returns:
            generator: followers data
        """
        followers = self.web.followers(username)
        return followers