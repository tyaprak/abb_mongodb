import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.abbr
conn = db.abbr

class Data:
    def __init__(self,abb):
        self.abb=abb.upper()
        self.target = { "abbr":abb }
        self.data=conn.find(self.target)
        for i in self.data:
            self.ff=i["fullforms"]
            self.count=i["v"]
        try:
            if len(self.ff)>0:
                self.isok=True
        except:
            self.isok=False
    def sayac_arttir(self):
        inc= { "$inc": { "v": 1 } }
        conn.update_one(self.target,inc)
    def veri_ekle(self,yeni):
        push= { "$push": { "fullforms": yeni } }
        conn.update_one(self.target,push)
    def kayit_olustur(self,ff):
        veri={
            "abbr":self.abb,
            "fullforms":[ff],
            "v":0
        }
        conn.insert_one(veri)
