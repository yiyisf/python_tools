"""
查询维基百科
"""

import wikipedia

# 设置语言
wikipedia.set_lang('en')

# 搜索词条
zhang = wikipedia.search('zhang')
# print(zhang)
# print(zhang[-1])

# 搜索词条信息(Zhang Ziyi)
print(wikipedia.summary(zhang[-1], sentences=1))  #一句话描述
"""
ng Ziyi ([ʈʂáŋ tsɨ̀.ǐ]; Chinese: 章子怡; born 9 February 1979) is a Chinese actress and model.
"""
ziyi = wikipedia.page(zhang[-1]) #获取词条
print(ziyi.content) #词条内容
print(ziyi.links) #链接

