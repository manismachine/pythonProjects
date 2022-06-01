from os import system
import time

def start_webBrowser():
    youtube_song = 'https://www.youtube.com/watch?v=21It4kL21VU'
    github_link = 'https://github.com/manismachine/secpro'
    exploit_db = 'https://www.exploit-db.com/docs/english/33864-android-keystore-stack-buffer-over%EF%AC%82ow.pdf'
    hackerrank = 'https://www.hackerrank.com/auth/login'
    stackoverflow = 'https://stackoverflow.com/questions/69944735/android-pre-launch-error-unsafe-cipher-mode'
    urls = [github_link, exploit_db, hackerrank, stackoverflow]

    # chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    # chrome_type = '-incognito'
    # system(f"\"{chrome_path}\" {chrome_type} {url}")

    edge_path = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
    edge_type = '-inprivate'
    for item in urls:
        system(f"\"{edge_path}\" {edge_type} {item}")


def start_software():
    atom_path = r"C:\\Users\\sam\\AppData\\Local\\atom\\atom.exe"
    pycharm_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\PyCharm Community Edition 2021.3.3"
    androidstudio_path = r"D:\\android-studio-2021.3.1.5-windows\\android-studio\\bin\\studio64.exe"
    opnvpn_path = r"C:\\Program Files\\OpenVPN\\bin\\openvpn-gui.exe"
    opnvpn_connect = r"C:\\Users\\sam\\PycharmProjects\\pythonProject\\ovpn_connect.bat"
    urls = [pycharm_path, androidstudio_path]

    for item in urls:
        system(f"{item}")

    start_webBrowser()


if __name__ == '__main__':
    start_software()
