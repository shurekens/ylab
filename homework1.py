#Task №1
def domain_name(url):
  first_dot = url.find(".") + 1
  second_dot = url.find(".", first_dot)
  slashes = url.find("//") + 2
  if "www." in url:
    return(url[first_dot : second_dot])
  else:
    return(url[slashes : first_dot - 1])
  
assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"

#Task №2
def int32_to_ip(int32):
  a = int32 // 16777216
  b = (int32 - (a * 16777216)) // 65536
  c = (int32 - (a * 16777216 + b * 65536)) // 256
  d = (int32 - (a * 16777216 + b * 65536 + c * 256))
  return(f"{a}.{b}.{c}.{d}")

assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"

#Task №3
def zeros(n):
  x = 5
  result = 0
  while x < n:
    result += (n // x)
    x *= 5
  return result
assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7

#Task №4
from itertools import combinations

def bananas(s) -> set:
  word = "banana"
  result = set()
  for item in combinations(range(len(s)), len(s) - len(word)):
    list_item = list(s)
    for i in item:
      list_item[i] = "-"
    res = "".join(list_item)
    if res.replace("-", "") == word:
      result.add(res)
  return result

#Task №5
def primfacs(n):
  i = 2
  primfac = []
  while i * i <= n:
    while n % i == 0:
      primfac.append(i)
      n = int(n / i)
    i = i + 1
  if n > 1:
    primfac.append(n)
  return primfac

def count_find_num(primesL, limit):
  numbers_list = []
  for i in range(1, limit + 1):
    if set(primfacs(i)) == set(primesL):
      numbers_list.append(i)
  if len(numbers_list) == 0:
    return []
  return [len(numbers_list), max(numbers_list)]


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []
