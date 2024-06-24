from constants import *
from seleniumbase import Driver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import logging
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import sys

def init_driver():
    try :
        driver=Driver(uc=True,proxy=PROXY)
        log('Driver initiated')
        return driver
    except Exception as e :
        log(f'Could not initiate driver : {e}',logging.ERROR)
        sys.exit()

def log(message, level=logging.INFO):
    print(message)
    logging.log(level, message)
    
def login(driver,account):
    driver.get('https://www.reddit.com/login/')
    time.sleep(2)
    driver.find_element(By.ID,'login-username').send_keys(str(account.username))
    driver.find_element(By.ID,'login-password').send_keys(str(account.psswd)+Keys.ENTER)
    time.sleep(15)
    try :
        if driver.find_element(By.CSS_SELECTOR,'#expand-user-drawer-button > span > span > span > span > img') :
            log(f'Logged in as {account.username}')
    except :
        try :
            driver.refresh()
            time.sleep(5)
            if driver.find_element(By.CSS_SELECTOR,'#expand-user-drawer-button > span > span > span > span > img') :
                log(f'Logged in as {account.username}')
        except :
            driver.get('https://www.reddit.com/login/')
            time.sleep(2)
            driver.find_element(By.ID,'login-username').send_keys(account.username)
            driver.find_element(By.ID,'login-password').send_keys(account.psswd+Keys.ENTER)
            time.sleep(20)
            if driver.find_element(By.CSS_SELECTOR,'#expand-user-drawer-button > span > span > span > span > img') :
                    log(f'Logged in as {account.username}')

def upvote_post(url,url2,account):
    if AUTO_JOIN :
        try :
            join_subreddit(url2,account)
        except Exception as e :
            log(f'Could not join subbreddit as {account.username}')
            raise(e)
    driver=init_driver()
    try :
        login(driver,account)
    except Exception as e :
        log(f'Could not login as {account.username}')
        raise(e)
    driver.get(url)
    time.sleep(2)
    post=driver.find_element(By.TAG_NAME,'shreddit-post')
    shadow=driver.execute_script('return arguments[0].shadowRoot',post)
    try :
        shadow.find_element(By.CSS_SELECTOR,'div.flex.flex-row.items-center.flex-nowrap.overflow-hidden.justify-start.h-2xl.mt-md.px-md.xs\:px-0 > span > span > button.group.button.flex.justify-center.aspect-square.p-0.border-0.button-secondary.disabled\:text-interactive-content-disabled.button-plain.inline-flex.items-center.hover\:text-action-upvote.focus-visible\:text-action-upvote').click()
        log(f'Upvoted post : {url} as {account.username}')
    except :
        shadow.find_element(By.CSS_SELECTOR,'div.flex.flex-row.items-center.flex-nowrap.overflow-hidden.justify-start.h-2xl.mt-md.px-md.xs\:px-0 > span > span > button:nth-child(1)').click()
        log(f'Upvoted post : {url} as {account.username}')
    driver.quit()

def downvote_post(url,url2,account):
    if AUTO_JOIN :
        try :
            join_subreddit(url2,account)
        except Exception as e :
            log(f'Could not join subbreddit as {account.username}')
            raise(e)
    driver=init_driver()
    try :
        login(driver,account)
    except Exception as e :
        log(f'Could not login as {account.username}')
        raise(e)
    driver.get(url)
    time.sleep(2)
    post=driver.find_element(By.TAG_NAME,'shreddit-post')
    shadow=driver.execute_script('return arguments[0].shadowRoot',post)
    try :
        shadow.find_element(By.CSS_SELECTOR,'div.flex.flex-row.items-center.flex-nowrap.overflow-hidden.justify-start.h-2xl.mt-md.px-md.xs\:px-0 > span > span > button.group.button.flex.justify-center.aspect-square.p-0.border-0.button-secondary.disabled\:text-interactive-content-disabled.button-plain.inline-flex.items-center.hover\:text-action-downvote.focus-visible\:text-action-downvote').click()
        log(f'Downvoted post : {url} as {account.username}')
    except :
        shadow.find_element(By.CSS_SELECTOR,'div.flex.flex-row.items-center.flex-nowrap.overflow-hidden.justify-start.h-2xl.mt-md.px-md.xs\:px-0 > span > span > button:nth-child(3)').click()
        log(f'Downvoted post : {url} as {account.username}')
    driver.quit()
