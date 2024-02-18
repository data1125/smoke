# # # # def miss(day):
# # # #     for dd in range(1,day+1):
# # # #         print(f"书桓走的第{dd}天,想他!")

# # # # miss(2)
# # # # miss(100)
# # # # color = "red"
# # # # if color == "red":
# # # #     print("it's a tomato")
# # # # elif color == "green":
# # # #     print("it's a green pepper")
# # # # elif color == "bee purple":
# # # #     print("i don't know what it is, but only bees can see it")
# # # # else:
# # # #     print("i've never heard of the color", )
# # # # letter='h'
# # # # a="this is your"
# # # # if letter == 'a' or letter == "e" or letter == "i"\
# # # #     or letter == "o" or letter == "u":
# # # #     print(f"{a}" ' a vowel')
# # # # else:
# # # #     print(f"{a}", " not a vowel")
# # # #############59
# # # # some_list=[]
# # # # if some_list:
# # # #     print("There's something in here")
# # # # else:
# # # #     print("key,it's empty!")
# # # ###########60
# # # # vowels= "aeiou"
# # # # letter="h"
# # # # vowels in letter 
# # # # if vowels in letter :
# # # #     print(vowels, "is a vowel")
# # # # else:
# # # #     print("funk")
# # # # letter="v"
# # # # vowel_set={'a','e','i','o','u'}
# # # # print(letter in vowel_set)
# # # # x=6
# # # # print(5<x and x>10)
# # # # print(5<x or x <10)
# # # # print(5<x and not x>10)
# # # #################61
# # # # tweet_limit=280
# # # # tweet_string= "blch"*50
# # # # diff=tweet_limit-len(tweet_string)
# # # # if diff>=90:
# # # #     print("A fitting tweet")
# # # # else:
# # # #     print("went over by",abs(diff))
# # # # tweet_limit=280
# # # # tweet_string= "blch"*50

# # # # if diff:=tweet_limit-len(tweet_string)>=0:
# # # #     print("A fitting tweet")
# # # # else:
# # # #     print("went over by",abs(diff))

# # # # secret=5
# # # # guess=5
# # # # if guess < secret:
# # # #     print("too low")
# # # # elif guess > secret:
# # # #     print("too high")
# # # # else:
# # # #     print("just right")
# # # # small = True
# # # # green = False
# # # # if small:
# # # #     if  green:
# # # #         print("pea")
# # # #     else:
# # # #         print("cherry")
# # # # else:
# # # #     if green:
# # # #         print("wetermelon")
# # # #     else:
# # # #         print("pumpkin")    
# # # # ################65
# # # # poem2="""I do not like thee, Doctor Fell.
# # # #     The reason why, I connot tell.
# # # #     but this I know, and know full well:
# # # #     I do not like thee, Doctor Fell"""
# # # # print(poem2)
# # # # print("give","us","""some""","""space""")
# # # #################66
# # # # num=input("你輸入數字")
# # # # print(type(int(num)))
# # # # print("a\tbv")
# # # # testimony="\"I did nothing!\" he said. \" or that oter thing.\""
# # # # print(testimony)
# # # # speech="The backslash\\bends over backwards to please you."
# # # # print(speech)
# # # # info=r"Type a \n to get a new line in a normal string"   
# # # # print(info)################取消換行
# # # # poem=r'''Boys and girls, come out to play.
# # # # the moon doth shine as bright as day.'''
# # # # print(poem)################原本已經換行+r 還是會換行
# # # ###############################68
# # # # a="release the kraken!"+ "no,wait!"
# # # # print(a)
# # # # a="duck"
# # # # b=a
# # # # c="grey duck"
# # # # print(a,b,c)
# # # #############################69
# # # # letters="abcdefghijklmnopqrstuvwxyz"
# # # # print(letters[100])
# # # # name='Henny'
# # # # print(name.replace("H","A"))
# # # ############################70
# # # # letters="abcdefghijklmnopqrstuvwxyz"
# # # # print(letters[:])
# # # # letters="abcdefghijklmnopqrstuvwxyz"
# # # # print(letters[20:])
# # # # letters="abcdefghijklmnopqrstuvwxyz"
# # # # print(letters[10:])
# # # # letters="abcdefghijklmnopqrstuvwxyz"
# # # # print(letters[12:15])
# # # # letters="abcdefghijklmnopqrstuvwxyz"
# # # # print(letters[::4])
# # # # letters="abcdefghijklmnopqrstuvwxyz"
# # # # print(letters[4:20:3])字母第4個開始間隔3個到第20個
# # # # letters="abcdefghijklmnopqrstuvwxyz"
# # # # print(letters[19::4]) 字母第19個開始間隔4個
# # # # letters="abcdefghijklmnopqrstuvwxyz"
# # # # print(letters[::-1]) 字母倒過來
# # # ######################73
# # # # letters="abcdefghijklmnopqrstuvwxyz"
# # # # print(len(letters))  計算長度  比如有26個字母
# # # # empty=""
# # # # print(len(empty))    符號不算 顯示文字長度
# # # # tasks="get gloves,get mask,give cat vitamins,call ambulance"
# # # # print(tasks.split())任務分割
# # # #######################74
# # # # crypto_list=["Yeti","Bigfoot","Loch Ness Monster"]
# # # # crypto_string=','.join(crypto_list)
# # # # print("Found and signing book deals:",crypto_string)兩段文字結合再一起
# # # # setup="a duck goes into a bar"
# # # # # print(setup.replace("duck","marmoset"))
# # # # print(setup.replace('a','a famous 100'))       替換
# # # #######################75
# # # # world="  earth "
# # # # print(world.strip("@"))
# # # # blurt="what the....!!?"
# # # # print(blurt.strip(".?!"))
# # # import string
# # # # blurt= "what the !!safdf%%"
# # # # # prospector="what in  tarnation.....??!!"
# # # # # print(prospector.strip(string.whitespace+string.punctuation))
# # # # print(blurt.strip(string.punctuation))
# # # ################################76 77 搜尋與選擇
# # # # poem='''all that doth flow we cannot liquid name
# # # #   or else would fire and water  be the same;
# # # #      but that is liquid which is moist and wet
# # # #       ire that property can never get.funny
# # # #      then 'tis not cold that doth the fire put out
# # # # but   tis the wet that makes it die, no doubt '''
# # # # # # word="the"
# # # # # print(poem.isalnum())
# # # # ################################78 79 字母大小變換
# # # # setup="a duck goes into a bar"
# # # # print(poem.rjust(50))
# # # ############################80
# # # # actor="Richard Gere"
# # # # cat="chester"
# # # # weight=29
# # # # print("my wife's favorite actor is %s" % actor)
# # # # a=42
# # # # print("%s" % a)
# # # #############################81 82 83

# # # # thing="woodchuck"
# # # # print("%.3s"% thing)
# # # # thing=98.6
# # # # print("%.1f"% thing)
# # # # thing=9876
# # # # print("%3d"% thing)
# # # # thing="woodchuck"
# # # # place="lake"
# # # # # print("The {} is in the {}".format(thing,place))
# # # # # print("the {0} is in the {0}".format(thing,place))
# # # # # print("the {thing} is in the {place}".format(thing="duck",place="baththb"))
# # # # d={"thing": "duck","place":"bathtub"}
# # # # print("the {0[thing]} is in the {0[place]}".format(d))
# # # # ###################################84 85
# # # # thing="wraith"
# # # # place="window"
# # # # # print("the{:!^8s}is at the{:^8s}".format(thing,place))
# # # # # thing="wereduck"
# # # # # place="werepond"
# # # # # # print(f"the {thing} is in the {place}")
# # # # # print(f"the {thing.capitalize()} is in the {place.rjust(40)}")
# # # # print(f"{thing[1:]=},{place[2:]=}")

