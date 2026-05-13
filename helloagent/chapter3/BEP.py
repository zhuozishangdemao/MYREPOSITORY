import re,collections
def get_stats(vocab):
    """
    统计词元对频率
    """
    pairs = collections.defaultdict(int)#生成一个默认的字典，访问不存在的键的时候不会抛出错误，会调用工厂函数（此处为int（））作为默认值
    for word,freq in vocab.items():
        symbols = word.items()
        for i in range(len(symbols)-1):
            pairs[symbols[i],symbols[i+1]]+=freq#这样读入可以使得键为二元组
    return pairs

def merge_vocab(pair,v_in):
    """
    合并词元对
    """
    v_out = {}
    bigram = re.escape(' '.join(pair))#
    #re.escape():对特殊字符转义，将.转义为\.
    p = re.comile(r'(?<!\S)'+bigram+r'(?<!\S)')
    #(?<!pattern)负向回顾后发断言
    for word in v_in :
        w_out = p.sub(''.join(pair),word)#对包含模式的进行合并
        #p.sub(repl,string,count=0)在stirng中查找所有和正则模式p匹配的部分，用repel内容替换
        v_out[w_out] = v_in[word]
    return v_out
    #这一步对与找到的最高频率的词元对，对于原有词语进行匹配

vocab = {'h u g </w>': 1, 'p u g </w>': 1, 'p u n </w>': 1, 'b u n </w>': 1}
num_merges = 4 # 设置合并次数

for i in range(num_merges):
    pairs = get_stats(vocab)
    if not pairs:
        break
    best = max(pairs,key = pairs.get)#key为max参数，表示比较方法，以函数返回值作为比较大小的依据
    vocab = merge_vocab(Best,vocab)
    print(f"第{i+1}次合并: {best} -> {''.join(best)}")
    print(f"新词表（部分）: {list(vocab.keys())}")
    print("-" * 20)