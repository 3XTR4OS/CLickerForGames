import json
import threading
import time

import keyboard
import pyautogui


class AutoClicker:
    def __init__(self):  # load settings
        try:
            with open('settings.json', 'r', encoding='utf-8') as file:
                settings = json.load(file)

            self.CLICK_SPEED: float = settings['CLICK_SPEED']
            self.START_STOP_HOTKEY: str = settings['START_STOP_HOTKEY']
            self.EXIT_HOTKEY: str = settings['EXIT_HOTKEY']
            self.running: bool = False
            self.clicker_thread: None | threading.Thread = None

        except (FileNotFoundError, KeyError, json.JSONDecodeError) as e:
            print(f"Ошибка чтения файла настроек 'settings.json': {e}")
            print("Будут использованы настройки по умолчанию.")

            self.CLICK_SPEED = 0.05
            self.START_STOP_HOTKEY = 'v'
            self.EXIT_HOTKEY = 'q'

    def _click_loop(self) -> None:
        """Этот метод выполняется в отдельном потоке и выполняет клики."""
        while self.running:
            pyautogui.click()
            time.sleep(self.CLICK_SPEED)

    def toggle_clicking(self) -> None:  # (вкл/выкл)
        if not self.running:
            self.running = True
            self.clicker_thread = threading.Thread(target=self._click_loop, daemon=True)
            self.clicker_thread.start()

            print(f"Кликер запущен. Нажмите '{self.START_STOP_HOTKEY}' для остановки.")

        else:
            self.running = False  # Поток завершится сам, так как self.running станет False.

            print("Кликер остановлен.")


def main():
    clicker = AutoClicker()
    print(f"Нажмите '{clicker.START_STOP_HOTKEY}' для [старта] ИЛИ [остановки] кликера.")
    print(f"Нажмите '{clicker.EXIT_HOTKEY}' для выхода из программы.")

    keyboard.add_hotkey(clicker.START_STOP_HOTKEY, clicker.toggle_clicking)
    keyboard.wait(clicker.EXIT_HOTKEY)

    print("Программа завершена.")


if __name__ == "__main__":
    main()
