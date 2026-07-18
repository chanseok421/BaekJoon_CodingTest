def solution(bandage, health, attacks):
    t, x, y = bandage
    max_health = health
    cur_health = health
    combo = 0
    attack_idx = 0
    last_time = attacks[-1][0]

    for time in range(1, last_time + 1):
        if attack_idx < len(attacks) and time == attacks[attack_idx][0]:
            cur_health -= attacks[attack_idx][1]
            combo = 0
            attack_idx += 1
            if cur_health <= 0:
                return -1
        else:
            combo += 1
            cur_health += x
            if combo == t:
                cur_health += y
                combo = 0
            if cur_health > max_health:
                cur_health = max_health

    return cur_health