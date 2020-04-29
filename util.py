import sys
import os


def key_pressed():
    try:
        import tty, termios
    except ImportError:
        try:
            # probably Windows
            import msvcrt
        except ImportError:
            # FIXME what to do on other platforms?
            raise ImportError('getch not available')
        else:
            key = msvcrt.getch().decode('utf-8')
            return key
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def print_avatar(DIRPATH, avatar_index):
    avatars_atributes = files_managment.import_data_to_dict(DIRPATH, "avatars_files", "avatars_atributes.csv")
    avatars_atributes_for_printing = files_managment.import_data_to_dict(DIRPATH, "avatars_files", "avatar_atributes_for_printing.csv")
    all_avatars = list(avatars_atributes.keys())
    avatar_image_file = avatars_atributes_for_printing[all_avatars[avatar_index]]["image"]
    avatar_image = files_managment.read_image_file(DIRPATH, "avatars_files", avatar_image_file)
    avatar_details = f"{avatar_image}\
                        \
                        AVATAR: {all_avatars[avatar_index]} ATRIBUTES: {avatars_atributes[all_avatars[avatar_index]]}"
    print(avatar_details)