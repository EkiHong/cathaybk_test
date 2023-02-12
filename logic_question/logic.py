# 下個五的倍數
def round_to_next_5(num):
    return num + (5 - num) % 5


def adjust_score(score):
    for name, original_score in score.items():
        round_to_5 = round_to_next_5(original_score)
        # rule 1
        if round_to_5 - original_score < 3:
            new_score = round_to_5
        else:
            new_score = original_score

        # rule 2
        if new_score < 40:
            new_score = original_score
        else:
            new_score = new_score

        print(f"{name} new score = {new_score}")


def calculate_free_fall(times, origin_height):
    distance = []
    rebound = []
    for i in range(1, times + 1):
        # 紀錄第一次落下的距離
        if i == 1:
            distance.append(origin_height)
        # 紀錄第一次以後，落下和回彈的距離
        else:
            distance.append(2 * origin_height)

        # 紀錄回彈的距離
        origin_height = origin_height / 2
        rebound.append(origin_height)

    print(f"Total Distance = {sum(distance)}")
    print(f"Rebound 10 = {rebound[-1]}")


if __name__ == '__main__':
    print(f" ---------- First Question ---------- ")
    original = {'德瑞克': 33, '尚恩': 73, '傑夫': 63, '馬基': 39}
    adjust_score(original)

    print(f" ---------- Second Question ---------- ")
    calculate_free_fall(times=10, origin_height=100)

