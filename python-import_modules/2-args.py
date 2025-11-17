#!/usr/bin/python3
import sys
a = sys.argv[1:]
if len(a) == 0:
    print("0 arguments.")
elif len(a) == 1:
    print("1 argument:")
else:
    print(f"{len(a)} arguments:")
for k, i in enumerate(a, 1):
    print(f"{k}: {i}")

if __name__ == "__main__":
    main()
