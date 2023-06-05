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
