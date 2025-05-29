import requests

def lookup_instagram(username):
    url = f"https://www.instagram.com/{username}/?__a=1&__d=dis"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            profile = data['graphql']['user']
            return {
                "Full Name": profile.get("full_name"),
                "Username": profile.get("username"),
                "Followers": profile.get("edge_followed_by", {}).get("count"),
                "Following": profile.get("edge_follow", {}).get("count"),
                "Bio": profile.get("biography"),
                "External URL": profile.get("external_url")
            }
        else:
            return {"error": f"User not found or private ({response.status_code})"}
    except Exception as e:
        return {"error": str(e)}
