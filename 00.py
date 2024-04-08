#def test(*args):
    #sum = 0
   # for n in args:
  #      sum += n
 #   return sum
#print(test(1,2,3,4,5))
#test(3,5)
#test(4,5,6,7)
#test(1,2,3,5,6)


def test(*args, **kwargs):
    print(args, kwargs)
test(1,2,3,4, a=5, b=6, c=7,d='hello')