import xml.sax

class CellHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.xmin = []
        self.ymin = []
        self.xmax = []
        self.ymax = []
        self.labelset = set()

    # 元素开始事件处理
    def startElement(self, tag, attributes):
        self.CurrentData = tag                   # 把当前标签 传给 current data

            
    # 内容事件处理
    def characters(self, content):
        #print(self.CurrentData, content)
        if self.CurrentData == 'name':           # 如果 当前 标签 是 name，就把 name 对应的 内容 放进 集合，然后 调用 元素结束
            self.labelset.add(content)
        if 'WBC' in self.labelset:
            if self.CurrentData == "xmin":
                self.xmin.append(int(content))
            elif self.CurrentData == "ymin":
                self.ymin.append(int(content))
            elif self.CurrentData == "xmax":
                self.xmax.append(int(content))
            elif self.CurrentData == "ymax":
                self.ymax.append(int(content))
                self.labelset = set()
            
            
    # 元素结束事件处理
    def endElement(self, tag):
        self.CurrentData = "" 

#if (__name__ == "__main__"):                        # 如果 单独执行 这一个文件
def parser(annot_path):
    
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = CellHandler()
    parser.setContentHandler(Handler)
    parser.parse(annot_path)
    return Handler.xmin,Handler.ymin,Handler.xmax,Handler.ymax