# # # #############################85 86
# # # # song=""" when an eel grabs your arm,
# # # # and it cauases great harm,
# # # # that's - a moray!"""
# # # # song= song.replace("m", "M")
# # # # print(song)
# # # # questions=[
# # # #     "we don't serve strings around here. are you a string?",
# # # #     "what is said Father's day in the forest?",
# # # #     "what makes the sound 'sis! Boom! bah!'?"
# # # # ]
# # # # answers=[
# # # #     "an exploding sheep.",
# # # #     "no, i'm a frayed knot.",
# # # #     "'pop! goes the weasel."
# # # # ]
# # # # q_a=((0, 1), (1, 2), (2, 0))
# # # # for q,a in q_a:
# # # #     print("Q:",questions[q])
# # # #     print("A:", answers[a])
# # # #     print() #Q A 的空格

# # # letter="""Thank you for your letter. we are sorry that our {product}
# # # {verbed} in your {room}. please note that it should never
# # # be used in a {room}, especially near any {animals}.

# # # send us your receipt and {amount} for shipping and handing.
# # # we will send you another {product} that, in our tests,
# # # is {percent}% less likely to have {verbed}.

# # # thank you for your support.
# # # sincerely
# # # {spokesman}
# # # {job_title}"""

# # # print(letter.format(
# # #     salutation="ambassador",
# # #     name="Nibbler",
# # #     product="pudding",
# # #     verbed="evaporated",
# # #     room="gazebo",
# # #     animals="octothorpes",
# # #     amount="$1.99",
# # #     percent=88,
# # #     spokesman="shirley iugeste",
# # #     job_title="I Hate this job"))

# # #############################89

# # # count=0
# # # while count<= 5:
# # #     print(count)
# # #     count+=1#   # 不加count+=1 會無限11111  加了之後會123456....

# # # while True:
# # #     stuff = input("String to capitalize [type q to quit]:")
# # #     if stuff == "q":
# # #         break
# # #     print(stuff.capitalize())

# # # while True:
# # #     value = input("Integer, please [q to quit]")
# # #     if value == 'q':  #退出
# # #        break
# # #     number = int(value)
# # #     if number % 2 == 0:  #偶數
# # #         continue
# # #     print(number, "squared is", number*number)

# # # numbers = [7, 3, 5]
# # # position = 0 
# # # while position < len(numbers):
# # #     number = numbers[position]
# # #     if number % 2 == 0:
# # #         print("Found even number",number)
# # #         break
# # #     position +=1
# # # else:   ########break 沒有被呼叫
# # #     print("No even number found")

# # # word = "thud"
# # # offset = 0 
# # # while offset < len(word):  ########第一種
# # #     print(word[offset])
# # #     offset +=1

# # # # for letter in word:   #############第二種
# # # #     print(letter)

# # # for letter in word:    ##############第三種
# # #     if letter == "d":
# # #         break
# # #     print(letter)

# # #####################################94
# # # list( range(0, 11, 3))
# # # # list( range(2, -1, -1))
# # # for i in range(0, 11, 3):
# # #     print(i)

# # # list (range(5, -1, -1, ))
# # # for x in range(5, -1, -1, ):    #########從5開始 到-1  每間格遞數-1  會等於543210
# # #     print(x)


# # guess_me=7
# # number=1
# # while  True #######################################一定要加True 讓if更完整
# #     if  number < guess_me:  
# #         print("too low")
# #     elif  number == guess_me:
# #         print("found it!")
# #         break #######################################一定要加break 才會停止
# #     elif  number > guess_me:
# #         print("oops")
# #         break  
# #     number+= 1

# # guess_me=5

# # for number in range(10):
# #     if  number < guess_me:
# #         print("too low")
# #     elif  number == guess_me:
# #         print("found it!")
# #      #######################################一定要加break 才會停止
# #     else:
# #         print("oops")
        
# #     number+= 1

