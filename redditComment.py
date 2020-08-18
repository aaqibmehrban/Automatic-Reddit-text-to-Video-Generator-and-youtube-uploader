import praw
file=open('credentials.txt','r')
file=file.readlines()
c_id=file[0].split(':')[1].strip()
s_id=file[1].split(':')[1].strip()
name =file[2].split(':')[1].strip()


def redditComment(subreddit_name,total_iterations,N):
    reddit = praw.Reddit(client_id=c_id,
            client_secret=s_id,
            user_agent=name)
    hot_subreddit = reddit.subreddit(subreddit_name).hot(limit=N)
    
    authors=[]
    comments=[]
    try:
        for post in hot_subreddit:
            post = post
        for i in range(total_iterations):
            if len(post.comments[i].body)<1000:
                authors.append(post.comments[i].author)
                comments.append(post.comments[i].body)
        total_iterations = len(authors)
        return (post,authors,comments, total_iterations)
    except:
        print('''
        Try any other combination this happen when posts or comments not found 
        Tip : Try to keep comments ammount bigger then posts Amount 
        
        
        ''')
    
    