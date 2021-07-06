import flask
from flask import request, jsonify,make_response,render_template_string
import requests 
from persistence import cache

app = flask.Flask(__name__)
app.config["DEBUG"] = True

SORTING_INDICES=['id','reads','likes','popularity']
DIRECTION_OPTIONS=['desc','asc']

@app.route('/', methods=['GET'])
def home():
    f = open("./html/index.html",'r',encoding = 'utf-8')
    return render_template_string(f.read())

@app.route('/api/ping', methods=['GET'])
def ping():
    return make_response(jsonify({'success':True}),200)

@app.route('/api/posts', methods=['GET'])
def get_posts():
    #getting parameters
    tags=request.args.get('tags')
    sort_by=request.args.get('sortBy')
    direction=request.args.get('direction')
    
    #handeling empty tags list
    if(tags==None):
        return make_response(jsonify({'error':'Tags parameter is required'}),400)
    
    #handeling invalid sortBy parameter
    if(sort_by!=None):
        if(sort_by not in SORTING_INDICES):
            return make_response(jsonify({'error':'sortBy parameter is invalid'}),400)
    
    #handeling invalid direction parameter
    if(direction!=None):
        if(direction not in DIRECTION_OPTIONS):
            return make_response(jsonify({'error':'direction parameter is invalid'}),400)
    
    #converting tags from srting to list
    tags=str(tags).split(',')
    all_posts=[]
    retrived=[] #ids of already retrieved posts
    cache_obj = cache()
    visited_tags=cache_obj.get_visited_tags() #tags that have already been visited in past

    
    for tag in tags:
        if(tag not in visited_tags):
            cache_obj.save_visited_tag(tag)
            URL="https://api.hatchways.io/assessment/blog/posts"
            PARAMS={"tag":tag}
            r = requests.get(url = URL, params = PARAMS) 
            current_posts=r.json()['posts']
            cache_obj.add_to_visited_posts(current_posts)
            for post in current_posts:
                if(post['id'] not in retrived):
                    all_posts.append(post)
                    retrived.append(post['id'])
        else:
            for post in cache_obj.get_visted_posts_by_tag(tag):
                if(post['id'] not in retrived):
                    all_posts.append(post)
                    retrived.append(post['id'])
    
    if(direction=='asc'):
        asc_post=sorted(all_posts, key = lambda i: i[sort_by])
        return make_response(jsonify(asc_post),200)
    elif(direction=='desc'):
        desc_post=sorted(all_posts, key = lambda i: i[sort_by],reverse=True)
        return make_response(jsonify(desc_post),200)
    return make_response(jsonify(all_posts),200)


app.run()