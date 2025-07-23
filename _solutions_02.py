# 현재 남아 있는 책의 총 수량
number_of_book = 100

# 현재까지 생성된 사용자(회원) 수를 관리하는 전역 변수
number_of_people = 0


def increase_user():
    """
    새로운 사용자가 생성될 때마다
    number_of_people를 1씩 증가시키는 함수입니다.
    """
    global number_of_people
    number_of_people += 1


# 각각 사용자 이름, 나이, 주소에 해당하는 리스트
name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, address):
    """
    전달된 이름(name), 나이(age), 주소(address)를 바탕으로
    사용자 정보를 딕셔너리로 만들어 반환합니다.
    생성된 사용자 수도 1 증가시킵니다.
    """
    increase_user()  # 전체 사용자 수 1 증가
    user_info = {'name': name, 'age': age, 'address': address}
    print(f'{name}님 환영합니다!')
    return user_info


# map 함수를 사용하여 name, age, address 리스트의 각 요소를
# 매핑하여 create_user를 호출하고, 그 결과를 리스트로 변환합니다.
many_user = list(map(create_user, name, age, address))


def rental_book(info):
    """
    사용자 정보(info)를 전달받아,
    1) 사용자 나이(info['age'])만큼 책의 수를 감소시키고,
    2) 대여 처리 후 출력할 메시지들을 튜플 형태로 반환(return)합니다.
    """
    global number_of_book
    rented_count = info['age']
    number_of_book -= rented_count  # 나이만큼 전역 변수 number_of_book 감소

    # 출력할 메시지들을 생성하여 반환
    remaining_msg = f'남은 책의 수 : {number_of_book}'
    rental_msg = f'{info["name"]}님이 {rented_count}권의 책을 대여하였습니다.'
    return remaining_msg, rental_msg


# 1) 사용자 정보에서 age를 10으로 나눈 결과로 변환하는 map
transformed_users = map(
    lambda x: {'name': x['name'], 'age': x['age'] // 10}, many_user
)

# 2) 변환된 사용자 정보를 rental_book에 넘겨 '출력할 메시지'들을 생성하는 map
#    이 시점에서 rental_book 함수가 실행되며 number_of_book 값이 변경됩니다.
rental_messages = map(rental_book, transformed_users)

# 3) map을 통해 반환된 메시지들을 실제로 출력하는 for 반복문
for remaining, rental in rental_messages:
    print(remaining)
    print(rental)
