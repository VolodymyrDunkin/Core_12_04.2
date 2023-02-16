"""Dict 02"""


lst = [i for i in range(10)]

def odd_even(lst):
    result = {"odd":[], "even":[]}
    for i in lst:
        if not i % 2:
            result["even"].append(i)
        else:
            result["odd"].append(i)
    return result


if __name__ == "__main__":
    print(odd_even(lst))