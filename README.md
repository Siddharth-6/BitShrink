# 🚀 BitShrink

**BitShrink** is a blazing-fast, Python-powered file compressor based on **Huffman Encoding**. Shrink your bits, not your ideas. Whether you're looking to optimize storage or dive into data compression, BitShrink is your go-to minimalist tool.

## 📂 Project Structure

- `main.py` – The entry point: handles compression, decompression, and evaluation.
- `Compressor.py` – Builds frequency map and manages the custom min-heap.
- `HuffmanTree.py` – Constructs the Huffman Tree and encoding maps.
- `Decompressor.py` – Reverses the bitstream using the tree to restore original data.

## ⚙️ How It Works

1. 📊 **Analyze**: Scans your file and builds a frequency map.
2. 🌲 **Encode**: Constructs a Huffman Tree using a custom heap and generates binary codes.
3. 🧠 **Compress**: Encodes the file into a compact bitstream.
4. 🔁 **Decompress**: Reconstructs the original content using the Huffman Tree.
5. 📈 **Evaluate**: Reports compression ratio and accuracy.

## ✅ Requirements

- Python 3.x
- Install the required package:
  ```bash
  pip install bitarray
  ```

## 🚀 How to Run

1. Clone the repository or download the files.
2. Place the text file you want to compress in the project directory.
3. Run the script:
   ```bash
   python main.py
   ```
4. Enter the file path when prompted (e.g., `example.txt`).

The script will:
- Create a compressed file: `example.txt.huff`
- Decode it to: `example.txt.decoded`
- Show compression percentage and decoding accuracy.

Outputs:

- Compressed file: `example.txt.huff`
- Decompressed file: `example.txt.decoded`
- Stats on compression percentage and accuracy

## 📊 Example Output

```
Enter the path to the file: example.txt

File has been successfully compressed and saved to example.txt.huff

Compression Percentage: 45.38%

File has been successfully decoded and saved to example.txt.decoded
```

## 📌 Notes

- Ideal for plain text files.
- Compression performance improves with text redundancy.

## 🎯 Why BitShrink?

- 🔬 Learn Huffman Encoding by example
- 💼 Lightweight and dependency-free (except `bitarray`)
- 📦 Useful for educational and experimental compression needs


🪪 MIT License • 🧠 Powered by Data Structure & Algorithms • 💻 Built with Python