# ################################################96    97 tuple 
# enpty_tuple=()
# print(enpty_tuple)
# one_marx = ("Groucho", "hello","3.14") 
# print(type(one_marx))
# print(one_marx)
# # 创建一个元组
# my_tuple = (1, 2, 3, 'a', 'b', 'c')

# # 访问元组中的元素
# print("第一个元素:", my_tuple[0])  # 输出: 第一个元素: 1
# print("最后一个元素:", my_tuple[-1])  # 输出: 最后一个元素: c

# # 元组是不可变的，尝试修改元素会引发错误
# # my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment

# # 元组可以包含不同类型的元素
# another_tuple = ('apple', 3.14, True)

# # 可以通过索引访问不同类型的元素
# print("元组中的字符串:", another_tuple[0])  # 输出: 元组中的字符串: apple
# print("元组中的浮点数:", another_tuple[1])  # 输出: 元组中的浮点数: 3.14
# print("元组中的布尔值:", another_tuple[2])  # 输出: 元组中的布尔值: True

# marx_tuple = ("Groucho", 3.14, "Harpo")
# a, b, c =marx_tuple
# print(type(b))


# password = "swordfish"
# icecream = "tuttifrutti"
# password, icecream = icecream, password  #######################tuple  來對調值
# print(password)

# marx_list = ("Groucho",) +  ("chico", "harpo")
# marx_list = ("how", "are", "you")*3
# print(tuple(marx_list))
# a=(4,2)
# b=(4,2,5)
# print(a==b)
##########################################################98  99   100
# words = ("fresh", "out", "of", "ideas")
# for words in words:   #############################有for就印出直行列表
#     print(words)
# t1 = ("fee", "fie", "foe")
# t2 = ("flop",)
# # print(id(t1))
# # t1 += t2
# # print(id(t1))
# # t1 = ("fee", "fie", "foe")
# # t2 = t1
# print(id(t1) == id(t2))  # 输出: True，t1 和 t2 引用了同一个元组对象

# empty_list = []
# weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# big_birds = ["emu", "ostrich", "casswary"]
# first_names = ["Graham", "John", "Terry", "Terry", "Michael"]
# leap_years = [2000, 2004, 2008]
# randomness = ["Punxsatawney", {"groundhog":"Phil"}, "Feb. 2"]
############################# list
# another_empty_list = list("cat") ####list("cat")印出["c","a","t"]   list=("cat")印出cat 
# print(another_empty_list)

# a_tuple = ("ready", "fire", "aim")
# print(list (a_tuple))

# talk_like_a_pirate_day = "9/19/2019"
# print(talk_like_a_pirate_day.split("/"))
# splitme = "a/b/ /c/d///e"
# print(splitme.split("/"))
# text = input("請輸入")

# #convert to uppercase
# #display on the screen
# print(text.lower())
# movies = ["Avatar", "Titanic", "Avengers", "mango"]
# movies.pop(0)
# print(movies)
# # colors = ["Red", "Blue", "Yellow"]
# # colors.insert(1, "pink")
# # print(colors)
#################################################101 102 103
####append , insert , offset , slice extend , pop , offset ,clear, index(要在print裡面)

# number = ["ab", "cd", "ef", "gh", "tt"]
# number [1:3] = [6, 7, 4, 5]  ###### 1以前不動  可以任意加多少
# number [1:3] = "wat?"
# del number [-1]
# number.remove(1)
# number.pop(1)
# print(number.index("ab"))
# print("aa" in number)

# my_string = ("Groucho", "Chico", "Garpo", "Shico")
# marxes = [1, 3, 5, 0]
# # marxes [0] = "apple" 
# # marxes.append("Zeppo")
# # marxes.insert(2, "Gummo")
# others =["Gummo", "Karl"]
# marxes.extend(others)
# print(marxes)
# separator = " ."
# joined = separator.join(marxes)
# print(joined)
# separated = marxes.split("/")
# print(separated)
# my_string = "apple,banana,orange,grape,mango"
# result = my_string.split(',', 1000000000)
# print(result)  # 输出：['apple', 'banana', 'orange,grape,mango']
# sorted_marxes = sorted(marxes)+
# my_string = "Hello World"
#############################################################109  110  111
# marxes = ["Groucho", "Chico", "Harpo", "Shico"]
# # 将列表中的英文单词首字母变为小写
# lowercase_marxes = [name.lower() for name in marxes]
# # 按照字母顺序排序
# sorted_lowercase_marxes = sorted(lowercase_marxes)
# # 输出排序后的列表
# print(sorted_lowercase_marxes)

