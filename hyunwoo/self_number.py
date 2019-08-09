

def build_not_self_num(num):
    """
    입력한 값, 생성자로 값을 만든다.
    :param num: 생성자
    :return: 만들어진 값
    """
    digits = str(num)
    result = num
    for digit in digits:
        result = result + int(digit)
    return result


def build_list_not_self_num(min_num, max_num):
    """
    생성자를 통해 만들어지는 값의 목록을 만든다.
    :param min_num: 생성자 시작값
    :param max_num: 생성자 끝값
    :return: 만들어진 값의 목록
    """
    build_list = list()
    for i in range(min_num, max_num):
        build_list.append(build_not_self_num(i))
    return build_list


def function_c(min_num, max_num):
    """
    숫자의 범위 안에서 싱글 넘버를 찾는다.
    :param min_num: 찾고자 하는 영역의 시작값
    :param max_num: 찾고자 하는 영역의 끝값
    :return: 싱글 넘버 리스트
    """
    not_self_num_list = build_list_not_self_num(min_num, max_num)
    self_num_list = list()
    for i in range(min_num, max_num):
        if i not in not_self_num_list:
            self_num_list.append(i)
    return self_num_list


print(function_c(1, 10000))
