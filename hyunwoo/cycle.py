

def check_cycle(value):
    cnt = 1
    build_num = build_step_1(value)
    while value != build_num:
        cnt = cnt + 1
        build_num = build_step_1(build_num)
    return cnt


def build_step_1(value):
    """
    알고리즘 규칙에 의해 값을 뽑아낸다.
    :param value:
    :return:
    """
    split_num = build_step_2(value)
    add_num = build_step_3(split_num.get('left'), split_num.get('right'))
    new_split_num = build_step_2(add_num)
    build_num = build_step_4(split_num.get('right'), new_split_num.get('right'))
    return build_num


def build_step_2(value):
    """
    값을 오른쪽 자리 값과, 왼쪽 자리 값으로 분리한다.
    :param value:
    :return:
    """
    right = 0
    left = 0
    if value < 10:
        right = value
    else:
        value = str(value)
        left = int(value[0])
        right = int(value[1])
    return dict(left=left, right=right)


def build_step_3(left, right):
    """
    오른쪽 자릿 수와 왼쪽 자리 수의 합을 구한다.
    :param right:
    :param left:
    :return:
    """
    return right + left


def build_step_4(origin_right, new_right):
    """
    연산 시작시의 오른쪽 자릿 수와 만들어진 값의 오른쪽 자릿 수를 순서대로 이어붙인다.
    :param origin_right:
    :param new_right:
    :return:
    """
    return int(str(origin_right)+str(new_right))


number = input()
print(check_cycle(int(number)))


