test = {
  'name': 'Iterators',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> s = [1, 2, 3, 4]
          >>> t = iter(s)
          >>> next(s)
          Error
          >>> next(t)
          1
          >>> next(t)
          2
          >>> iter(s)
          Iterator
          >>> next(iter(s))
          1
          >>> next(iter(t))
          3
          >>> next(iter(s))
          1
          >>> next(iter(t))
          4
          >>> next(t)
          StopIteration
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> r = range(6)
          >>> r_iter = iter(r)
          >>> next(r_iter)
          0
          >>> [x + 1 for x in r]
          [1, 2, 3, 4, 5, 6]
          >>> [x + 1 for x in r_iter]
          3599898b41ed92836fc2d788cf3c88d2
          # locked
          >>> next(r_iter)
          480e2afbef4ea5033f7ed1d175609b6e
          # locked
          >>> list(range(-2, 4))   # Converts an iterable into a list
          5fbbba1ca6846ab4c8284abcdb653606
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> map_iter = map(lambda x : x + 10, range(5))
          >>> next(map_iter)
          f6b228b9600512664524ace9bb20487f
          # locked
          >>> next(map_iter)
          e8c16581add35bc404672e54d14aa222
          # locked
          >>> list(map_iter)
          f713ba8c5c3e496289c4eb738fbf14ec
          # locked
          >>> for e in filter(lambda x : x % 2 == 0, range(1000, 1008)):
          ...     print(e)
          4c54662f8cc7843b0d0c7304d9aea453
          49997c1f2b100c379b7dc11fbeca9acc
          53d7745981558f7e8c26148d16d17451
          feadf216fc357bcef6948ecbbe485ab2
          # locked
          >>> [x + y for x, y in zip([1, 2, 3], [4, 5, 6])]
          7ad6104e44cc3932c03229aa44e6763f
          # locked
          >>> for e in zip([10, 9, 8], range(3)):
          ...   print(tuple(map(lambda x: x + 2, e)))
          fc256b507aea54543e84f2838c2bbb62
          310160eef8ed7ef357f0a1551017325a
          5256c0c8831146d1adfffbbc4fa65772
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
