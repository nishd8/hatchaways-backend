import json

class cache:
    def __init__(self):
        print('Cache Activated')

    def get_visited_tags(self):
        f = open('api/visited_tags.txt','r')
        tags=f.read().split(',')
        f.close()
        return(tags) 
    
    def save_visited_tag(self,tag):
        if tag not in self.get_visited_tags():
            f = open('api/visited_tags.txt','a')
            f.write(tag+",")
            f.close()
            print('tag added')
        else:
            print('tag already exists')
    
    def get_visted_posts(self):
        visited_posts=[]
        try:
            f=open('api/cache.json','r')
            visited_posts=json.load(f)
            f.close()
        except:
            visited_posts=[]
        return visited_posts
    
    def get_visted_posts_by_id(self,id):
        posts=self.get_visted_posts()
        if(len(posts)>0):
            for post in posts:
                if post['id']==id:
                    return post
                else:
                    return None
        else:
            return None
            
    def get_visted_posts_by_tag(self,tag):
        posts=self.get_visted_posts()
        post_by_tags=[]
        if(len(posts)>0):
            for post in posts:
                if tag in post['tags']:
                    post_by_tags.append(post)
            return post_by_tags
        else:
            return None
    
    def add_to_visited_posts(self,posts):
        cached_posts = self.get_visted_posts()
        for post in posts:
            if(self.get_visted_posts_by_id(post['id']) == None):
                cached_posts.append(post)
                print('Post Added')
            else:
                print('Post Already Exists')
        f=open('api/cache.json','w')
        f.write(json.dumps(cached_posts))
        f.close()