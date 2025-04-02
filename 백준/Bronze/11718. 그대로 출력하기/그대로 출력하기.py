while True: #무한루프
    try: #try는 Python에서 "오류(예외)가 날 수 있는 코드"를 안전하게 실행하기 위해 사용하는 문법이야.
        line = input()
        print(line)
        
    except EOFError: #EOFError가 발생하면 (즉, 더 이상 입력이 없으면), break로 탈출
        break