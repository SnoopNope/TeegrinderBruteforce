import urllib2
import re
import webbrowser
import time

"""
Credit for the method goes to Sawboo from YouTube
(http://www.youtube.com/watch?v=SGiDvmCYASE)

I updated the script to use the urllib2 module instead of requests, so it'll
work on Python versions below 2.7.5. Also rewrote it a little to fit my
coding style.

Notes: The searching will take a really long time if you're trying to match 3. 
With 7 choices, it still took me over 7000 requests to get a match.
"""


""" BEGIN OPTIONS """
# number of shirts to match (range: 1-3)
MATCH_NUMBER = 3

# your shirt size (S, M, L, XL, 2XL)
SIZE = 'L'

# your gender (M, F)
GENDER = 'M'

# cookie format (without quotes): "SESSION_SERVER=???; PHPSESSID=???"
# get both values from your browser. i trust you're able to do so.
COOKIE = 'SESSION_SERVER=INSTANCE_02; PHPSESSID=sampleSessionId'

# user agent. also i trust you're able to get this.
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107'

# image name of the shirts you want. to get them just grind till you see a
# shirt you like, then copy its url. you don't need the full url, just
# the image name will do. e.g. ('cool-shirt-250x0.png')
# more shirts will mean shorter search times.
SHIRTS = [
            'samurai-resurrection-mens-front-250x0.png',
            'native-upheaval-mens-front-250x0.png',
            'to-serve-and-protect-with-humor-mens-front-250x0.png',
         ]

# delay in seconds between grinds. don't spam their servers!
DELAY = 1

# number of bundles to find before stopping. useful if you're going to let
# the script run unsupervised and want different combinations to choose from
# when you get back.
BUNDLES_TO_FIND = 5
""" END OPTIONS """


HEADERS = {'User-Agent': USER_AGENT, 'Cookie': COOKIE}

def add_to_cart(bundle, key):
    print 'Adding to cart...'
    url = 'http://www.designbyhumans.com/a/ShowCartOverlay?product_attributes=%s&_=%s' % (bundle, key)
    req = urllib2.Request(url, headers=HEADERS)
    res = urllib2.urlopen(req)
    if res.getcode() == 200:
        webbrowser.open('http://www.designbyhumans.com/cart/')

def grind():
        url = 'http://www.designbyhumans.com/a/TeeGrind?gender=%s&size=%s&_=1376135318369' % (GENDER, SIZE)
        req = urllib2.Request(url, headers=HEADERS)
        count = 0

        while True:
            try:
                res = urllib2.urlopen(req).read()
                matched_shirts = 0
                for shirt in SHIRTS:
                    result = re.findall(shirt, res)
                    if result != []:
                        matched_shirts += 1
                
                if matched_shirts != MATCH_NUMBER:
                    print '[%s] Not enough matches (%s/%s)' % (count, matched_shirts, MATCH_NUMBER)
                    count += 1
                    time.sleep(DELAY)
                    continue
                else:
                    break
            except Exception, e:
                print e
                continue

        bundle = re.findall('"bundle_id":"(.*)"}', res)[0]
        key = re.findall('"_":"(.*)","gender"', res)[0]
        return bundle, key

if __name__ == '__main__':
    count = 0
    while count < BUNDLES_TO_FIND:
        bundle, key = grind()
        print 'Match found!'
        add_to_cart(bundle, key)
        count += 1
