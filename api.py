import requests
from bs4 import BeautifulSoup
class Api:
    def __init__(self):
        pass
    def user_cycle_search(self,user):
        cycle = []
        ccle = ''
        cycle_count = requests.get("https://repl.it/@"+user)
        supper = BeautifulSoup(cycle_count.content,'html.parser')
        httm = supper.find('span',{"title":"cycles"})
        httml = str(httm)
        n = httml.split('(')
        l = list(n[1])
        for item in l:

            try:
                int(item)

                cycle.append(item)

            except:
                pass
        return int(ccle.join(cycle))
    def user_description(self,user):
        description = requests.get("https://repl.it/@" + user)
        supper = BeautifulSoup(description.content, 'html.parser')
        httml = supper.find('span', {"class": "Linkify"})
        httm = str(httml)
        x= httm.replace('<span class="Linkify">','')
        s = x.replace('</span>','')
        return s
    def user_most_recent_post(self,user):
        recentos = requests.get("https://repl.it/@"+user+"?tab=posts")
        supper = BeautifulSoup(recentos.content,'html.parser')
        httm = supper.find("div",{"class":"jsx-2329710370 board-post-list-item-post-title"})
        httml = str(httm)
        x = httml.replace('<div class="jsx-2329710370 board-post-list-item-post-title">','')
        s = x.replace('</div>','')
        return s
    def user_most_recent_comment(self,user):
        redollar = requests.get("https://repl.it/@" + user + "?tab=comments")
        supper = BeautifulSoup(redollar.content, 'html.parser')
        httm = supper.find("div", {"class": "rendered-markdown jsx-4279741890"})
        try:
            oop = httm.find('a')
            oop1 = oop.get("href")
        except:
            pass

        httml = str(httm)
        r = httml.replace('<div class="rendered-markdown jsx-4279741890"><p>',
                          '')
        try:
            x = r.replace('<span class="jsx-589677836 user-hover-card user-hover-card-inline">'
                            '<a href="'+oop1+'">','')
        except:
            pass
        s = x.replace('</a></span>','')
        y = s.replace('</p></div>','')
        return y
    def user_most_recent_comment2(self,user):
        redollar = requests.get("https://repl.it/@" + user + "?tab=comments")
        supper = BeautifulSoup(redollar.content, 'html.parser')
        httm = supper.find("div", {"class": "rendered-markdown jsx-4279741890"})
        oop = httm.find('a')
        oop1 = oop.get("href")

        httml = str(httm)
        x = httml.replace('<div class="rendered-markdown jsx-4279741890"><p>',
                          '')

        s = x.replace('</a></span>','')
        y = s.replace('</p></div>','')
        return y


replit = Api()

print(replit.user_description("robowolf"))
