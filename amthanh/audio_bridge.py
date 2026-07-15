"""
audio_bridge.py
Nhận sự kiện âm thanh từ STM32 (Space Invaders) qua UART và phát ra loa laptop.

Giao thức: mỗi sự kiện là 1 frame 2 byte:
    [0xAA] [code]
- 0xAA  : sync byte, không bao giờ xuất hiện trong text debug ASCII
- code  : ký tự sự kiện, ví dụ 'W' = win/hit, 'L' = lose, 'S' = shoot

Cài đặt thư viện:
    pip install pyserial pygame

Cách dùng:
    1. Sửa SERIAL_PORT bên dưới cho đúng cổng COM (Windows: "COM5", Linux: "/dev/ttyUSB0")
    2. Bỏ 3 file .wav vào cùng thư mục với script này: shoot.wav, hit.wav, lose.wav
       (hoặc đổi tên trong SOUND_MAP cho khớp file bạn có)
    3. Chạy: python audio_bridge.py
"""

import sys
import os
import time
import serial
import pygame

# ==== CẤU HÌNH ====
SERIAL_PORT = "COM7"      # <-- đổi thành cổng COM/ttyUSB thực tế của bạn
BAUD_RATE = 115200         # phải khớp MX_USART1_UART_Init() trong main.c
SYNC_BYTE = 0xAA

# Map code (byte gửi từ STM32) -> file âm thanh tương ứng
SOUND_MAP = {
    ord('S'): "shoot.wav",   # bắn đạn
    ord('W'): "hit.wav",     # bắn trúng địch
    ord('L'): "lose.wav",    # bị bắn trúng / game over
}
# ===================


def load_sounds():
    # Luon lay duong dan tuyet doi theo thu muc CHUA SCRIPT NAY,
    # khong phu thuoc vao thu muc hien tai khi go lenh "python audio_bridge.py"
    script_dir = os.path.dirname(os.path.abspath(__file__))

    sounds = {}
    print(f"Dang tim file am thanh trong: {script_dir}")
    for code, filename in SOUND_MAP.items():
        full_path = os.path.join(script_dir, filename)
        if not os.path.isfile(full_path):
            print(f"  [KHONG THAY] {filename} -> khong ton tai o {full_path}")
            continue
        try:
            sounds[code] = pygame.mixer.Sound(full_path)
            print(f"  [OK] {filename} da load thanh cong")
        except Exception as e:
            print(f"  [LOI] Khong load duoc {filename}: {e}")

    if not sounds:
        print("[CANH BAO] Khong load duoc file am thanh nao ca! Kiem tra lai vi tri file .wav.")
    return sounds


def main():
    pygame.mixer.init()
    sounds = load_sounds()

    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    except Exception as e:
        print(f"[LOI] Khong mo duoc cong {SERIAL_PORT}: {e}")
        sys.exit(1)

    print(f"Da ket noi {SERIAL_PORT} @ {BAUD_RATE} baud. Dang cho su kien am thanh...")

    while True:
        b = ser.read(1)
        if not b:
            continue  # timeout, khong co du lieu, thu lai

        if b[0] != SYNC_BYTE:
            # byte le, khong phai frame am thanh (co the la text debug) -> bo qua
            continue

        code_byte = ser.read(1)
        if not code_byte:
            continue

        code = code_byte[0]
        if code in sounds:
            sounds[code].play()
            print(f"[EVENT] code='{chr(code)}' -> phat am thanh")
        else:
            print(f"[EVENT] code='{chr(code)}' (chua co file am thanh cho code nay)")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nDa dung.")