from app import schemas

def test_get_posts(authorized_client, test_posts, user):
    response = authorized_client.get(f'/posts/')
    
    def validate(post):
        return schemas.PostVoteResponse(**post)
    
    post_map = map(validate, response.json() )
    post_list = list(post_map)
    
    # print(post_list)
    
    assert test_posts[0].title in [post.Post.title for post in post_list]
    assert len(test_posts) == len(response.json())
    assert response.status_code == 200
    
def test_unauthorized_get_posts(client, test_posts):
    response = client.get(f"/posts/{test_posts[0].id}")
    assert response.status_code == 401
    
# cover every individual scenarios for testing to test the application

     