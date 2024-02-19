from StartupMetaManager import StartupMetaManager


# noinspection SpellCheckingInspection
def set_install_folder(manager: StartupMetaManager) -> str:
    install_folder = input('请输入GTAV安装目录: ')
    manager.set_install_folder(install_folder)
    return install_folder


def set_startup_meta(manager: StartupMetaManager) -> dict:
    while True:
        print('请输入新增启动项')
        input_str = input('的密码或文件路径(-1退出): ')
        if input_str == '-1':
            break
        else:
            nickname = input('请输入此启动项昵称: ').lower()
            try:
                manager.paser_startup_meta_passwd(input_str, nickname)
                print(f'已添加启动项: [{nickname}]')
            except Exception as e:
                print(f'[error] {e}')
    print('\n' * 100)
    return manager.get_startup_meta()


def remove_startup_meta(manager: StartupMetaManager):
    startup_meta = manager.get_startup_meta()
    while True:
        print('现有启动项:')
        nicknames = list(startup_meta.keys())
        for i, nickname in enumerate(nicknames):
            print(f'{i + 1}-> [{nickname}]')
        input_str = input('请输入需要删除的启动项序号(-1退出): ')
        if input_str == '-1':
            break
        elif input_str.isdigit():
            index = int(input_str)
            if 0 < index <= len(nicknames):
                nickname = nicknames[index - 1]
                startup_meta = manager.remove_startup_meta(nickname)
                print(f'已删除启动项: [{nickname}]')
            else:
                print('无效输入...')


# noinspection SpellCheckingInspection
def main():
    manager = StartupMetaManager()

    install_folder = manager.get_install_folder()
    if install_folder is None:
        print('[warning] GTAV安装目录未设置...')
        set_install_folder(manager)

    startup_meta = manager.get_startup_meta()
    if startup_meta is None or len(startup_meta) == 0:
        print('[warning] startup.meta未设置...')
        set_startup_meta(manager)

    while True:
        startup_meta = manager.get_startup_meta()
        install_folder = manager.get_install_folder()

        print(f'GTAV安装目录: [{install_folder}]')
        print('可选启动项:')
        nicknames = list(startup_meta.keys())
        for i, nickname in enumerate(nicknames):
            print(f'{i + 1}-> [{nickname}]')
        print('======')
        print('0-> 取消设置启动项')
        print('-1-> 删除已有启动项')
        print('-2-> 添加新启动项')
        print('-3-> 重新设置GTAV安装目录')

        input_str = input('请输入序号: ')
        if input_str.replace('-', '').isdigit():
            index = int(input_str)
            if index == 0:
                manager.delete_startup_meta_path()
                input('已取消设置启动项...(输入回车继续)')
            elif index == -1:
                remove_startup_meta(manager)
            elif index == -2:
                set_startup_meta(manager)
            elif index == -3:
                set_install_folder(manager)
            elif 0 < index <= len(nicknames):
                nickname = nicknames[index - 1]
                manager.write_startup_meta(nickname)
                input(f'已设置启动项: [{nickname}]...(输入回车继续)')
            else:
                input('无效输入...(输入回车继续)')
        else:
            input('无效输入...(输入回车继续)')
        print('\n' * 100)


if __name__ == '__main__':
    main()
    # pyinstaller --onefile --icon=resource\icon.ico src\Main.py --name=GTAV战局锁工具 --clean
