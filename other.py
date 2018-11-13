from train import run

# Here we test `run`
print("======================================================")
print("""run(("--backbone vgg --bz 110 --train").split())""")
run(("--backbone vgg --bz 110 --train").split())

print("======================================================")
print("""run(("--backbone densenet --bz 110 --debug").split())""")
run(("--backbone densenet --bz 110 --debug").split())