#!/usr/bin/python3
for alpha_letters in range(97, 123):
    if alpha_letters == e or alpha_letters == q:
        continue
    print("{:c}".format(alpha_letters), end=" ")
