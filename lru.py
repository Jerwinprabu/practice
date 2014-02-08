#!/usr/bin/python
""" Code an LRU cache in python you dipshit """

class LruCache(object):
    "Get'R'Done"
    KEY, VALUE, PREV, NEXT = 0,1,2,3   
    def __init__(self, max_sz):
        NEXT = LruCache.NEXT
        self.max_sz = max_sz
        self.map = {}
        self.head = [None, None, None, None]
        self.tail = [None, None, self.head, None]
        self.head[NEXT] = self.tail
    def addnode(self, node):
        NEXT, PREV = LruCache.NEXT, LruCache.PREV
        assert len(node) == 4
        tail_prev = self.tail[PREV]
        tail_prev[NEXT] = self.tail[PREV] = node
        node[PREV] = tail_prev
        node[NEXT] = self.tail
    def touch(self, name):
        NEXT, PREV = LruCache.NEXT, LruCache.PREV
        assert name in self.map
        node = self.map.get(name)
        _, _, prev_node, next_node = node
        prev_node[NEXT] = next_node
        next_node[PREV] = prev_node
        self.addnode(node)
        
    def __getitem__(self, name):
        VALUE = LruCache.VALUE
        if name in self.map:
            self.touch(name)
            return self.map.get(name)[VALUE]
        else:
            return None
        
    def __setitem__(self, key, value):
        NEXT, PREV, KEY = LruCache.NEXT, LruCache.PREV, LruCache.KEY
        if key in self.map:
            self.touch(key)
            self.map[key][VALUE] = value
        else:
            if len(self.map) == self.max_sz:
                head_old = self.head[NEXT]
                head_new = head_old[NEXT]
                self.head[NEXT] = head_new
                head_new[PREV] = self.head
                del self.map[head_old[KEY]]
                del head_old
            node = [key, value, None, None]
            self.map[key] = node
            self.addnode(node)
    def _snode(self, node):
        KEY, VALUE = LruCache.KEY, LruCache.VALUE
        return "({},{})".format(node[KEY],node[VALUE])
    def _slist(self, node):
        NEXT = LruCache.NEXT
        if node and (node is not self.tail):
            yield self._snode(node)
            for s in self._slist(node[NEXT]):
                yield s
        else:
            yield ""
    def __str__(self):
        NEXT = LruCache.NEXT
        l = [node for node in self._slist(self.head[NEXT])]
        return ",".join(l)
        
def test():
    print "Running test"
    inp = {"batman":"robin", "hanz":"franz",
           "derf":"herf","derpina":"herpina"}
    cache = LruCache(4)
    for key, val in inp.items():
        print "key, val:", key, val
        cache[key] = val
        print "FINAL:", cache

    print cache["hanz"]
    print cache["derpina"]
    print cache["batman"]

    print cache

    cache["foo"] = "Bar"
    print cache

if __name__ == "__main__":
    test()
