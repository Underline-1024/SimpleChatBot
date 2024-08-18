from pysenti import ModelClassifier

texts = ["你是傻逼吗？"]
model=ModelClassifier()
for i in texts:
    result = model.classify(i)
    print(i, result)