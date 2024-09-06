import re
import subprocess


def get_framebuffer_resolution(framebuffer_device):
    fbset_output = subprocess.check_output(["fbset", "-s", "-fb", framebuffer_device])

    for line in fbset_output.split("\n"):
        line = line.strip()
        if line.startswith("geometry"):
            print(line)
            parsed = re.match(r"geometry (\d+) (\d+)", line)
            return (parsed.group(1), parsed.group(2))


print(get_framebuffer_resolution("/dev/fb0"))
