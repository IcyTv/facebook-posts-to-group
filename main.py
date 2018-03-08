#!/usr/bin/env python

#Add your access token with the scope: publish_actions, user_posts, user_managed_groups.
#You can set the scopes at https://developers.facebook.com/tools/explorer
access_token = ""
#Add your groups id. You can find it by going to your group and copy pasting the number between the slashes
#https://www.facebook.com/groups/{THIS NUMBER}/
group_id = ""



import facebook
import time


last_post_id = 0

if __name__ == "__main__":
	graph = facebook.GraphAPI(access_token=access_token, timeout=None, version=None, proxies=None)
	name = graph.get_object("me")["name"]
	while True:
		data = graph.get_object("me/posts")
		if(data["data"][0]["id"] != last_post_id):
			print "NEW POST AVAILABLE"
			print data["data"][0]["story"]
			last_post_id = data["data"][0]["id"]
			graph.put_object(group_id, connection_name="feed", message="A new post from " + name + "\n" + data["data"][0]["story"])
		time.sleep(5*60)
		print "Sleeping"