# thing = ("mozzarella", "cinderella", "salmonella")
# things = tuple(s.capitalize() for s in thing)   #####capitalize 首字母大寫
# print(things)


# numbers = [2, 1, 4.0, 3]
# numbers.sort()   #########sort = 從小排到大
# print(numbers)
# numbers.sort(reverse= True)  ###sort = 從小排到大  再 ###reverse 從大排到小
# print(len(numbers))

# a = [1, 2, 3]
# print(a)
# b = a
# print(b)
# a [0] = "surprise"
# b [0] = "I hate surprises"
# print(a)

# a = [1, 2, 3]
# b = a.copy()     ######a.copy 改變任何變數都不會影響 b.c.d
# c = list(a)
# d = a [:]
# a [0] = "integer lists are boring"
# a [2] = [8, 9]
####################################################112  113 
# import copy
# a = [1, 2, [8, 9]]
# b = copy.deepcopy(a)
# c =list(a)
# d = a[:]
# a [2] [1] = 10
# print(b)

# cheeses = ["brie", "gjetost", "havarti"]
# for cheese in cheeses:
#     if cheese.startswith("g"):
#         print("I won't eat anything that starts with 'g'")
#         break
#     else:
#         print(cheese)

###############################################114
# cheeses = []
# for cheese in cheeses:
#     print("this shop has some lovely', cheese")
#     break
# else:
#     print("this is not much of a cheese shop =, is it?")
#################################################################用zip 讓變數裡一一對應其他變數
# days = ["moday", "Tuesday", "wednesday"]
# fruits = ["banana", "orange", "peach"]
# drinks = ["coffee", "tea", "beer"]
# desserts = ["tirmisu", "ice cream", "pie", "pudding"]
# for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
#     print(day, ": drink", drink, "-eat", fruit, "-enjoy", dessert)

# english = "Monday", "Tuesday", "wednesday"
# french = "lundi", "mardi", "mercredi"
# print(dict(zip(english, french)))

# number_list = []
# number_list.append(1)
# number_list.append(2)
# number_list.append(3)
# number_list.append(4)
# number_list.append(5)
# print(number_list)

# for number in range(1, 60):
#     number_list.append(number)
# print(number_list)

# number_list = list(range(1, 6))
# print(number_list)

# number_list =[number-1 for number in range(1, 5)]
# print(number_list)

# a_list = [number for number in range(0 ,6) if number % 2 ==0]
# a_list = []
# for number in range(0, 8):
#     if number % 1 == 0:
#       a_list.append(number)
#     print(a_list)

# a_list = list(range(1, 8))
# for _ in range(len(a_list), 0, -1):
#     print(' '.join(map(str, a_list)))
#     a_list.pop()

# for i in range(1, 7):
#     for j in range(1, i + 1):
#         print(j, end= "")
#     print()

# rows = range(0, 2)
# cols = range(0, 10)
# for row in rows:
#     for col in cols:
#         print(row, col)

# w = input("請輸入數字")
# s  = input("請輸入數字")
# x = input("請輸入數字")
# z =  input("請輸入數字")   
# cols = range(1,  7)
# rows = range(1, 4)

# cells = [(col, row)for col in cols for row in rows]
# for row, col in cells:    ###########加了這一行顯示兩個數字中間沒有逗點  11  22  33
#       if  col<= 3:
#           print(col)

# for cell in range(1,   10000):
#        print(cell / 100.0)     #10.0   100.0   1000.0  數字越大,顯示小數點後位越多

