from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False

    """
    i = 1
    if x < 10:
        return True
    times = len(str(x))
    while times:
        ''' last_1= x%10
            last_2 = x//10%10
            last_3 = x//100%10.......'''
        if x//i%10 >= x//(10*i)%10:
            i *= 10
            times -= 1
        else:
            return False
    return True
        

def get_k_run_starter(n, k):
    """Returns the 0th digit of the kth increasing run within n.
    >>> get_k_run_starter(123444345, 0) # example from description
    3
    >>> get_k_run_starter(123444345, 1)
    4
    >>> get_k_run_starter(123444345, 2)
    4
    >>> get_k_run_starter(123444345, 3)
    1
    >>> get_k_run_starter(123412341234, 1)
    1
    >>> get_k_run_starter(1234234534564567, 0)
    4
    >>> get_k_run_starter(1234234534564567, 1)
    3
    >>> get_k_run_starter(1234234534564567, 2)
    2
    """
    def length(x):
        i=0
        while x!=0:
            x=x//10
            i+=1
        return i
    #定义一个函数用来求一个int数据的长度，最后一步才用到这个函数
    # 的位数大小初值设为1
    final=None
    #用final作为最后的返回值，定初值为None
    num2=n
    #num2是用来统计每次从n右边开始删掉一个递增数据后n剩余的数字，初始值是n
    # 例如n为123444345删掉一次后为123444
    my_list=[]
    #用来存放n这个数据的所有递增序列的列表
    '''
    拆分方法是判断右边数字是否比左边数字大如果是，就让i变量自增，当这个循环条件不满足之后
    之后用n%（10**i）就可以得到从n右边开始的第一个递增序列，然后把他加进列表，同时用变量
    num2来记录n//（10**i）得到把n从右边去掉此递增序列后的剩余数字，重复进行此操作以获得
    全部递增序列
    '''
    while n!=0:
        i=1
        # 这里的i是用来统计输入的int数据n从右边开始往左数的第一个递增序列（此序列下标0）
        while n % 10 > n % 100 // 10:
            #判断右边数字是否比左边数字
            i+=1
            n=n//10
            #每循环一次就让n的数字删除一位
        my_list.append(num2 % (10 ** i))
        num2=num2//(10**i)
        #num2 % (10 ** i)得到的是递增序列，num2//(10**i)得到的是去掉递增序列后的剩余数据
        n=n//10
        #在这里让n再次//10是因为循环执行了两次，意味着n//10了两次，但是i的值已经是3，所以
        #要再次//10来让数位匹配到刚删除完递增序列后的数字
        #这里的n和num2容易混淆，n的作用是让循环可以继续下去，num2则是用来提取递增序列
    final=my_list[k]//(10**(length(my_list[k])-1))
    #my_list[k]就是要求的那个递增序列，用开始定义的length函数求他的长度，
    # my_list[k]//(10**(length(my_list[k])-1))求首位数字
    return final


def make_repeater(func, n):
    """Return the function that computes the nth application of func.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
    def repeated_func(x):
        result = x
        for _ in range(n):
            result = func(result)
        return result
    return repeated_func

def composer(func1, func2):
    """Return a function f, such that f(x) = func1(func2(x))."""
    def f(x):
        return func1(func2(x))
    return f


def apply_twice(func):
    """ Return a function that applies func twice.
    func -- a function that takes one argument

    >>> apply_twice(square)(2)
    16
    """
    def twice(x):
        return func(func(x))
    return twice

def div_by_primes_under(n):
    """
    >>> div_by_primes_under(10)(11)
    False
    >>> div_by_primes_under(10)(121)
    False
    >>> div_by_primes_under(10)(12)
    True
    >>> div_by_primes_under(5)(1)
    False
    """
    def _checker(x):
        count = n
        while count>=2:
            if x%count == 0:
               return True
            count -= 1
        return False
    return _checker


def div_by_primes_under_no_lambda(n):
    """
    >>> div_by_primes_under_no_lambda(10)(11)
    False
    >>> div_by_primes_under_no_lambda(10)(121)
    False
    >>> div_by_primes_under_no_lambda(10)(12)
    True
    >>> div_by_primes_under_no_lambda(5)(1)
    False
    """
    def checker(x):
        return False
    i = ____________________________
    while ____________________________:
        if not checker(i):
            def outer(____________________________):
                def inner(____________________________):
                    return ____________________________
                return ____________________________
            checker = ____________________________
        i = ____________________________
    return ____________________________


def zero(f):
    return lambda x: x


def successor(n):
    return lambda f: lambda x: f(n(f)(x))


def one(f):
    """Church numeral 1: same as successor(zero)"""
    "*** YOUR CODE HERE ***"


def two(f):
    """Church numeral 2: same as successor(successor(zero))"""
    "*** YOUR CODE HERE ***"


three = successor(two)


def church_to_int(n):
    """Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(three)
    3
    """
    "*** YOUR CODE HERE ***"


def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n.

    >>> church_to_int(add_church(two, three))
    5
    """
    "*** YOUR CODE HERE ***"


def mul_church(m, n):
    """Return the Church numeral for m * n, for Church numerals m and n.

    >>> four = successor(three)
    >>> church_to_int(mul_church(two, three))
    6
    >>> church_to_int(mul_church(three, four))
    12
    """
    "*** YOUR CODE HERE ***"


def pow_church(m, n):
    """Return the Church numeral m ** n, for Church numerals m and n.

    >>> church_to_int(pow_church(two, three))
    8
    >>> church_to_int(pow_church(three, two))
    9
    """
    "*** YOUR CODE HERE ***"
