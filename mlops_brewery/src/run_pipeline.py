import subprocess

steps = [
    "src/ingest.py",
    "src/preprocess.py",
    "src/train.py"
]

for step in steps:
    subprocess.run(["python", step], check=True)

print("Pipeline finalizado com sucesso")
