def frequency(s):
  h = dict()
  for char in s:
    if char not in h:
      h[char]=1
    else:
      h[char]+=1
  return h


class Heap:
    def __init__(self, comparator):
        self.data = []
        self.comparator = comparator  # function: returns True if a < b

    def insert(self, item):
        self.data.append(item)
        self._sift_up(len(self.data) - 1)

    def extract(self):
        if not self.data:
            raise IndexError("pop from empty heap")
        self._swap(0, len(self.data) - 1)
        item = self.data.pop()
        self._sift_down(0)
        return item

    def peek(self):
        if not self.data:
            raise IndexError("peek from empty heap")
        return self.data[0]

    def _sift_up(self, idx):
        parent = (idx - 1) // 2
        if idx > 0 and self.comparator(self.data[idx], self.data[parent]):
            self._swap(idx, parent)
            self._sift_up(parent)

    def _sift_down(self, idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        n = len(self.data)

        if left < n and self.comparator(self.data[left], self.data[smallest]):
            smallest = left
        if right < n and self.comparator(self.data[right], self.data[smallest]):
            smallest = right

        if smallest != idx:
            self._swap(idx, smallest)
            self._sift_down(smallest)

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return repr(self.data)


