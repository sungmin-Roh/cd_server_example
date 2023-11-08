#!/usr/bin/env python3
# test5
import socket
import time

# 서버의 IP 주소와 포트 번호를 설정합니다.
IP_ADDR = '0.0.0.0'
TCP_PORT = 8080
BUFFER_SIZE = 1024  # 버퍼 사이즈 설정

# 소켓을 생성하고 옵션을 설정한 다음, IP 주소와 포트 번호에 바인드합니다.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((IP_ADDR, TCP_PORT))

# 연결을 기다리는 상태로 설정합니다. 한 번에 하나의 연결만 허용합니다.
s.listen(1)

# 무한 루프를 통해 클라이언트 연결을 계속 받습니다.
while True:
    # 클라이언트의 연결을 받아들입니다.
    conn, addr = s.accept()
    print('Client address:', addr)

    # 클라이언트로부터 데이터를 받습니다.
    data = conn.recv(BUFFER_SIZE)

    # 받은 데이터에 현재 시간을 추가합니다.
    currentTime = " " + "updated4 !!! " + str(time.time()) + "\r\n"
    print(data.decode('utf-8'))

    # 데이터에 현재 시간을 추가한 후 클라이언트에 다시 보냅니다.
    data = data + currentTime.encode('ascii')
    conn.send(data)  # echo

    # 연결을 닫습니다.
    conn.close()