# small_birds = ["hummingbird", "finch"]
# extingct_birds = ["dodo", "passenger pigeon", "Norwegian Blue" ]
# carol_birds = [3, "French hens", 2, "turtledoves"]
# all_birds = [small_birds, extingct_birds, carol_birds]
# print(all_birds[1][0])   ################取print(all_birds[1]extingct_birds [0]dodo)

# number_thing = (number for number in range(1, 6))
# print(type(number_thing))

######################################################119
# 7.1
# x= int(input("請輸入你出生年份"))
# years_list =[1980, 1981, 1982, 1983, 1984, 1985]  
# # print(years_list[5])
# if  x in years_list:
#     print(f"你是{x}出生的")
# else:
#     print("你猜錯了")

# thing = ["mozzarella", "cinderella", "salmonella"]
# # # things = [i for i in thing]
# # # print(things)
# print(thing[1].capitalize())
# print(thing)
# thing[1] = thing[1].capitalize()
# thing[0] = thing [0].upper()
# thing.remove("salmonella")
# del thing[0:2]
# print(thing)

# print(thing)
# name = "ada lovelace"
# print(name.title())    ##########使用title 變數不能有括號

# surprise = ["Groucho", "Chico", "Harpo"]
# surprise[2] = surprise[2].lower()
# surprise[2] = surprise[2][::-1]
# print(surprise[2].capitalize())

# even = [number for number in range(10) if number % 2 == 0]
# print(even)

# start1 = ["fee", "fie", "foe"]
# rhymes = [
#     ("flop", "get a mop"),
#     ("fope", "turn the rope"),
#     ("fa", "get your ma"),
#     ("fudge", "call the judge"),
#     ("fat", "pet the cat"),
#     ("fog", "walk the dog"),
#     ("fun", "say we're done"),
# ]
# start2 = "Someone better"
# start1_caps = " ".join([word.capitalize() + " ! "  for word in start1])
# for first, second in rhymes:
#     print(f"{start1_caps} {first.capitalize()}!")
#     print(f"{start2} {second},")

###################################################121 122 123
# empty_dict = {}
# print(empty_dict)

# bierce = {

#     "day": """A period of twenty-four hours, mostly misspent""",
#     "positive": """Mistaken at the top of one's voice""",
#     "misfortune": """the kind of fortune that never misses""" 
# }

# print(bierce)
# acme_customer = {"first": "white", "middle": "E", "last": "Coyote"}
# print(acme_customer)
# import json
# acme_customer = dict(first="white", middle="E", last= "Coyote")
# # print(json.dumps(acme_customer))
# x =dict(name = "Elmer", ef="hunter")
# print(x)

# lol = [ ["a", "b"], ["c", "d"], ["e", "f"]] ####有lol一定要用 [ [] ]
# print(dict(lol))

# lol = [ ("a", "b"), ("c", "d"), ("e", "f")]   ####用[ () ]印出來會顯示  a : b
# print(dict(lol))

# tol = [ ("a", "b"), ("c", "d"), ("e", "f")]   ####用[ () ]印出來會顯示  a : b
# print(dict(tol))  ##############雙字元字串的串列

# tos = ("ab", "cd", "ef")  ######雙字元字串的tuple
# print(dict(tos))

#################################################124  125  126

# pythons = {
#     "Chapman": "Graham",
#     "Cleese": "john",
#     "Idle": "Eric",
#     "Jones": "Terry",
#     "palin": "Michael",
# }
# pythons["Gilliam"] = "Terry"  ############加入成員
# print(pythons)

# some_pythons = {
#     "Graham": "Chapman",
#     "John": "cleese",
#     "Eric": "Idle",
#     "Terry": "Gilliam",
#     "MIchael": "palin",
# }
# # some_pythons["Gilliam"] = "Terry"  ############加入成員
# print(some_pythons.get("Jofsadf", "not a python"))

# y = 8
# z = lambda x:x * y
# print(z(6))

