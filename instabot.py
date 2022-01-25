### This script follows 65 users per hour 


from instapy import InstaPy
from instapy import smart_run
import time

insta_username = 'stop.waiting.for.friday'
insta_password = ''

for x in range(10000):
    print("this is " + str(x) + " time")
    print('starting again')

    session: InstaPy = InstaPy(username=insta_username,
                      password=insta_password,
                      headless_browser=False)





    with smart_run(session):


        session.set_relationship_bounds(enabled=True,
                                        delimit_by_numbers=True,
                                        max_followers=100000,
                                        min_followers=0,
                                        min_following=0,)



        session.set_quota_supervisor(enabled=True,
                                     sleepyhead=True, stochastic_flow=True,

                                     notify_me=True,
                                     peak_follows_hourly=65, #hourly follow limit
                                     peak_follows_daily=400) #daily follow limit
                                     #peak_unfollows_hourly=25,
                                     #peak_unfollows_daily=300)



        session.follow_user_followers(['in.a.relationship.with.freedom', 'victoriassecret'], amount=5000, #'insta_username', amount of user followers

                                    randomize=False, interact=False)





        #session.unfollow_users(amount=200, allFollowing=True, style="LIFO", unfollow_after=48 * 60 * 60)
        session.end()

        print('sleep mode!')
        time.sleep(900)
        print('sleep mode over')



