# ======================================================================
# 1. 전역 변수 (Global Variables) 선언
# ======================================================================
# 프로그램의 여러 부분에서 공동으로 사용하고 상태를 공유해야 하는 변수들입니다.

# 현재 대여 가능한 전체 책의 수량을 저장하는 변수입니다.
number_of_book = 100


def decrease_book(num):
    """
    책의 총 수량(number_of_book)을 지정된 수(num)만큼 줄이고,
    결과를 화면에 즉시 출력하는 함수입니다.
    """
    # 'global' 키워드는 함수 외부(전역 공간)에 선언된 변수를 직접 수정하겠다는 의미입니다.
    global number_of_book

    # 전역 변수 number_of_book의 값을 num만큼 감소시킵니다.
    number_of_book -= num

    # 변경된 후 남은 책의 수를 화면에 출력합니다.
    print('남은 책의 수 : ', number_of_book)


# 현재까지 생성된 총 사용자(회원) 수를 추적하는 전역 변수입니다.
number_of_people = 0


def increase_user():
    """
    새로운 사용자가 생성될 때마다 전체 사용자 수(number_of_people)를 1씩 증가시킵니다.
    """
    global number_of_people
    number_of_people += 1


# ======================================================================
# 2. 데이터 및 사용자 생성 로직
# ======================================================================

# 초기 사용자 정보를 담고 있는 병렬(parallel) 리스트들입니다.
name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, address):
    """
    이름, 나이, 주소를 인자로 받아 사용자 정보 딕셔셔너리를 생성하여 반환합니다.
    """
    increase_user()
    user_info = {'name': name, 'age': age, 'address': address}
    print(f'{name}님 환영합니다!')
    return user_info


# map 함수를 사용하여 name, age, address 리스트의 요소들을 하나씩 꺼내 create_user 함수에 인자로 전달합니다.
many_user = list(map(create_user, name, age, address))


# ======================================================================
# 3. 책 대여 로직 및 실행
# ======================================================================


def rental_book(info):
    """
    한 명의 사용자 정보(info)를 받아 책 대여 처리를 수행하는 함수입니다.
    """
    decrease_book(info['age'])
    print(f'{info["name"]}님이 {info["age"]}권의 책을 대여하였습니다.')


# --- 책 대여 처리 단계 1: 대여할 수량 정보 가공 ---


def transform_user_for_rental(user_info):
    """
    기존 사용자 정보(user_info)를 받아, 책 대여에 필요한 형태로 가공하는 함수입니다.
    대여 규칙(나이를 10으로 나눈 몫)을 적용하여 새로운 딕셔너리를 반환합니다.

    Args:
        user_info (dict): 원본 사용자 정보 딕셔너리

    Returns:
        dict: 이름과, 대여할 책의 수가 담긴 새로운 딕셔너리
    """
    transformed_info = {
        'name': user_info['name'],
        'age': user_info['age'] // 10,  # 대여할 책 수는 나이를 10으로 나눈 몫
    }
    return transformed_info


# 'lambda' 대신 위에서 정의한 'transform_user_for_rental' 함수를 map에 사용합니다.
# map은 many_user 리스트의 각 사용자 정보를 transform_user_for_rental 함수에 전달하여
# 그 반환값들로 새로운 이터레이터를 생성합니다.
transformed_users = map(transform_user_for_rental, many_user)

# --- 책 대여 처리 단계 2: 실제 대여 실행 ---

# list()를 사용해 map 객체를 강제로 순회(iterate)하게 만들어,
# 그 과정에서 rental_book 함수가 각 사용자에 대해 한 번씩 호출되도록 합니다.
list(map(rental_book, transformed_users))
