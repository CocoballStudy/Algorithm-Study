num = int(input())
files = {}

for i in range(num):
    file = input().split('.')[1] # . 기준으로 잘라서 확장자만 저장
    if file not in files:
        files[file] = 1
    else:
        files[file] += 1

# 확장자 오름차순 정렬
for k, v in sorted(files.items(), key=lambda x: x[0]):
    print(k, v)