import platform
# from app_config import CPU_SERIAL

class PIInfo:
    """ Get Pi Details """
    def serial_number(self):
        """ Collect Serial Number """
        if platform.system() == "Windows":
            return CPU_SERIAL
        else:
            with open('/proc/cpuinfo', 'r', encoding="utf-8") as pi_serial_file:
                for line in pi_serial_file:
                    if line.startswith("Serial"):
                        return line.split(":")[1].strip()
            return None