# signals = {"green": "go", "yellow": "go faster", "red": "smile for the camera"}
# # print(signals.keys())        ######keys   
# # print(list(signals.keys()))  ######list   字典的抬頭
# # print(list(signals.values()))  ######values 字典的內容
# # print(list(signals.items()))     ######items  字典全部
# print(len(signals))               #######len    字典長度  (3)

#####################################127  128  129  130 131
# first = {"a":"agony", "b":"bliss"}
# second = {"b":"bagels", "c":"candy"}
# third = {"d": "donuts"}
# print({**first,**second, **third})  ######print ({})加** 才能把字典結合

# pythons = {
#     "Chapman": "Graham",
#     "Cleese":  "John",
#     "Gilliam": "Terry",
#     "Idle":    "Eric",
#     "Jones":   "Terry",
#     "Palin":   "Michael",
# }
# others = {"Marx": "Groucho", "Howard": "Moe"}
# ithers = {"open": "my", "you": "school"}
# pythons.update(others)   #########用update()結合
# pythons.update(ithers) 
# print(pythons)

# first = {"a": 1 , "b": 2}
# second = {"b": "platypus"}
# first.update(second)
# print(first)

# pythons = {
#     "Chapman": "Graham",
#     "Cleese":  "John",
#     "Gilliam": "Terry",
#     "Idle":    "Eric",
#     "Jones":   "Terry",
#     "Palin":   "Michael",
# }
# others = {"Marx": "Groucho", "Howard": "Moe", "a": "a"}
# pythons.update(others)   #########用update()結合
# # del pythons["Marx"]     #########用del刪除字典裡一個單字
# # print(pythons.pop("Palin"))  ######pop放在print裡面 字典相對應的單字也會印出來
# # print(len(pythons))
# # pythons.clear()                ###########clear清除所有項目
# # pythons ={}                    ###########{}放在最下面就能清除所有項目
# print("Chapman" in pythons)      ###########在print裡面用in來確認是否單字存在

# signals = {"green": "go",
#            "yellow": "go faster",
#            "red": "smaile for the camera"}
# origina_signals = signals.copy()   ########copy在上面blue字典就不會印出來
# signals["blue"] = "confuse evertone"   #############[]=XXX 才能加入一個字典單字
# # save_signals = signals
# print(origina_signals)

# signals = {"green": "go",
#            "yellow": "go faster",
#            "red": ["stop", "smile"]}
# # signals_copy = signals.copy()  
# signals["red"][1] = "sweat"   #######signals [][]改變red串列的值
# print(signals)

# import copy
# signals = {"green": "go",
#            "yellow": "go faster",
#            "red": ["stop", "smile"]}
# signals_copy = copy.deepcopy(signals)  ######深度拷貝
# signals["red"][1] = "sweat" ##########擺在deepcopy上面印出sweat 擺在下面印出smile
# print(signals_copy)

#####################################132  133   134
# a = {1:1, 2:2, 3:3}
# b = {3:3, 1:1, 2:2}
# print(a == b)     ###############比較字典 ==
# a = {1: [1, 2], 2: [1], 3:[1]}
# b = {1: [1, 2], 2: [1], 3:[1]}
# print(a == b)

# accusation = {"room": "ballroom", "weapon": "lead pipe",
#               "person": "col. Mustard"}
# for card in accusation:     ########accustion 印出字典的鍵
#     print(card)
# for value in accusation.values():  ####accusation.values 印出字典的內容
#     print(value)
# for item in accusation.items():   ######accusation.items 印出所有字典
#     print(item)
# for card, contents in accusation.items():  ####讓字典變成一句話
#     print("Card", card, "has the contents", contents)

# {Rey_expression: value_expression for expression in iterable}
# word = "letters"   
# # letter_counts = {letter:word.count(letter) for letter in word}
# letter_counts = {letter:word.count(letter) for letter in set(word)}  ##印出順便不一樣
# print(letter_counts)  ############letters單字 印出 L.1個 E.2個 T.2個 r.1個

