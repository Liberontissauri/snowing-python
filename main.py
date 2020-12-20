from Screen import Screen
import shutil

terminal = Screen(
                    size_x = shutil.get_terminal_size().columns,
                    size_y = shutil.get_terminal_size().lines,
                    snowball_speed = 0.1
                    
                )

terminal.start()