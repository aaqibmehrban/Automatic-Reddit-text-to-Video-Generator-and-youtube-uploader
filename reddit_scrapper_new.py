import praw
from divideComment import *


def new_scrapr(links, N):
    jp = int(1)
    file = open('credentials.txt', 'r')
    file = file.readlines()
    c_id = file[0].split(':')[1].strip()
    s_id = file[1].split(':')[1].strip()
    name = file[2].split(':')[1].strip()

    reddit = praw.Reddit(client_id=c_id,
                         client_secret=s_id,
                         user_agent=name)
    # filee=open('script_generated.txt','w+')
    y_locations = []
    comments = []
    authors = []
    post_titles = []
    post_authors = []
    post_y_locations = []
    post_bodies=[]
    post_bod_y_locations=[]
    replies = []
    replies_author = []
    replies_y_locations = []
    if jp == 1:
        title_for_thumbnail = ''
    N = int(N)  # number of comments
    for url in links:
        y_l = []
        commn = []
        auths = []
        cmforwrite = []
        arthurforwrite = []

        submission = reddit.submission(url=url)
        post_text = submission.selftext
        post_authors.append(submission.author.name)
        # filee.write(submission.author.name)
        # print(submission.title)
        if jp == 1:
            title_for_thumbnail = submission.title

        submission.comments.replace_more()
        i = int(1)
        submission.comment_sort = 'best'
        br=int(1)
        for top_level_comment in submission.comments:
            if len(top_level_comment.body) <= 1000:

                chkkk=top_level_comment.author
                # chkkk=chkkk.lower()
                # print(chkkk)
                # chkkk=chkk.name
                if top_level_comment.author != None:
                    if 'bot' not in str(chkkk).lower() and 'auto' not in str(chkkk).lower():
                        try:
                            bc = top_level_comment.replies[0]
                            # print(bc.body)

                            (replies_part, replies_y_location) = divideComment(bc.body)
                            replies.append(replies_part)
                            replies_author.append(bc.author.name)
                            replies_y_locations.append(replies_y_location)
                        except:
                            continue



                        cmnttext = top_level_comment.body
                        cmforwrite.append(cmnttext)

                        at = top_level_comment.author
                        print(at.name)
                        arthurforwrite.append(at.name)
                        # word = cmnttext.replace('\n', '')
                        word=cmnttext.strip()
                        (comments_parts, y_location) = divideComment(word)
                        commn.append(comments_parts)
                        y_l.append(y_location)
                        aut = top_level_comment.author
                        auths.append(aut.name)
                        if br==N:
                            break
                        br+=1
            # else:
            # break
        (post_titls, post_y_location) = divideComment(submission.title)
        post_titles.append(post_titls)
        post_y_locations.append(post_y_location)
        post_text=post_text.replace('\n','')
        (post_bod,post_bod_y_location)=divideComment(post_text)
        post_bodies.append(post_bod)
        post_bod_y_locations.append(post_bod_y_location)
        # for i in arthurforwrite[:N]:
        #     filee.write(i)

        for i in commn[:N]:
            comments.append(i)
        # for i in cmforwrite[:N]:
        #     filee.write(i)

        for i in y_l[:N]:
            y_locations.append(i)
        for i in auths[:N]:
            authors.append(i)


    # print(post_titles)
    # for x in range(len(post_authors)):
    #     filee.write(post_authors[x])
    #     for y in range(len(post_titles[x])):
    #         filee.write(post_titles[y])
    # for y in range(len(comments)):
    #     filee.write(authors[y])
    #     for x in range(len(comments[x])):
    #         filee.write(comments[y])
    jp += 1

    return post_titles,post_authors,comments,authors,y_locations,post_y_locations,title_for_thumbnail,post_bodies,post_bod_y_locations,replies_author,replies,replies_y_locations
    # print(post_titles)
    # print(post_authors)
    # print(post_bodies)
    # print(post_bod_y_locations)
    # print(comments)
    # print(authors)
    # print(y_locations)
    # print(post_y_locations)
    # print(title_for_thumbnail)
    # print(replies_author)
    # print(replies_y_locations)
    # print(replies)

# url = ['https://www.reddit.com/r/AMA/comments/gwbw52/my_parents_said_online_that_george_deserved_it/']
# new_scrapr(url, 4)
