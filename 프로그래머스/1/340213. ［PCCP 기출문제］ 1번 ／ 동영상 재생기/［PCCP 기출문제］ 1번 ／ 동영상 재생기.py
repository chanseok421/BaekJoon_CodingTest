def solution(video_len, pos, op_start, op_end, commands):
    to_sec = lambda t: int(t[:2]) * 60 + int(t[3:])
    total, cur = to_sec(video_len), to_sec(pos)
    op_s, op_e = to_sec(op_start), to_sec(op_end)

    def skip_op(t):
        return op_e if op_s <= t <= op_e else t

    cur = skip_op(cur)
    for cmd in commands:
        if cmd == "prev":
            cur = max(0, cur - 10)
        else:  # "next"
            cur = min(total, cur + 10)
        cur = skip_op(cur)

    return f"{cur // 60:02d}:{cur % 60:02d}"