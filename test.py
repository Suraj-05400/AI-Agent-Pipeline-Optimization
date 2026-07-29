from app.pipeline import Pipeline

document = """

Artificial Intelligence is a branch of computer science.
It focuses on creating systems that can learn from data.


Machine learning algorithms include regression,
classification, clustering and neural networks.


Healthcare applications of AI include disease prediction,
medical image analysis, drug discovery and patient monitoring.


Cybersecurity uses AI for threat detection,
malware analysis and anomaly detection.


Cloud computing provides scalable infrastructure
for deploying artificial intelligence applications.

"""


pipeline = Pipeline()


result = pipeline.run(
    "healthcare applications",
    document * 20
)


print("\nFINAL RESULT")
print("----------------")

print(result)