def upvote_comment(url,url2,account):
    if AUTO_JOIN :
        try :
            join_subreddit(url2,account)
        except Exception as e :
            log(f'Could not join subbreddit as {account.username}')
            raise(e)
    driver=init_driver()
    try :
        login(driver,account)
    except Exception as e :
        log(f'Could not login as {account.username}')
        raise(e)
    driver.get(url)
    time.sleep(2)
    comment=driver.find_element(By.TAG_NAME,'shreddit-comment-action-row')
    shadow=driver.execute_script('return arguments[0].shadowRoot',comment)
    try :
        shadow.find_element(By.CSS_SELECTOR,'div > div > span > button.group.button.flex.justify-center.aspect-square.p-0.border-0.button-plain.disabled\:text-interactive-content-disabled.disabled\:text-interactive-content-disabled.button-plain.inline-flex.items-center.hover\:text-action-upvote.focus-visible\:text-action-upvote').click()
        log(f'Upvoted comment :{url} as {account.username}')
    except :
        shadow.find_element(By.CSS_SELECTOR,'div > div > span > button.group.button.flex.justify-center.aspect-square.p-0.border-0.button-plain.disabled\:text-interactive-content-disabled.false.button-plain.inline-flex.items-center.hover\:text-action-upvote.focus-visible\:text-action-upvote').click()
        log(f'Upvoted comment : {url} as {account.username}')
    driver.quit()
def downvote_comment(url,url2,account):
    if AUTO_JOIN :
        try :
            join_subreddit(url2,account)
        except Exception as e :
            log(f'Could not join subbreddit as {account.username}')
            raise(e)
    driver=init_driver()
    try :
        login(driver,account)
    except Exception as e :
        log(f'Could not login as {account.username}')
        raise(e)
    driver.get(url)
    time.sleep(2)
    comment=driver.find_element(By.TAG_NAME,'shreddit-comment-action-row')
    shadow=driver.execute_script('return arguments[0].shadowRoot',comment)
    try :
        shadow.find_element(By.CSS_SELECTOR,'div > div > span > button.group.button.flex.justify-center.aspect-square.p-0.border-0.button-plain.disabled\:text-interactive-content-disabled.disabled\:text-interactive-content-disabled.button-plain.inline-flex.items-center.hover\:text-action-downvote.focus-visible\:text-action-downvote').click()
        log(f'Downvoted comment : {url} as {account.username}')
    except :
        shadow.find_element(By.CSS_SELECTOR,'div > div > span > button.group.button.flex.justify-center.aspect-square.p-0.border-0.button-plain.disabled\:text-interactive-content-disabled.false.button-plain.inline-flex.items-center.hover\:text-action-downvote.focus-visible\:text-action-downvote').click()
        log(f'Downvoted comment : {url} as {account.username}')
    driver.quit()
def comment_post(url,url2,account,comment):
    if AUTO_JOIN :
        try :
            join_subreddit(url2,account)
        except Exception as e :
            log(f'Could not join subbreddit as {account.username}')
            raise(e)
    driver=init_driver()
    try :
        login(driver,account)
    except Exception as e :
        log(f'Could not login as {account.username}')
        raise(e)
    driver.get(url)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,'#main-content > shreddit-async-loader > comment-body-header > shreddit-async-loader:nth-child(1) > comment-composer-host > faceplate-tracker:nth-child(1) > button').click()
    time.sleep(1)
    driver.find_element(By.TAG_NAME,'shreddit-composer').send_keys(str(comment))
    driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
    time.sleep(10)
    log(f'Commented : {comment} post : {url} as {account.username}')
    driver.quit()
def join_subreddit(url,account) :
    driver=init_driver()
    try :
        login(driver,account)
    except Exception as e :
        log(f'Could not login as {account.username}')
        raise(e)
    driver.get(url)
    time.sleep(3)
    subred=driver.find_element(By.TAG_NAME,'shreddit-subreddit-header-buttons')
    shawdow=driver.execute_script('return arguments[0].shadowRoot',subred)
    button=shawdow.find_element(By.CSS_SELECTOR,'div > faceplate-tracker > shreddit-join-button')
    if 'subscribed="">' in button.get_attribute("outerHTML") :
        log(f'Subreddit : {url} already joined by {account.username}',logging.WARNING)
    else :
        button.click()
        time.sleep(5)
        log(f'Subreddit : {url} joined as {account.username}')
    driver.quit()
