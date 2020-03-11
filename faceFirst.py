import os
import json
import facebook

def main():
    token = os.getenv('facebook_access_token')
    graph = facebook.GraphAPI(token)

    fields = ['birthday, email, friends, posts']
    profile = graph.get_object('me', fields=fields)

    print(json.dumps(profile, indent=4))

if __name__ == '__main__':
    main()