# http://vipprog.net/wiki/exercise.html

"""
平方根を小数点以下60桁まで求める。
"""

def my_square(n):
              x = 1.0
              while 1:
                            if x * x >= n:
                                          x=(x * x + (x - 1) * (x - 1)) / 2
                                          for i in range(0,10):
                                                        j = n / x
                                                        x = (j + x) / 2
                                          print ('%.60f' % x)
                                          break
                            else:
                                          x = x + 1
 
my_square(2)
