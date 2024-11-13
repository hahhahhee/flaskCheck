# pip install pymongo

from pymongo import MongoClient
connection = MongoClient()    # mongod 인스턴스 생성

# print(connection)


# DB생성
db = connection["Test"]
# print(db)

# 컬렉션 생성
collection = db.AAA
# print(collection)

# create 삽입
# post = {"name" : "user1", 
#         "Timeline" : "I sometimes cry", 
#         "follow" : "200"}

# post = {"name" : "user02", 
#         "Timeline" : "I'm user", 
#         "follow" : 0}

# db.컬렉션명.insertOne(document)
# x = collection.insert_one(post)
# print(x)

# insert_many() : 여러 문서 추가, 리스트에 여러 딕셔너리
# post = [{"name" : "user02", 
#         "Timeline" : "I'm user", 
#         "follow" : 0},
#         {"name" : "wingard", 
#         "Timeline" : "I love them", 
#         "follow" : 200},
#         {"name" : "in_reson", 
#         "Timeline" : "Blade of Destruction", 
#         "follow" : 1}]

# x = collection.insert_many(post)
# print(x)

# CRUD : Read 조회
# fine_one() : 가장 빨리 검색되는 문서 하나 검색, 조건 입력 가능
# x = collection.find_one()
# print(x)

# x = collection.find_one({"name" : "user02"})
# print(x)

# find() 문서전체 검색
print("문서전체 검색")
docs = collection.find()
for doc in docs :
  print(doc)

# 원하는 필드만 조회 : 두번째 인수로 원하는 필드를 넣어준다
# name, Timeline, 조회:1
# _id는 기본이 항상 조회되는 1이므로 0이라고 명시를 하여야 한다. 
# docs = collection.find({},{'_id':0, 'name':1, 'Timeline':1})
# for doc in docs :
#   print(doc)

# follow를 기준으로 내림차순 정렬
# 정렬 : -1은 내림차순, 1은 오름차순
# docs = collection.find().sort({'follow':-1})
# for doc in docs :
#   print(doc)

# docs = collection.find().sort({'follow':1})
# for doc in docs :
#   print(doc)

# docs = collection.find().sort({'name':1})
# for doc in docs :
#   print(doc)

# docs = collection.find().sort({'name':-1})
# for doc in docs :
#   print(doc)

# 조건 추가 follow수가 100이상인 다큐먼트의 name과 follow
# 조건은 첫번째 인수에 기입한다. 
# 연산자 사용 $gt(초과) $gte(이상) $lt(미만) $lte(이하) $ne(같지않음) $or(또는) $in(배열요소중 하나)
# print("조건 추가 follow수가 100이상인 다큐먼트의 name과 follow")
# docs = collection.find({'follow':{'$gte':100}},{'_id':0, 'name':1, 'follow':1})
# for doc in docs :
  # print(doc)

# print("follow int변환")
# $expr는 MongoDB에서 필드 간의 비교나 산술 연산을 수행할 때 사용하는 연산자
# docs = collection.find({'$expr':{'$gte':[{'$toInt':'$follow'},100]}},{'_id':0, 'name':1, 'follow':1})
# for doc in docs :
#   print(doc)

# document 문서의 수
print("document 문서의 수")
docs = collection.count_documents({})
print(docs)

# Update(수정)
# name이 user02인 follow의 수를 80으로 수정하시오
# 첫번째 객체(인수)에 수정할 다큐먼트 지정, 두번째 인수에는 수정할 내용을 입력한다. 
# x = collection.update_one({'name':'user02'},{'$set':{'follow':'100'}})
# print(x)

# 모두 수정
# x = collection.update_many({'name':'user02'},{'$set':{'follow':'100'}})
# print(x)

# user02인 회원을 찾아서 프린트 하시오.
print("user02인 회원을 찾아서 프린트 하시오.")
docs = collection.find({'name':'user02'})
for doc in docs :
  print(doc)

# 삭제 Delete
# x = collection.delete_one({'name':'user02'})
# print(x)
# xs = collection.find()
# for x in xs :
#   print(x)

# 모두 삭제
x = collection.delete_many({'name':'user02'})
print(x)
xs = collection.find()
for x in xs :
  print(x)