import os
import json
import facebook

def main():
    token = os.getenv('face_page_token')
    graph = facebook.GraphAPI(token)

    fields = ['id, name, posts']
    profile = graph.get_object('me', fields=fields)

    print(json.dumps(profile, indent=4))

if __name__ == '__main__':
    main()