# vowels = "aeiou"
# word = "onomatopoeia"   
# vowel_counts = {letter: word.count(letter) for letter in set(word)
#                 if letter in vowels}  
# print(vowel_counts)  #兩個單字 印出有幾個字母重疊
    
####################################  135 136 137 138 139 140 141
# empty_set = set()
# print(empty_set)
# even_numbers = {0, 2, 4, 6, 8}
# print(even_numbers)
# odd_numbers = {1, 3, 5, 7, 9}
# print(odd_numbers)
# print(set("letters"))    ########用set印出是無順序的

# print(set(["Dasher", "Dancer", "Prancer", "Mason-Dixon"]))  ###串列  set是無序
# print(set(("Ummagumma", "Echoes", "Atom Heart Mother")))   ####tuple set是無序
# print(set({"apple": "red", "orange": "orange", "cherry": "red"}))###字典的抬頭
# reindeer = set(["Dasher", "Dancer", "Prancer", "Mason-Dixon"])
# print(len(reindeer)) ##用set就要用()  沒有set也能印出len   
# s = set ((1, 2, 3))
# # s.add(4) ##用add加入4
# s.remove(3) ##用remove刪除3
# print(s)
# funriture = set(("sofa", "ottoman", "table"))
# for piece in funriture:
#     print(piece) ####for加set印出也是無順序
drinks = {
    "martini": {"vodka", "vermouth"},
    "black russian": {"vodka", "kahlua", "coffee"},
    "white russian": {"cream", "kahlua", "vodka"},
    "manhattan": {"rye", "vermouth", "bitters"},
    "screwdriver": {"orange juice", "vodka"}
}
# for  name, contents in drinks.items():
#     if "vodka" in contents:  #####找出有vodka
#         print(name)

# for name, contents in drinks.items():
#     if "vodka" in contents and not ("vermouth" in contents or "cream" in contents):
#         print(name)   ###找出vodka並挑出內容有 "vermouth" "cream"就不印出

# for name, contents in drinks.items():
#     if contents & {"vermouth", "orange juice"}:
#         print(name)   ##找出有vermouuth和orange 

# for name,contents in drinks.items():
#     if "vodka" in contents and not contents & {"vermouth", "cream"}:
#         print(name)

bruss = drinks["black russian"]  ####black  title
wruss = drinks["white russian"]  ####white  title
a = {1100, 1100, 1, 1100}
b = {10, 1100}
print(a&b)  ####找出兩個的內容相同  並列印
print(a.intersection(b))
print(bruss&wruss)  ##找出兩個的內容相同 並列印
print(bruss|wruss)  ##印出兩個的內容
print(a|b)  ###a和b 印出內容不相同 
print(a.union(b))
print(a-b)   ###a-b 找出兩個的內容相 並列印 a 剩的內容  如果是b-a 就印出 b 剩的內容
print(a.difference(b))  ##加difference就變成集合
print(bruss^wruss)  ##找出兩個的內容不相同 並列印
print(a<=b)
print(a.issubset(b))
print(bruss<=wruss)
print(a<=a)
print(a.issubset(a)) ###issubset變成不可集合
print(a<b)
print(a<a)
print(bruss<wruss)
print(a>=b)
print(a.issuperset(b)) ###superset超集合是子集合的相反
print(wruss>=bruss)
print(a>=a)
print(a.issuperset(a))###任何集合都是它自己的超集合
print(a>b)
print(wruss>bruss)
print(a>a)  #############不可能自己是超集合
a_set = {number for number in range(1,6) if number % 3 ==1}
print(a_set)
print(frozenset([3, 2, 9])) ########用frozenset = 冰凍凝固
print(frozenset(set([1, 3, 2])))
print(frozenset({3, 1, 2}))
print(frozenset((2, 1, 3)))
fs = frozenset([3, 1, 2])
print(fs)
print(fs.add(3))####用frozenset = 冰凍凝固 就無法用add加入


 


























