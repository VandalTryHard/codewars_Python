"""5 kyu
Extract the domain name from a URL
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
"""


### How this works
from tld import get_tld
domain_name = "http://github.com/carbonfive/raygun"
domain_name = get_tld(domain_name, as_object=True)
print(domain_name.domain)
