from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

target_movie = db.movies.find_one({'title': '월-E'})
target_star = (target_movie['star'])
print(target_star)

movies = list(db.movies.find({'star': target_star}))

for movie in movies:
    print(movie['title'])
# 비효율적
# for movie in movies:
#     db.movies.update_one(movie, {'$set' : {'star' : '9.41'}})

db.movies.update_many({'star' : target_star}, {'$set' : {'star' : '0'}})