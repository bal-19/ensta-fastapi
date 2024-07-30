from ..library.datetime import Datetime


def profile(data: dict):
    """
    Mapping profile data

    Args:
        data (dict): data from Insta.profile()

    Returns:
        dict: mapped data
    """
    return {
        "fullname": data.full_name,
        "profile_picture_url": data.profile_picture_url_hd,
        "follower_count": data.follower_count,
        "following_count": data.following_count,
        "biography": data.biography,
        "biography_links": data.biography_links,
        "pronouns": data.pronouns,
        "category_name": data.category_name,
        "highlight_count": data.highlight_count,
        "total_post_count": data.total_post_count,
        "is_business_account": data.is_business_account,
        "is_professional_account": data.is_professional_account,
        "is_private": data.is_private,
        "is_verified": data.is_verified,
        "datetime": Datetime.formatted_date(),
        "timestamp": Datetime.timestamp()
    }

def followers(data: dict):
    """
    Mapping followers data

    Args:
        data (dict): data from Insta.followers()

    Returns:
        dict: mapped data
    """
    return {
        "username": data.username,
        "fullname": data.full_name,
        "has_anonymous_profile_picture": data.has_anonymous_profile_picture,
        "profile_picture_url": data.profile_picture_url,
        "is_private": data.is_private,
        "is_verified": data.is_verified,
        "datetime": Datetime.formatted_date(),
        "timestamp": Datetime.timestamp()
    }

def followings(data: dict):
    """
    Mapping followings data

    Args:
        data (dict): data from Insta.followings()

    Returns:
        dict: mapped data
    """
    return {
        "username": data.username,
        "fullname": data.full_name,
        "has_anonymous_profile_picture": data.has_anonymous_profile_picture,
        "profile_picture_url": data.profile_picture_url,
        "is_private": data.is_private,
        "is_verified": data.is_verified,
        "datetime": Datetime.formatted_date(),
        "timestamp": Datetime.timestamp()
    }