# class EvenNumbers:
#     def __init__(self, start=0, end=1, step=0):
#         self.start = start
#         self.end = end
#         self.step = step
#
#
#     def __iter__(self):
#         self.value = self.start - self.step
#         return self
#
#
#     def __next__(self):
#         if self.value + self.step < self.end:
#             self.value += self.step
#
#             return self.value
#         else:
#             raise StopIteration()
#
#
# en = EvenNumbers(10, 25, 2)
# for i in en:
#     print(i)


# def all_variants(text):
#
#     for start in range(len(text)):
#         for end in range(start + 1, len(text) + 1):
#
#           yield a, b, c * b
            # yield text[start:end]
            # yield text[start:end]


            # for end in range(start + 1, len(text) + 1):
            #     yield text[start:end]



# for substr in all_variants('abc'):
#     print(substr)


# def all_variants(text):
#
#
#     for start in range(len(text)):
#         for end in range(len(text) + 1):
#             if end % 1 != 0:
#
#                     yield text[start:end]
#         for end in range(start + 1, len(text) + 1):
#                 if end % 1 != 1:
#                     yield text[start:end]
#                 for end in range(len(text)):
#                     if end % 3 != 0:
#                         yield text[end]
#                     for end in range(start + 1, len(text)):
#                         if end % 1 != 0:
#                             yield text[start:end]
#
# z = all_variants('abc')
# for substr in z:
#     print(substr)


# text = 'abcde'
# for count in range(1,len(text) + 1):
#     for i in range(len(text) + 1 - count):
#         print(count, i, i + count)
#         print(text[i: i + count])


# def all_variants(text):
#
#     for count in range(1,len(text) + 1):
#         for i in range(len(text) + 1 - count):
#             print(count, i, i + count)
#             yield(text[i: i + count])
#
#
# for substr in all_variants('abc'):
#     print(substr)

def all_variants(text):
    for count in range(1, len(text) + 1):
        for i in range(len(text) + 1 - count):
            print(count, i, i + count)
            yield (text[i: i + count])


for substr in all_variants('abc'):
    print(substr)









