import httplib

urls=[
  'www.google.com',
  'www.facebook.com',
  'www.apple.com'
]

class Uptime:
  def __init__(self, url):
    self.url = url

  def testURL(self):
    try:
        conn = httplib.HTTPConnection(self.url)
        conn.request("HEAD", "/")
        print conn.getresponse().status
    except StandardError:
        print None


for url in urls:
  result = Uptime(url)
  result.testURL()