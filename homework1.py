def domain_name(url):
  first_dot = url.find(".") + 1
  second_dot = url.find(".", first_dot)
  slashes = url.find("//") + 2
  if "www." in url:
    return(url[first_dot : decond_dot])
  else:
    return(url[slashes : first_dot - 1])
  
assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"

