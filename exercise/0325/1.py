
"""


"""


def isvalid(a_in, a_out):
    st = []
    n = len(a_in)
    i = 0
    for j in range(n):
        if st and st[-1] == a_out[j]:
            st.pop()
            continue

        while i < n and a_in[i] != a_out[j]:
            st.append(a_in[i])
            i += 1
        if i < n and a_in[i] == a_out[j]:
            i += 1
            pass
        else:
            if st and st[-1] == a_out[j]:
                st.pop()
            else:
                return False

    return True


N = int(input())
data = []
for _ in range(N):
    n = int(input())
    row1 = list(map(int, input().split(' ')))
    row2 = list(map(int, input().split(' ')))
    data.append([row1, row2])

for a, b in data:
    print(isvalid(a, b))

# data = [
#     [[1, 2, 3], [1, 2, 3], ],
#     [[1, 2, 3], [3, 2, 1], ],
#     [[1, 2, 3, 4], [3, 2, 1, 4], ],
#     [[1, 2, 1, 4], [3, 2, 4, 1], ],
# ]
# for a, b in data:
#     print(isvalid(a, b))

