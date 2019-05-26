import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode('utf-8')
    return html


# 人人影视
def searchWord_renren(word):
    try:
        word = word.replace(' ', '%20')
        result = getHtml("http://www.91dict.com/words?w=" + word)
        if (result.find('查不到该词') != -1):
            print('查询失败 ' + word)
            # searchWord(word)
            # return ''
        result = result.replace('"/resources', '"http://www.91dict.com/resources')
        result = result.replace('listBox hide', 'listBox')
        result = result[0:result.rfind('<div class="col-sm-12 col-lg-5 checkWord">')]
        result = result[0:result.rfind('<div class="wrapper"')] + result[result.rfind('<section class="content">'):]
        result = result.replace('style="display: none"', '')
        result = result.replace('查看详情', '')
        # result = result.encode('utf-8')
        return result
    except:
        #                print('查询失败 ',word)
        #                searchWord(word)
        return ''


# 科林辞典
def searchWord_kelin(word):
    try:
        word = word.replace(' ', '%20')
        result = getHtml("http://www.youdao.com/w/" + word + "/#keyfrom=dict2.top")
        if (result.find('柯林斯英汉双解大词典') == -1):
            head = result[result.rfind('<head>'):result.rfind('</head>') + 7]
            result = result[result.rfind('<span class="keyword">'):result.rfind('<!-- close webPhrase Tag -->')]
            result = head + result
            # result = str(result, "utf-8")
            # print(result)
            return result
        head = result[result.rfind('<head>'):result.rfind('</head>') + 7]
        result = result[result.rfind('<div id="authTrans" class="trans-wrapper trans-tab">'):result.rfind(
            '<!--例句选项卡 begin-->') + 19]
        result = head + result
        result = result.replace('查看详情', '')
        # result = result.encode('utf-8')
        return result
    except:
        # print('查询失败 ',word)
        # searchWord_renren(word)
        return ''

# result = searchWord_kelin('validation')
# print(result)