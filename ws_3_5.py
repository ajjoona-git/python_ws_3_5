from pprint import pprint as print # 개발 시 디버깅을 위해 사용

# 현재 시스템에 등록된 사용자 수를 나타내는 전역 변수
number_of_people = 0
# 현재 대여 가능한 책의 총 수를 나타내는 전역 변수
number_of_book = 100


def increase_user():
    """
    전역 변수 'number_of_people'의 값을 1 증가시킵니다.
    새로운 사용자가 생성될 때 호출됩니다.
    """
    global number_of_people
    number_of_people += 1


def create_user(name, age, address):
    """
    새로운 사용자 정보를 생성하고 전역 사용자 수를 증가시킵니다.

    Args:
        name (str): 사용자의 이름.
        age (int): 사용자의 나이.
        address (str): 사용자의 주소.

    Returns:
        dict: 생성된 사용자 정보(이름, 나이, 주소)를 담은 딕셔너리를 반환합니다.
    """
    increase_user()
    print(name + '님 환영합니다!')
    user_info = {
        'name': name,
        'age': age,
        'address': address,
    }
    return user_info


# 테스트용 사용자 이름, 나이, 주소 리스트
name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

# map 함수를 사용하여 각 사용자 정보를 생성하고 리스트로 변환
# many_user 리스트는 각 사용자의 딕셔너리 정보를 포함합니다.
many_user = map(create_user, name, age, address)


def rental_book(info):
    """
    사용자가 책을 대여하는 과정을 처리하고 남은 책의 수를 갱신합니다.

    Args:
        info (dict): 대여자의 이름과 대여할 책의 수('age' 키로 표현)가 포함된 딕셔너리.
                     'name'과 'age' 키를 필수로 포함해야 합니다.
    """
    decrease_book(info['age'])
    print(f"{info['name']}님이 {info['age']}권의 책을 대여하였습니다.")

def decrease_book(rented_book):
    """
    전역 변수 'number_of_book'의 값을 대여된 책의 수만큼 감소시킵니다.

    Args:
        rented_book (int): 대여된 책의 수.
    """
    global number_of_book
    number_of_book -= rented_book
    print(f'남은 책의 수 : {number_of_book}')


# # 1. 람다 사용하지 않고 풀기 (주석 처리된 원본 코드)
# def get_info_for_rental(user_info):
#     """
#     기존 사용자 정보(user_info)를 받아, 책 대여에 필요한 형태로 가공하는 함수입니다.
#     대여 규칙(나이를 10으로 나눈 몫)을 적용하여 새로운 딕셔너리를 반환합니다.

#     Args:
#         user_info (dict): 원본 사용자 정보 딕셔너리.
#                           'name'과 'age' 키를 포함해야 합니다.

#     Returns:
#         dict: 이름과, 대여할 책의 수가 담긴 새로운 딕셔너리.
#     """
#     transformed_info = {
#         'name': user_info['name'],
#         'age': user_info['age'] // 10,
#     }
#     return transformed_info


# # transformed_users의 각 항목에 대해 rental_book 함수를 적용하여 책 대여를 처리합니다.
# # list()를 사용하여 map 객체를 소모시키고 모든 대여 작업을 완료합니다.
# transformed_users = map(get_info_for_rental, many_user)
# list(map(rental_book, transformed_users))


# ---

# 2. 람다 사용하기
# 'many_user' 리스트의 각 사용자 정보에 대해 람다 함수를 적용하여
# 이름과 (나이 // 10)으로 계산된 대여 책 수를 포함하는 새로운 딕셔너리 생성
# 이 결과는 map 객체(이터레이터)로 반환됩니다.
transformed_users = map(
    lambda x: {'name': x['name'], 'age': x['age'] // 10}, many_user
)

# transformed_users의 각 항목에 대해 rental_book 함수를 적용하여 책 대여를 처리합니다.
# list()를 사용하여 map 객체를 소모시키고 모든 대여 작업을 완료합니다.
list(map(rental_book, transformed_users))