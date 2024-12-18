![img.png](img.png)
在 Python 中，pop 方法常用于不同的数据结构，如字典（dict）和列表（list）。每种数据结构的 pop 方法签名有所不同。
dict.pop(key, default=None)
key：要删除的键。
	•	default（可选）：如果键不存在时返回的默认值。如果不提供且键不存在，会引发 KeyError。
当您调用 info.pop('age') 时，self 自动指向 info 字典实例，您只需要传递 'age' 作为 key。
	•	PyCharm 的提示 pop(self, __key) 只是展示了方法的完整签名，其中 self 是内部实现细节，用户无需关心。
