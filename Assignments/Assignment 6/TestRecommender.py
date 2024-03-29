'''
@author: Lihong Wang
'''

import SmallDukeEatsReader
import RecommenderEngine


def driver():
    
    (items,ratings) = SmallDukeEatsReader.getdata()
    print("items = ",items)
    print("ratings = ", ratings)
    print()

    avg = RecommenderEngine.averages(items,ratings)
    print("average",avg)
    if avg == [('DivinityCafe', 4.0), ('TheCommons', 3.0),
 ('Tandoor', 2.4285714285714284), ('IlForno', 1.8),
 ('FarmStead', 1.4), ('LoopPizzaGrill', 1.0),
 ('TheSkillet', 0.0), ('PandaExpress', -0.2),
 ('McDonalds', -0.3333333333333333)]:
        print('The averages function works!')
    else:
        print('The averages function does not work!')
    print()

    key = 'Sung-Hoon'
    slist = RecommenderEngine.similarities(key,ratings)
    print(key,slist)
    if slist == [('Wei', 1), ('Sly one', -1), ('Melanie', -2), ('Sarah Lee', -6),
 ('J J', -14), ('Harry', -24), ('Nana Grace', -29)]:
        print('The similarities function works!')
    else:
        print('The similarities function does not work!')
    print()

    key = 'Sarah Lee'
    r3 = RecommenderEngine.recommendations(key,items,ratings,3)
    print("top",r3)
    if r3 == [('Tandoor', 149.5), ('TheCommons', 128.0),
 ('DivinityCafe', 123.33333333333333), ('FarmStead', 69.5),
 ('TheSkillet', 66.0), ('LoopPizzaGrill', 62.0),
 ('IlForno', 33.0), ('McDonalds', -69.5),
 ('PandaExpress', -165.0)]:
        print('The recommendations function works!')
    else:
        print('The recommendations function does not work!')
    print()

        
if __name__ == '__main__':
    driver()