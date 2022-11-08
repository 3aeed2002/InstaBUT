#instagram bot created by Saeed Abbaszadeh
#Social Media :
#   Instagram pages :
#       saeed_abszd_81  ,,,,,  instarobot.py


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random


class InstaBot:
    def __init__(self , username , password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        
    def closebrowser(self):
        'close the browser'

        self.driver.close()

    #Login Method
    def login(self):
        'Login to your account'


        driver = self.driver  

        #Open instagram login page
        driver.get('https://www.instagram.com/')

        time.sleep(random.randint(5 , 8))

        #Find username box and inject username
        driver.find_element(By.XPATH , '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username)

        time.sleep(random.randint(2 , 4))

        #Find password box and inject password
        driver.find_element(By.XPATH , '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)

        time.sleep(random.randint(2 , 4))

        #Click on login button 
        driver.find_element(By.XPATH , '//*[@id="loginForm"]/div/div[3]').click()

        time.sleep(random.randint(9 , 12))

        #Open profile 
        driver.get(f'https://instagram.com/{self.username}')

        time.sleep(random.randint(8 , 13))

        #Like Method
    def like(self , hashtag):
        'Like photos from hashtag'

        driver = self.driver

        driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/')

        time.sleep(random.randint(9 , 14))

        piclin = []
        uniphoto = []

        print('Scrolling ... ')
        for i in range(1 , 8):  #How many you wanna scroll the page
                try:
                    time.sleep(random.randint(10 , 15))
                    driver.execute_script("window.scrollTo(0 , document.body.scrollHeight)")
                    time.sleep(random.randint(10 , 15))

                    #Collect tag name 'a' and collect 'href' attribute
                    hrefinview = driver.find_elements(By.TAG_NAME , 'a')
                    piclin = [i.get_attribute('href') for i in hrefinview if '.com/p/' in i.get_attribute('href')]
                    uniphoto = [i for i in piclin if i not in uniphoto] 
                    
                except Exception:
                    time.sleep(random.randint(2 , 3))    
            
        print('len of post`s :' , len(uniphoto))    

        q = 1
        # Start to like the post's
        for pic in uniphoto:
            try:
                # Go to post
                driver.get(pic)
                time.sleep(random.randint(24 , 31))

                # Click on Like button 
                driver.find_element(By.XPATH , '//span[@class="_aamw"]//*[@class="_abl-"]').click()
                print(f'post [{q}] liked')
                q += 1
                time.sleep(random.randint(16 , 22))
            except Exception:
                time.sleep(2)
                continue    
    
    #Follow Method
    def follow(self , ids):
   
        'follow the followers of your favorite pages'

        driver = self.driver

        usrlist0 = []
        usrlstuni = []
        uni = []
        for i in ids:
            try:

                time.sleep(random.randint(5 , 9))

                driver.get(f'https://instagram.com/{i}/')

                time.sleep(random.randint(10 , 13))

                print('Collecting username`s ...')
                #Click on followers
                driver.find_element(By.XPATH , '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a/div').click()

                time.sleep(random.randint(10 , 12)) 

                #Collect tag name 'a'
                usrlist = driver.find_elements(By.XPATH , '//a[@class="qi72231t nu7423ey n3hqoq4p r86q59rh b3qcqh3k fq87ekyn bdao358l fsf7x5fv rse6dlih s5oniofx m8h3af8h l7ghb35v kjdc1dyq kmwttqpk srn514ro oxkhqvkx rl78xhln nch0832m cr00lzj9 rn8ck1ys s3jn8y49 icdlwmnq notranslate _a6hd"]')

                #Split href attribute    
                usrlist0 = [usr.get_attribute('href') for usr in usrlist if 'instagram.com/' in usr.get_attribute('href')]
                usrlstuni = [usr for usr in usrlist0 if usr not in usrlstuni]
        
                for user in usrlstuni:
                    if user not in uni:
                        uni.append(user) 

            except Exception:
                continue                       

        print('uniqe username`s : ' , uni)
        print('len of username`s : ' , len(uni))

        time.sleep(random.randint(9 , 13))

        a = 1
        #start to Follow pages
        for ids in uni:
            try:
                time.sleep(random.randint(15 , 23))

                print(f'[{a}]following The {ids}')
                driver.get(ids)

                time.sleep(random.randint(16 , 26))

                time.sleep(random.randint(27 , 35))

                #click on follow button
                driver.find_element(By.XPATH , '//div[text()="Follow"]').click()
                print(f'[{a}]The {ids} followed')
                a += 1
                time.sleep(random.randint(16 , 25))

            except Exception:
                continue

    #Unfollow Method
    def unfollow(self , amount):

        'Unfollow your Followings'

        driver = self.driver
        myprofile = self.username

        links = []
        unilin = []

        for i in range(0 , amount):

            driver.get(f'https://instagram.com/{myprofile}/')

            time.sleep(random.randint(8 , 12))

            print('Collecting username`s ...')

            #click on following 
            driver.find_element(By.XPATH , '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[3]/a/div').click()

            time.sleep(random.randint(9 , 13))

            #Find and collect tag name of 'a'
            userls = driver.find_elements(By.XPATH , '//a[@class="qi72231t nu7423ey n3hqoq4p r86q59rh b3qcqh3k fq87ekyn bdao358l fsf7x5fv rse6dlih s5oniofx m8h3af8h l7ghb35v kjdc1dyq kmwttqpk srn514ro oxkhqvkx rl78xhln nch0832m cr00lzj9 rn8ck1ys s3jn8y49 icdlwmnq notranslate _a6hd"]')

            print('user list :' , userls)

            time.sleep(random.randint(9 , 11))

            #Collect href attribute
            links = [lin.get_attribute('href') for lin in userls if '/' in lin.get_attribute('href')]
            time.sleep(7)

            unilin = [i for i in links if i not in unilin]  

            print('username links : ' , unilin)

            time.sleep(random.randint(4 , 6))

            print('len of username`s to unfollow : ' , len(unilin))    

            z = 1
            #start unFollowing usernames
            for usr in unilin:
                try:
                
                    time.sleep(random.randint(21 , 32))

                    print(f'[{z}]unfollowing {usr}')
                    driver.get(usr)

                    time.sleep(random.randint(22 , 31))

                    #Click on Unfollow button
                    driver.find_element(By.XPATH , '//button[@class="_acan _acap _acat"]//*[@class="_ab8w  _ab94 _ab99 _ab9h _ab9k _ab9p  _ab9- _abcm"]').click()

                    time.sleep(random.randint(20 , 27))

                    #Final Button to unfollow
                    driver.find_element(By.XPATH , '//button[@class="_a9-- _a9-_"]').click()
                    print(f'[{z}]The {usr} Unfollowed')

                    z += 1

                    time.sleep(random.randint(7 , 10))

                except Exception:
                    continue

    def send_direct(self):
        'send message to your followings'

        username = self.username 
        driver = self.driver

        driver.get(f'https://instagram.com/{username}/')

        time.sleep(random.randint(8 , 12))

        #click on following 
        driver.find_element(By.XPATH , '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[3]/a/div').click()

        time.sleep(random.randint(9 , 14))

        #Find and collect tag name of 'a'
        userls = driver.find_elements(By.XPATH , '//a[@class="qi72231t nu7423ey n3hqoq4p r86q59rh b3qcqh3k fq87ekyn bdao358l fsf7x5fv rse6dlih s5oniofx m8h3af8h l7ghb35v kjdc1dyq kmwttqpk srn514ro oxkhqvkx rl78xhln nch0832m cr00lzj9 rn8ck1ys s3jn8y49 icdlwmnq notranslate _a6hd"]')

        print('user list :' , userls)

        time.sleep(random.randint(9 , 11))

        #Collect href attribute
        links = [lin.get_attribute('href') for lin in userls if '/' in lin.get_attribute('href')]
        time.sleep(7)  

        print('username links : ' , links)
        print('len of username`s to send message : ' , len(links))
        time.sleep(random.randint(4 , 6))

        x = 1
        #start Following usernames
        for usr in links:
            try:

                time.sleep(random.randint(6 , 9))

                driver.get(usr)

                print(f'[{x}]sending message to {usr}')

                time.sleep(random.randint(14 , 20))

                #Click on message button
                driver.find_element(By.XPATH , '//div[text()="Message"]').click()

                time.sleep(random.randint(9 , 15))

                #your message file
                mess = ''' 
                      write your message
                    '''

                #send message to box
                driver.find_element(By.XPATH , '//textarea[@placeholder="Message..."]').send_keys(mess)

                time.sleep(random.randint(10 , 20))

                #Click on send button
                driver.find_element(By.XPATH , '//button[text()="Send"]').click()

                print(f'[{x}] message sent to {usr}')
                x += 1

            except Exception:
                continue

    def like_and_follow(self , hashtag):
        pass            

        
                       
username = input('Enter your account username : ')
passwd = input('Enter your account password : ')

account1 = InstaBot(username , passwd)

account1.login()


actions = input(''' -----------------------------------------       
    instarobot.py  |||||||  saeed_abszd_81 
    _____________________________________

     1 : Liking the desired hashtag post's 
     2 : Follow the followers of your page's
     3 : Unfollow your following's
     4 : Send message to your following's 

     Choose one or more options with comma (,) example 1,2,3,4 : ''')

act = actions.split(',')

for i in act:
    
    #like method
    if i == '1':
        print('Part of like ...')
        
        hashtag = input('Enter your desired hashtag : ')
        account1.like(hashtag)

    #Follow method
    elif i == '2':
        print('Part of Follow ...')

        users = input('Enter usernames with comma (,) example instarobot.py,saeed_abszd_81 : ')
        userls = users.split(',')

        account1.follow(userls)

    #Unfollow method
    elif i == '3':
        print('Part of Unfollow ...')

        countr = int(input('Each number is equal to 12 users example 1 = 12 username`s : '))

        account1.unfollow(countr)

    #send direct method
    elif i == '4':
        print('Part of Send-Direct ...')

        account1.send_direct()

    else:
        print('Your desired option was not found !!!')
        print('Try Again you can do it')