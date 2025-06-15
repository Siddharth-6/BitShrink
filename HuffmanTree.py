class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

class HuffmanTree:
    def __init__(self, heap):
        while len(heap) > 1:
            left = heap.extract()
            right = heap.extract()
            merged = Node(None, left.freq + right.freq, left, right)
            heap.insert(merged)
            
        self.root = heap.extract()

def generate_codes(node, prefix='', code_map=None, char_map=None):
    if code_map is None:
        code_map = {}
    if char_map is None:
        char_map = {}
    if node is None:
        return code_map,char_map
    # Leaf node → character has a code
    if node.char is not None:
        code_map[node.char] = prefix
        char_map[prefix] = node.char
    else:
        generate_codes(node.left, prefix + '0', code_map,char_map)
        generate_codes(node.right, prefix + '1', code_map,char_map)
    return code_map,char_map
