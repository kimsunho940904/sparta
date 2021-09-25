from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만듭니다.

# Create(생성)
user1 = {'name': '론', 'age': 40}
user2 = {'name': '해리', 'age': 40}
db.users.insert_one(user1)
db.users.insert_one(user2)

# Read(조회) - 한 개 값만
user = db.users.find_one({'name': '론'})

# Read(조회) - 여러 값 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age': 40}, {'_id': False}))

# Update(업데이트) - 여러 값
db.people.update_many({'age': 40}, { '$set': {'age': 70}})

# Update(업데이트) - 하나 값
db.users.update_one({'name': '론'}, {'$set': {'age': 116}})

# Delete(삭제)
db.users.delete_one({'name': '론'})