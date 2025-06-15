from bitarray import bitarray

def decode_content(encoded_bits, huffman_tree_root):
    decoded_content = ""
    current_node = huffman_tree_root

    for bit in encoded_bits:
        if bit == 0: 
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.left is None and current_node.right is None:
            decoded_content += current_node.char
            current_node = huffman_tree_root  

    return decoded_content


