import requests, json



r_p = requests.get('https://jsonplaceholder.typicode.com/posts')
r_u = requests.get('https://jsonplaceholder.typicode.com/users')
r_posts = r_p.json()
r_users = r_u.json()


def user(id):
    return list(filter(lambda a: a['id'] == id, r_users))[0]

for post in r_posts:
    post['user'] = user(post['userId'])
    print(json.dumps(post, indent=1))
