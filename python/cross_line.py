
import re
stdin = "M3 is a company which provides medical-related services through the use of the Internet since 2000. M3 stands for Medicine, Media and Metamorphosis."
match_num = re.findall('[A-Z]', stdin)
match_large = re.findall('[0-9',stdin)

print(match_num + match_large)