def get_accounts(elem) :
        acc_list=[]
        if elem.nacc=='ALL' or int(elem.nacc)>len(ACCOUNTS) or int(elem.nacc)<0 :
            acc_list=ACCOUNTS
        else : 
            acc_list= random.sample(ACCOUNTS,elem.nacc)
        log(f'Accounts selected : {[a.username for a in acc_list]}')
        return acc_list





if __name__=='__main__':
    logging.basicConfig(filename='Log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    log('============ STARTED EXECUTION =============')

    '''
    Setting up virtual display for linux :
    import subprocess
    command = ["Xvfb", ":99", "-screen", "0", "1024x768x24", "&"]
    process = subprocess.Popen(command)
    os.environ["DISPLAY"] = ":99"
    '''
    
    for elem in UPVOTE_POST :
            for acc in get_accounts(elem) :
                try :
                    upvote_post(elem.url,elem.url2,acc)
                except Exception as e:
                    log(f'Could not upvote post {elem.url} as {acc}, error {e} : skipping..',logging.WARNING)
                    continue
                time.sleep(UPVOTE_POST_SLEEP)
            log(f'Finished post upvoting, sleeping for {SLEEP_TIME} seconds ')
            time.sleep(SLEEP_TIME)

    for elem in DOWNVOTE_POST :
        for acc in get_accounts(elem) :
            try :
                downvote_post(elem.url,elem.url2,acc)           
            except Exception as e:
                log(f'Could not downvote post {elem.url} as {acc}, error {e} : skipping..',logging.WARNING)
                continue
            time.sleep(DOWNVOTE_POST_SLEEP)
        log(f'Finished post downvoting, sleeping for {SLEEP_TIME} seconds ')
        time.sleep(SLEEP_TIME)
        
    for elem in UPVOTE_COMMENT :
        for acc in get_accounts(elem) :
            try :
                upvote_comment(elem.url,elem.url2,acc)
            except Exception as e:
                log(f'Could not upvote comment {elem.url} as {acc}, error {e} : skipping..',logging.WARNING)
                continue
            time.sleep(UPVOTE_COMMENT_SLEEP)
        log(f'Finished comment upvoting, sleeping for {SLEEP_TIME} seconds ')
        time.sleep(SLEEP_TIME)

    for elem in DOWNVOTE_COMMENT :
        for acc in get_accounts(elem) :
            try :   
                downvote_comment(elem.url,elem.url2,acc)
            except Exception as e:
                log(f'Could not downvote comment {elem.url} as {acc}, error {e} : skipping..',logging.WARNING)   
                continue         
            time.sleep(DOWNVOTE_COMMENT_SLEEP)
        log(f'Finished comment downvoting, sleeping for {SLEEP_TIME} seconds ')
        time.sleep(SLEEP_TIME)

    for elem in COMMENT_ON_POST :
        for acc in get_accounts(elem) :
            try :
                comment_post(elem.url,elem.url2,acc,elem.comment)
            except Exception as e:
                log(f'Could not comment post {elem.url} as {acc}, error {e} : skipping..',logging.WARNING)
                continue
            time.sleep(COMMENT_ON_POST_SLEEP)
        log(f'Finished commentting post, sleeping for {SLEEP_TIME*2} seconds ')
        time.sleep(SLEEP_TIME*2)

    for elem in JOIN_SUBREDDIT :
        for acc in get_accounts(elem) :
            try :
                join_subreddit(elem.url,acc)
            except Exception as e:
                log(f'Could not join {elem.url} as {acc}, error {e} : skipping..',logging.WARNING)
                continue
            time.sleep(JOIN_SUBREDDIT_SLEEP)
        log(f'Finished Joining subreddit, sleeping for {SLEEP_TIME*2} seconds ')
        time.sleep(SLEEP_TIME*2)

    log('============ FINISHED EXECUTION =============')
