import Compressor
import Decompressor
import HuffmanTree
import os
from bitarray import bitarray

def calculate_compression_percentage(original_file_path, compressed_file_path):
    original_size = os.path.getsize(original_file_path)
    print("Original Size:", original_size, "bytes")
    compressed_size = os.path.getsize(compressed_file_path)
    print("Compressed Size:", compressed_size, "bytes")
    compression_percentage = ((original_size - compressed_size) / original_size) * 100
    
    return compression_percentage

def Accuracy(original_file_content, decoded_file_content):
    temp = 0
    for char in original_file_content:
        if char in decoded_file_content:
            temp += 1

    return temp / len(original_file_content) * 100

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

print("")
file_path = input("Enter the path to the file: ").strip('"')
print("")
file_content = read_file(file_path)

freq_map = Compressor.frequency(file_content)
# print("Frequency Map:", freq_map)

min_heap = Compressor.Heap(lambda x, y: x.freq < y.freq)
for char, freq in freq_map.items():
    min_heap.insert(HuffmanTree.Node(char, freq))

hTree = HuffmanTree.HuffmanTree(min_heap)
# print("Huffman Tree Root Frequency:", hTree.root.left.freq)
code_map,char_map = HuffmanTree.generate_codes(hTree.root)
# print("Code Map:", code_map)

encoded_content = bitarray()
for char in file_content:
    encoded_content.extend(code_map[char])

output_file_path = file_path + ".huff"
with open(output_file_path, 'wb') as file:
    encoded_content.tofile(file)

print(f"File has been successfully compressed and saved to {output_file_path}")
print("")

print("Compression Percentage: {:.2f}%".format(calculate_compression_percentage(file_path, output_file_path)))
print("")

decoded_content = Decompressor.decode_content(encoded_content, hTree.root)

# Save the decoded content to a file
decoded_file_path = file_path + ".decoded"
with open(decoded_file_path, 'w') as file:
    file.write(decoded_content)

print(f"File has been successfully decoded and saved to {decoded_file_path}")
print("")

print("Accuracy: {:.2f}%".format(Accuracy(file_content, decoded_content)))
print("")