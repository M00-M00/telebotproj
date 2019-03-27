from datetime import datetime, date, time

t_now = datetime.now()

# Add a token for the bot & chatId  for channel/group/contact to be messaged

bot_token= ''
bot_chatId =''





# Add posts to the file


PostA = 'Test post number 1'

PostB = 'Test post number 2'

PostC = 'Test post 3 '

PostD = 'Another post'




#Assign posts and time (in format (Months, Day, Hours, Minutes))


Post1 = PostB
Time1 = (3, 28, 23, 1)

Post2 = PostA
Time2 = (3, 28, 22, 55)

Post3 = PostC
Time3 = (3, 29, 22, 59)

#... extend if needed


#
#CREATE SCHEDULE IN FORMAT [[Time1, Post1], [Time2, Post2]]
#Below are examples how Schedule would look if 1, 2 or 3 posts are schedule. For example if onlybone post is to be scheduled, then make schedule with only one post active by moving the hashtag

#Schedule = [Time1, Post1]


#Schedule = [[Time1, Post1], [(Time2), Post2]]

Schedule = [[Time1, Post1], [Time2, Post2],[Time3, Post3]]
